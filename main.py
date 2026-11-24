"""Developer excuse entry for make.fun bounty
u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3 (variant B).

Writes exactly one line to /output/entry.txt. Never writes to the repo
root: the grader sandbox mounts the repo read-only.
"""

import os
import sys

LINE = "The tests passed, so I shipped the bug to production and now it reviews my pull requests, rejects my fixes, and pages me at 3am."

# Concept iteration log (family: CI-PASSED / GIT-BLAME — a named artifact
# applied to the wrong target, with the human inverted):
# v1: "CI was green, so I deployed the bug to production and now it approves
#     my pull requests." — DROPPED: inversion is there but "approves" is flat,
#     and at 89 chars it wastes the budget.
# v2: "The tests all passed, so I deployed the bug to production and now it
#     reviews my pull requests." — KEPT direction: "reviews" is a stronger,
#     more dev-true verb than "approves", but still only 96 chars.
# v3: "The tests passed, so I shipped the bug to production and now it
#     reviews my pull requests and rejects my fixes." — KEPT: "rejects my
#     fixes" adds the sting, but the line still ends before the inversion
#     peaks.
# v4: "The tests passed, so I shipped the bug to production, and git blame
#     now says I wrote it." — DROPPED: the git-blame twist lands flat on its
#     own; naming me as author is blame, not a reversal of power.
# v5: "The tests passed, so I shipped the bug to production and now it
#     reviews my code, rejects my fixes, and pages me at 3am." — KEPT:
#     the triple escalation (reviews -> rejects -> pages) completes the
#     inversion, but "reviews my code" is vaguer than "pull requests".
# v6: "The tests passed, so I shipped the bug to production and now it
#     reviews my pull requests, rejects my fixes, and pages me at 3am."
#     — KEPT: specific artifact (pull requests), full arc, 128 chars.
# v7: "CI went green, so I shipped the bug to production and now it reviews
#     my pull requests, rejects my fixes, and pages me at 3am." — DROPPED:
#     "CI went green" is punchier jargon, but "The tests passed" is the
#     excuse a developer actually says out loud when prod breaks.
# v8: identical to v6 — SHIPPED. The spoken-excuse opening plus the
#     three-step inversion (it reviews me, it rejects me, it pages me)
#     is the strongest version of this concept.


def main() -> int:
    if not (1 <= len(LINE) <= 200):
        print(f"error: line is {len(LINE)} chars, must be 1-200", file=sys.stderr)
        return 1
    if LINE != LINE.strip() or "\n" in LINE or "\r" in LINE:
        print("error: line must be a single line with no surrounding whitespace",
              file=sys.stderr)
        return 1
    if "  " in LINE:
        print("error: double space in line", file=sys.stderr)
        return 1
    if not LINE.endswith("."):
        print("error: line must end with a full stop", file=sys.stderr)
        return 1
    try:
        data = LINE.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"error: line is not valid UTF-8: {exc}", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as fh:
        fh.write(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
