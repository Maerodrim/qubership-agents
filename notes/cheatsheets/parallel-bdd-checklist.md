# Parallel BDD-development checklist (qubership-envgene)

Three groups of checks before committing or pushing changes under `cucumber_tests/`,
when several PRs/branches are moving in parallel. Every item is tied to a real incident
we already hit in `qubership-envgene` — this is not a theoretical list.

See also: [qubership-conventions.md](qubership-conventions.md) (commits and PRs),
[bdd-test-engineer.md](../../agents/bdd-test-engineer.md) (the agent role that should
run this checklist before handing off a result).

---

## 1. No duplicate or stale commits

Parallel branches almost always touch the same shared touch points. Before committing:

- [ ] **Shared dictionaries/registries are not duplicated.** `cucumber_tests/conftest.py::_XFAIL_REASONS` —
  the single most frequent conflict spot: during a merge/rebase both sides add their own key to
  the same dict. Resolve from the **commit's actual diff** (`git show <sha> -- conftest.py`), not
  from the `<<<<<<<`/`>>>>>>>` conflict markers — those show the parent's stale context, not what
  the commit actually changes.
- [ ] **A scenario ID is not already taken by another parallel branch.** `UC-<PREFIX>-<N>` must be
  unique within a feature. The `UC-CC-CP-4` collision (two independent branches added different
  scenarios under the same ID) was only caught by review, not by git — a text diff won't catch it
  when the scenarios land in different places in the file.
- [ ] **CI suite registration doesn't duplicate auto-discovery.** After `cucumber_tests/run_suites.sh`
  (auto-discovers `step_defs/test_*.py`), ANY hardcoded `pytest cucumber_tests/step_defs/test_X.py`
  step in `.github/workflows/perform_e2e_tests.yml` or `.github/actions/run-e2e-bdd/action.yml` is
  redundant and runs that suite twice. Check: `git diff origin/main -- .github` should be empty if
  the PR doesn't change the CI mechanism itself.
- [ ] **Test fixtures are not stale relative to current code.** Example: the step
  `"the environment AppDefs and RegDefs paths are resolved for the deploy"` was removed from
  `step_defs/` by one branch but stayed in the `.feature` file of another — a
  `StepDefinitionNotFoundError` instead of a meaningful failure. Before committing:
  `grep -rn "<step text>" cucumber_tests/` should find both the definition and every usage.
- [ ] **Dead fixture fields are removed**, not kept "just in case" (e.g. `override_key`, never
  read by any assertion).

## 2. Tests don't break the current green state

- [ ] **Full local run BEFORE pushing, not after.** CI is not the first check. Bring up Docker
  (`docker compose -f devtools/docker-compose.yml up -d --build cucumber`), run
  `bash cucumber_tests/run_suites.sh` in full, not just the suite you changed.
- [ ] **All 10 suites stay green**, not only the one you edited. One shared file
  (`conftest.py`, a template under `mock_nexus/`) can break suites that look unrelated to the PR.
- [ ] **Re-run after a rebase/merge**, even when the local diff "obviously looks safe". Merging
  main may have shifted a dependency version (example: Alpine moved `python3-dev`, the image build
  broke without a single line changed in the tests).
- [ ] **No side-effect files in the commit.** A local `run_suites.sh` run leaves `reports/`,
  `e2e_tests.log`, and sometimes `deploy-plan.yaml` (a test-isolation leak — something writes the
  deploy plan into `CI_PROJECT_DIR` instead of a tmp workspace) at the repo root. `git status`
  before committing should be clean of untracked junk.
- [ ] **Compare test counts before/after**, not just pass/fail. A scenario silently lost during a
  feature-file refactor (e.g. splitting it into separate files) won't fail the run — it just
  shrinks the test count. `pytest --collect-only | wc -l` before and after should match
  expectations.

## 3. Per-case check: enabled-ness and adequacy

### Enabled-ness — the scenario actually runs, not silently skipped

- [ ] **The scenario is collected by pytest-bdd.** `pytest cucumber_tests/step_defs/ --collect-only -q`
  should show this exact `UC-*`. A missing `test_<feature>.py` runner is the most common cause of
  a silent skip: pytest-bdd doesn't complain, it just never sees the scenarios.
- [ ] **The suite is in the actual CI list**, not only in a local `run_suites.sh`. Five of ten
  suites (`external_creds`, `clean_sub_flows`, `credential_rotation`, `resource_profiles`,
  `mixed_flows`) never ran in PR CI until the hardcoded list was replaced with auto-discovery —
  bugs in them had accumulated unnoticed for months.
- [ ] **The `@xfail_*` tag is defined** in `_XFAIL_REASONS` — otherwise the scenario either fails
  with a `KeyError`, or (worse) silently isn't marked xfail and masks a real regression. Check
  with a script (`ast.parse` plus a tag-set diff), not by eye.
- [ ] **The step actually prints both streams on failure.** `assert_success` in
  `cucumber_tests/framework/workspace.py` historically surfaced only `stderr` — a Java-CLI
  (Quarkus, writes to `stdout`) error never made it into the report at all, and a failure looked
  like "exit code 1" with no reason given.

### Adequacy — the scenario verifies what it claims to

- [ ] **The oracle is not a tautology.** Ask: "if the code did nothing, would the test still
  pass?" A plain check that a file exists that already existed BEFORE the pipeline ran is not an
  oracle.
- [ ] **The negative scenario fails at the claimed point.** `UC-EC-D-8` was labeled "checks
  rejection on mixed credentials" but actually failed on a `FileNotFoundError` in `process_sd.py`
  long before the credential validator — the check proved nothing about credential mixing until
  the fixture was given the needed `appdefs`/`regdefs`.
- [ ] **The xfail-reason text points at the real code path.** The Java message
  `"sub component 'null' of service:svc1"` blamed a sub-component that doesn't exist — the real
  cause was a property read off the service itself (the `entity` variable is reused inside a loop
  and keeps the last iteration's value after it). Don't copy an error message into an xfail-reason
  without reading the code that prints it.
- [ ] **No self-blessing.** A test is not validated by the same code/fixture the PR just changed
  in a neighboring file of the same commit.
- [ ] **Data has discriminating power.** Two scenarios (replace/merge, baseline A/B) must not pass
  on the same input data — if they did, that would prove nothing about the difference between the
  modes.

---

## Quick "run everything" command

```bash
export MSYS_NO_PATHCONV=1 MSYS2_ARG_CONV_EXCL='*'   # otherwise Git Bash on Windows mangles /workspace/...
docker compose -f devtools/docker-compose.yml exec -T cucumber \
  bash /workspace/cucumber_tests/run_suites.sh
```

If it fails, check `Stdout:` in the failure text, not just `Stderr:`.
