#!/usr/bin/env python3
"""Oncoskill PHI/PII pre-commit scan (v0).

A simple, dependency-free safety net to catch accidental personal/medical data before it is
committed. It is a *development tool* — it is NOT part of the installable skill and does no
network access.

What it does: scans text files for high-signal patterns (emails, phone numbers, dates of birth,
long national-ID-like digit runs) and known sensitive keywords, and warns on any file under a
private/ or evals-private/ path that is about to be tracked.

It is intentionally conservative: it flags *candidates* for a human to review. False positives are
expected (and acceptable) — this is a tripwire, not an authority.

Usage:
    python scripts/phi_scan.py [paths ...]      # scan given files/dirs (default: repo root)
    python scripts/phi_scan.py --staged         # scan only git-staged files (for a pre-commit hook)

Exit code 1 if any candidate is found, else 0.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys

# High-signal patterns. Deliberately simple.
PATTERNS = {
    "email": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    # international-ish phone: + or 00, then 8+ digits possibly grouped
    "phone": re.compile(r"(?<!\w)(?:\+|00)\d[\d\s().-]{7,}\d"),
    # dates of birth like 01/02/1970, 1970-02-01, 01.02.1970
    "dob": re.compile(r"\b(?:\d{1,2}[./-]\d{1,2}[./-](?:19|20)\d{2}|(?:19|20)\d{2}[./-]\d{1,2}[./-]\d{1,2})\b"),
    # long digit runs (national ID / SNS / record numbers): 9+ digits
    "long_id": re.compile(r"\b\d{9,}\b"),
}

# Keywords that, combined with the above, raise concern. (Lowercased match.)
SENSITIVE_HINTS = (
    "sns ", "n.º utente", "numero utente", "passport", "national id",
    "medical record", "mrn", "date of birth", "d.o.b", "дата рождения", "снилс", "паспорт",
)

# Files/dirs to skip (binary, vendored, or expected to contain example contacts).
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", "dist", "build"}
TEXT_EXTS = {".md", ".txt", ".yaml", ".yml", ".json", ".py", ".csv", ".tsv", ".html", ".js", ".ts"}

# Allowlist: synthetic test/example files are expected to contain pattern-like strings.
ALLOWLIST_SUBSTR = (
    "evals/public/",          # synthetic by design (still scanned, but emails there are fake examples)
    "assets/share-pack/",     # blank/synthetic templates — example dates are illustrative, not PHI
    "assets/state-templates/",
    "assets/letters/",        # placeholder skeletons + synthetic worked examples
)

# Keywords that mark a date as a likely date-of-birth (vs. ordinary metadata dates).
DOB_HINTS = ("date of birth", "d.o.b", "dob", "born ", "дата рождения", "д.р.")

# Lines that are clearly metadata, not personal data — skip date matches on these.
METADATA_LINE_RE = re.compile(
    r"^\s*(verified_at|review_due|date|last_updated|source_version|sourcedate|"
    r"next review|last checked|last reviewed|accessed)\b", re.I)

# The scanner's own source contains example patterns — don't scan it.
SELF_SKIP = ("scripts/phi_scan.py",)


def iter_files(paths):
    for p in paths:
        if os.path.isfile(p):
            yield p
        elif os.path.isdir(p):
            for root, dirs, files in os.walk(p):
                dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
                for f in files:
                    yield os.path.join(root, f)


def staged_files():
    try:
        out = subprocess.check_output(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
            text=True,
        )
    except Exception:
        return []
    return [f for f in out.splitlines() if f.strip()]


def scan_file(path):
    ext = os.path.splitext(path)[1].lower()
    if ext and ext not in TEXT_EXTS:
        return []
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as fh:
            text = fh.read()
    except OSError:
        return []
    lines = text.splitlines()
    low = text.lower()
    dob_hint = any(h in low for h in DOB_HINTS)
    sens_hint = any(h in low for h in SENSITIVE_HINTS)
    findings = []
    for label, rx in PATTERNS.items():
        for m in rx.finditer(text):
            line_no = text.count("\n", 0, m.start()) + 1
            line_text = lines[line_no - 1] if 0 <= line_no - 1 < len(lines) else ""
            if label == "dob":
                line_low = line_text.lower()
                on_line_dob = any(h in line_low for h in DOB_HINTS)
                # Ordinary metadata dates (verified_at, accessed, etc.) are not PHI —
                # but never skip a line that itself mentions a date of birth.
                if METADATA_LINE_RE.search(line_text) and not on_line_dob:
                    continue
                severity = "REVIEW" if (dob_hint or on_line_dob) else "WARN"
            elif label == "long_id":
                severity = "REVIEW" if sens_hint else "WARN"
            else:  # email, phone — strong signals on their own
                severity = "REVIEW"
            findings.append((label, line_no, m.group(0).strip(), severity))
    return findings


def main(argv=None):
    ap = argparse.ArgumentParser(description="Oncoskill PHI/PII pre-commit scan (v0).")
    ap.add_argument("paths", nargs="*", default=None, help="files/dirs to scan")
    ap.add_argument("--staged", action="store_true", help="scan only git-staged files")
    args = ap.parse_args(argv)

    if args.staged:
        targets = staged_files()
    else:
        targets = args.paths or ["."]

    any_hit = False
    for path in iter_files(targets):
        norm = path.replace(os.sep, "/")
        if any(s in norm for s in SELF_SKIP):
            continue
        # Any private path being scanned at all is itself a red flag if it would be committed.
        if "/private/" in norm or norm.startswith("private/") or "evals-private/" in norm:
            print(f"[BLOCK] private path should not be committed: {path}")
            any_hit = True
            continue
        allow = any(s in norm for s in ALLOWLIST_SUBSTR)
        for label, line, snippet, severity in scan_file(path):
            if allow and severity == "REVIEW":
                severity = "WARN"  # synthetic file — downgrade
            if severity == "REVIEW":
                any_hit = True
            print(f"[{severity}] {path}:{line}: possible {label}: {snippet!r}"
                  + (" (allowlisted synthetic file)" if allow else ""))

    if any_hit:
        print("\nphi_scan: candidates found — review before committing. "
              "If these are synthetic/intended, confirm and re-run or override your hook.")
        return 1
    print("phi_scan: no high-signal personal-data candidates found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
