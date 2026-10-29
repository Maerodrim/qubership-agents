"""Cross-references docs/use-cases/*.md (headings "## UC-<ID>: <title>") against BDD scenarios
in cucumber_tests/features/*.feature ("Scenario: UC-<ID>: <title>") in the qubership-envgene repo.

Usage (stdlib only, no dependencies):
    python test-documentation-matrix.py [<git-ref>] [<path-to-qubership-envgene>]

Defaults: <git-ref> = origin/main; the path defaults to a sibling qubership-envgene folder
(if qubership-agents and qubership-envgene sit next to each other, as on the author's machine).

Prints JSON with two lists:
- rows: for each docs/use-cases/<doc>.md — how many UCs, how many are test-covered, which
  <.feature> files cover them, which ids are missing.
- orphans: for each cucumber_tests/features/<name>.feature — scenarios whose UC-id has no
  matching "## UC-<ID>:" heading anywhere in docs/use-cases.

The number tables in the sibling note (test-documentation-matrix.md) can be recomputed with
this script, but the hand-written notes (e.g. the UC-09 vs UC-06 duplicate in cloud-passport)
and the note's own structure are not touched by it — that's a manual, judgment-based edit, not
autogeneration.
"""
import json
import os
import re
import subprocess
import sys

UC_ID = r"UC-(?:[A-Z0-9]+-)*\d+[a-z]?"
UC_RE = re.compile(r"^#{2,4}\s+(" + UC_ID + r")\s*:\s*(.*)$", re.M)
SC_RE = re.compile(r"^\s*Scenario(?: Outline)?:\s*(" + UC_ID + r")\s*:\s*(.*)$", re.M)


def default_repo_path() -> str:
    here = os.path.dirname(os.path.abspath(__file__))
    # notes/architecture/ -> notes/ -> qubership-agents/ -> siblings dir -> qubership-envgene/
    return os.path.normpath(os.path.join(here, "..", "..", "..", "qubership-envgene"))


def git(repo: str, *args: str) -> str:
    result = subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True, encoding="utf-8")
    if result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {result.stderr}")
    return result.stdout


def ls(repo: str, ref: str, path: str) -> list[str]:
    return [p for p in git(repo, "ls-tree", "--name-only", ref, path).splitlines() if p]


def show(repo: str, ref: str, path: str) -> str:
    return git(repo, "show", f"{ref}:{path}")


def main() -> None:
    ref = sys.argv[1] if len(sys.argv) > 1 else "origin/main"
    repo = sys.argv[2] if len(sys.argv) > 2 else default_repo_path()
    if not os.path.isdir(os.path.join(repo, ".git")):
        raise SystemExit(f"Not a git repository: {repo}")

    docs: dict[str, dict[str, str]] = {}
    for p in ls(repo, ref, "docs/use-cases/"):
        if p.endswith("README.md"):
            continue
        name = p.split("/")[-1][:-3]
        txt = show(repo, ref, p)
        docs[name] = {m.group(1): m.group(2).strip() for m in UC_RE.finditer(txt)}

    feature_doc_files = {p.split("/")[-1][:-3] for p in ls(repo, ref, "docs/features/") if not p.endswith("README.md")}

    feats: dict[str, set[str]] = {}
    feat_titles: dict[str, dict[str, str]] = {}
    for p in ls(repo, ref, "cucumber_tests/features/"):
        name = p.split("/")[-1][:-8]
        txt = show(repo, ref, p)
        matches = list(SC_RE.finditer(txt))
        feats[name] = {m.group(1) for m in matches}
        feat_titles[name] = {m.group(1): m.group(2).strip() for m in matches}

    all_tested_ids = {i for ids in feats.values() for i in ids}

    rows = []
    for doc_name, ucs in sorted(docs.items()):
        if not ucs:
            continue
        missing = [i for i in ucs if i not in all_tested_ids]
        covering_files = sorted({fn for fn, ids in feats.items() if ids & set(ucs)})
        rows.append({
            "doc": doc_name,
            "total": len(ucs),
            "covered": len(ucs) - len(missing),
            "missing": [{"id": i, "title": ucs[i]} for i in missing],
            "feature_files": covering_files,
            "has_feature_doc": doc_name in feature_doc_files,
        })

    doc_ids = {i for ucs in docs.values() for i in ucs}
    orphans = {}
    for fn, ids in feats.items():
        extra = sorted(i for i in ids if i not in doc_ids)
        if extra:
            orphans[fn] = [{"id": i, "title": feat_titles[fn].get(i, "")} for i in extra]

    print(json.dumps({"ref": ref, "rows": rows, "orphans": orphans}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
