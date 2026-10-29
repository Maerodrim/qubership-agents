# Test & documentation matrix (qubership-envgene)

Cross-references the use-case catalog in `docs/use-cases/*.md` (headings `## UC-<ID>: <title>`) against BDD-test scenarios in `cucumber_tests/features/*.feature` (`Scenario: UC-<ID>: <title>`). Built automatically from `origin/main` at generation time — see [How to regenerate](#how-to-regenerate) at the end of this file; the numbers are only good until the next PR that touches `docs/use-cases/` or `cucumber_tests/features/`.

Two directions of mismatch the matrix catches:
- **Documented, not tested** — the "Partially covered" and "Not covered at all" sections.
- **Tested, but no matching UC in the docs** — the ["Code ahead of documentation"](#code-ahead-of-documentation) section: either the scenario deserves a doc entry, or this is a different numbering scheme and the cross-reference is a false positive (see the `bdd-test-review` skill under `qubership-envgene/.claude/skills/` — it asks exactly this same first question before any verdict).

## Coverage summary by area

| Area (`docs/use-cases/`) | UC total | Covered | `.feature` exists | `docs/features/` pair exists |
|---|---|---|---|---|
| `app-reg-defs.md` | 10 | 0 | — | yes |
| `artifact-downloading.md` | 32 | 0 | — | no |
| `auto-environment-name.md` | 5 | 0 | — | no |
| `blue-green-deployment.md` | 9 | 0 | — | yes |
| `calculator-cli.md` | 21 | 18 | `calculator-cli.feature` | yes |
| `cloud-passport.md` | 9 | 0 | — | no |
| `cloud-passport-discovery.md` | 4 | 0 | — | no |
| `cmdb-import.md` | 4 | 0 | — | no |
| `credential-rotation.md` | 10 | 8 | `credential-rotation.feature` | no |
| `envgene-null-value-validation.md` | 4 | 0 | — | no |
| `environment-instance-generation.md` | 16 | 0 | — | yes |
| `environment-inventory-generation.md` | 16 | 15 | `environment-inventory-generation.feature` | no |
| `gsf-repository-maintenance.md` | 6 | 0 | — | no |
| `registry-discovery.md` | 6 | 0 | — | no |
| `resource-profiles.md` | 16 | 4 | `resource-profiles.feature` | no |
| `sbom-retention.md` | 7 | 7 | `sbom-retention.feature` | yes |
| `sbom-storage-migration.md` | 1 | 0 | — | no |
| `sd-processing.md` | 36 | 0 | — | yes |
| `system-certificate.md` | 9 | 0 | — | yes |
| `template-inheritance.md` | 5 | 0 | — | no |
| `template-version-update.md` | 2 | 0 | — | no |
| `cloud-passport.md` *(PR #1791, not in main)* | 9 | 7 | `cloud-passport.feature` | no |

**Total:** 59 of 237 documented UCs are covered by a BDD scenario (including 7 of 9 in the not-yet-merged PR #1791).

## Partially covered — concrete backlog

Test infrastructure for the area already exists, specific scenarios are missing:

### `calculator-cli.md` — 18/21

- [ ] **UC-CC-CG-1** — Cleanup context for every namespace in No-CMDB v1 deploy
- [ ] **UC-CC-CG-2** — No cleanup context in No-CMDB v2 deploy
- [ ] **UC-CC-CG-3** — No cleanup context in No-CMDB v2 clean

### `credential-rotation.md` — 8/10

- [ ] **UC-CR-ENC-2** — Update Credentials with Encrypted Payload when Encryption Is Enabled
- [ ] **UC-CR-ENC-4** — Update Credentials with Encrypted Payload when Encryption Is Disabled

### `environment-inventory-generation.md` — 15/16

- [ ] **UC-EINV-AT-ALL-1** — Fail without committing changes if any operation fails (negative)

### `resource-profiles.md` — 4/16

- [ ] **UC-RP-SS-1** — Namespace is the active side when an override is present
- [ ] **UC-RP-SS-2** — Namespace is the active side when the namespace object baseline is set
- [ ] **UC-RP-BR-1** — Override baseline takes precedence over the object baseline
- [ ] **UC-RP-BR-2** — Object baseline is used when the override carries no baseline
- [ ] **UC-RP-BR-3** — Empty string baseline is treated as absent
- [ ] **UC-RP-BR-4** — Baseline-only override selects a baseline with no custom values
- [ ] **UC-RP-AB-1** — Override is always applied and custom values win over the baseline when the name matches
- [ ] **UC-RP-AB-2** — Service with no baselines receives the custom values only
- [ ] **UC-RP-AB-3** — Baseline name mismatch on a service that has baselines emits a warning
- [ ] **UC-RP-AB-4** — Override with custom values and no baseline emits a warning
- [ ] **UC-RP-ES-4** — Merge mode with the same baseline combines both overrides
- [ ] **UC-RP-LR-1** — A referenced override name resolves to the most specific scope

### `cloud-passport.md` — 7/9 *(in PR #1791)*

- [ ] **UC-05** — Parameter source traceability
- [ ] **UC-09** — Backward compatibility for existing business environments — bdd-test-review on PR #1791 found this to be a byte-for-byte duplicate of UC-06 and dropped the scenario; the doc entry itself should either be removed too or explicitly point at UC-06 (not silently left as-is).

## Not covered at all

16 areas, 158 UCs total — not a single BDD scenario. The full list is in a collapsible block per area; the table above is just counts for scanning.

| Area | UCs | `docs/features/` pair |
|---|---|---|
| `app-reg-defs.md` | 10 | yes |
| `artifact-downloading.md` | 32 | no |
| `auto-environment-name.md` | 5 | no |
| `blue-green-deployment.md` | 9 | yes |
| `cloud-passport.md` | 9 | no |
| `cloud-passport-discovery.md` | 4 | no |
| `cmdb-import.md` | 4 | no |
| `envgene-null-value-validation.md` | 4 | no |
| `environment-instance-generation.md` | 16 | yes |
| `gsf-repository-maintenance.md` | 6 | no |
| `registry-discovery.md` | 6 | no |
| `sbom-storage-migration.md` | 1 | no |
| `sd-processing.md` | 36 | yes |
| `system-certificate.md` | 9 | yes |
| `template-inheritance.md` | 5 | no |
| `template-version-update.md` | 2 | no |

<details>
<summary><code>app-reg-defs.md</code> — 10 UCs, none covered</summary>

- UC-ARD-TR-1 — Basic AppDef/RegDef template rendering
- UC-ARD-TR-2 — Basic AppDef/RegDef template delete
- UC-ARD-TR-3 — Shared template repository, off-site instance rendering
- UC-ARD-TR-4 — Shared template repository, on-site instance rendering
- UC-ARD-DO-1 — Replace template-rendered definition with definition override
- UC-ARD-DO-2 — Delete definition override
- UC-ARD-DO-3 — Add new definition via definition override with no matching template
- UC-ARD-PM-1 — Root mode behavior (auto-migration from legacy layout)
- UC-ARD-PM-2 — Dual mode behavior (upgrade with no cleanup)
- UC-ARD-CI-1 — Export definitions to CMDB

</details>

<details>
<summary><code>artifact-downloading.md</code> — 32 UCs, none covered</summary>

- UC-AD-SD-1 — Download SD from Artifactory with User/Password (AppDef v1 + RegDef v1)
- UC-AD-SD-2 — Download SD from Artifactory with Anonymous Access (AppDef v1 + RegDef v1)
- UC-AD-SD-3 — Download SD from Nexus with User/Password (AppDef v1 + RegDef v1)
- UC-AD-SD-4 — Download SD from Nexus with Anonymous Access (AppDef v1 + RegDef v1)
- UC-AD-SD-5 — Download SD from Artifactory with User/Password (AppDef v1 + RegDef v2)
- UC-AD-SD-6 — Download SD from Artifactory with Anonymous Access (AppDef v1 + RegDef v2)
- UC-AD-SD-7 — Download SD from Nexus with User/Password (AppDef v1 + RegDef v2)
- UC-AD-SD-8 — Download SD from Nexus with Anonymous Access (AppDef v1 + RegDef v2)
- UC-AD-SD-9 — Download SD from AWS CodeArtifact with Secret (AppDef v1 + RegDef v2)
- UC-AD-SD-10 — Download SD from GCP Artifact Registry with Service Account (AppDef v1 + RegDef v2)
- UC-AD-SD-11 — Download Specific Version SD
- UC-AD-ENV-9 — Download Template from Artifactory with GAV notation
- UC-AD-ENV-10 — Download Template from Artifactory with GAV notation and Anonymous Access
- UC-AD-ENV-11 — Download Template from Nexus with GAV notation
- UC-SC-NEX-1 — Download template artifact from Nexus with custom CA certificate
- UC-AD-ENV-12 — Download Template from Nexus with GAV notation and Anonymous Access
- UC-AD-ENV-13 — Download Template with app ver notation from Artifactory (ArtDef v1)
- UC-AD-ENV-14 — Download Template with app ver notation from Artifactory and Anonymous Access (ArtDef v1)
- UC-AD-ENV-15 — Download Template with app ver notation from Nexus (ArtDef v1)
- UC-AD-ENV-16 — Download Template with app ver notation from Nexus and Anonymous Access (ArtDef v1)
- UC-AD-ENV-17 — Download Template from Artifactory with app ver notation (ArtDef v2)
- UC-AD-ENV-18 — Download Template from Artifactory with app ver notation and Anonymous Access (ArtDef v2)
- UC-AD-ENV-19 — Download Template from Nexus with app ver notation (ArtDef v2)
- UC-AD-ENV-20 — Download Template from Nexus with app ver notation and Anonymous Access (ArtDef v2)
- UC-AD-ENV-21 — Download Template from AWS CodeArtifact with app ver notation (ArtDef v2)
- UC-AD-ENV-22 — Download Template from GCP Artifact Registry with app ver notation (ArtDef v2)
- UC-AD-ENV-23 — Download SNAPSHOT Template Version
- UC-AD-ENV-24 — Download Specific Template Version
- UC-AD-ERR-1 — Handle Missing Application Definition
- UC-AD-ERR-2 — Handle Missing Registry Definition
- UC-AD-ERR-3 — Handle Authentication Failure
- UC-AD-ERR-4 — Handle Missing Artifact Definition

</details>

<details>
<summary><code>auto-environment-name.md</code> — 5 UCs, none covered</summary>

- UC-AEN-END-1 — Environment with no explicit environmentName defined
- UC-AEN-END-2 — Environment with explicit environmentName defined
- UC-AEN-END-3 — Environment with explicit environmentName different from folder name
- UC-AEN-END-4 — Invalid folder structure for environment
- UC-AEN-END-5 — Template rendering with derived environment name

</details>

<details>
<summary><code>blue-green-deployment.md</code> — 9 UCs, none covered</summary>

- UC-BG-1 — Init Domain
- UC-BG-2 — Warmup
- UC-BG-3 — Promote
- UC-BG-4 — Commit
- UC-BG-5 — Rollback
- UC-BG-6 — Reverse Warmup
- UC-BG-7 — Reverse Promote
- UC-BG-8 — Reverse Commit
- UC-BG-9 — Reverse Rollback

</details>

<details>
<summary><code>cloud-passport.md</code> — 9 UCs, none covered</summary>

- UC-01 — Environment inherits cluster Cloud Passport automatically
- UC-02 — Environment uses explicitly named Cloud Passport
- UC-03 — Environment builds without Cloud Passport
- UC-04 — Environment uses passport from custom location
- UC-05 — Parameter source traceability
- UC-06 — Business environments auto-associate the business passport in a mixed cluster
- UC-07 — Infra environments use an explicit infra passport in a mixed cluster
- UC-08 — Mixed cluster failure when infra relies on auto-association
- UC-09 — Backward compatibility for existing business environments

</details>

<details>
<summary><code>cloud-passport-discovery.md</code> — 4 UCs, none covered</summary>

- UC-CPD-1 — Cloud Passport discovered from Discovery pipeline
- UC-CPD-2 — Passport jobs skipped and env_builder fails
- UC-CPD-3 — Pipeline generation fails when integration is missing
- UC-CPD-4 — Pipeline generation fails when GET_PASSPORT and CRED_ROTATION_PAYLOAD are both set

</details>

<details>
<summary><code>cmdb-import.md</code> — 4 UCs, none covered</summary>

- UC-CMDB-1 — CMDB import with create
- UC-CMDB-2 — CMDB import with do_not_create
- UC-CMDB-3 — CMDB import with validate_only
- UC-CMDB-4 — Placeholder credentials pass validation

</details>

<details>
<summary><code>envgene-null-value-validation.md</code> — 4 UCs, none covered</summary>

- UC-NVV-1 — Unresolved parameter blocks pipeline
- UC-NVV-2 — Unresolved credential blocks pipeline
- UC-NVV-3 — All values resolved
- UC-NVV-4 — Multiple unresolved values reported together

</details>

<details>
<summary><code>environment-instance-generation.md</code> — 16 UCs, none covered</summary>

- UC-EIG-NF-1 — Namespace NOT in BG Domain with deploy_postfix
- UC-EIG-NF-2 — Namespace NOT in BG Domain without deploy_postfix
- UC-EIG-NF-3 — Controller Namespace in BG Domain with deploy_postfix
- UC-EIG-NF-4 — Controller Namespace in BG Domain without deploy_postfix
- UC-EIG-NF-5 — Origin Namespace in BG Domain with deploy_postfix
- UC-EIG-NF-6 — Origin Namespace in BG Domain without deploy_postfix
- UC-EIG-NF-7 — Peer Namespace in BG Domain with deploy_postfix
- UC-EIG-NF-8 — Peer Namespace in BG Domain without deploy_postfix
- UC-EIG-TA-1 — Environment Instance Generation with `artifact` only
- UC-EIG-TA-2 — Environment Instance Generation with `artifact` and `bgNsArtifacts` and BG Domain
- UC-EIG-TA-3 — Environment Instance Generation with `artifact` and `bgNsArtifacts` and without BG Domain
- UC-EIG-ES-1 — Generate Effective Set without `SD_DATA` or `SD_VERSION`
- UC-EIG-ES-2 — Generate Effective Set with `SD_DATA` or `SD_VERSION`
- UC-EIG-ES-3 — Apply `CUSTOM_PARAMS` when `GENERATE_EFFECTIVE_SET` is true
- UC-EIG-ES-4 — Ignore `CUSTOM_PARAMS` when `GENERATE_EFFECTIVE_SET` is false
- UC-EIG-ME-1 — Parallel Environment Instance Generation for Multiple Environments

</details>

<details>
<summary><code>gsf-repository-maintenance.md</code> — 6 UCs, none covered</summary>

- UC-GSF-TMP-1 — Initialize Template Repository via GSF
- UC-GSF-TMP-2 — Upgrade Template Repository via GSF
- UC-GSF-TMP-3 — Downgrade Template Repository via GSF
- UC-GSF-INST-1 — Initialize Instance Repository via GSF
- UC-GSF-INST-2 — Upgrade Instance Repository via GSF
- UC-GSF-INST-3 — Downgrade Instance Repository via GSF

</details>

<details>
<summary><code>registry-discovery.md</code> — 6 UCs, none covered</summary>

- UC-RD-1 — Artifact Definition discovered from CMDB
- UC-RD-2 — registry_discovery job is not added to pipeline
- UC-RD-3 — Discovery forced when local definition exists
- UC-RD-4 — Pipeline generation fails when discovery disabled
- UC-RD-5 — Job runs but runtime discovery is skipped (invalid AppVer)
- UC-RD-6 — CMDB export failure during discovery

</details>

<details>
<summary><code>sbom-storage-migration.md</code> — 1 UC, none covered</summary>

- UC-SBOM-MIG-1 — First run after upgrade

</details>

<details>
<summary><code>sd-processing.md</code> — 36 UCs, none covered</summary>

- UC-SD-1 — Single SD_VERSION with `replace` mode
- UC-SD-2 — Single SD_VERSION with `extended-merge` mode
- UC-SD-2a — Single SD_VERSION with `extended-merge` mode when Full SD does not exist
- UC-SD-3 — Single SD_VERSION with `basic-merge` mode
- UC-SD-3a — Single SD_VERSION with `basic-merge` mode when Full SD does not exist
- UC-SD-4 — Single SD_VERSION with `basic-exclusion-merge` mode
- UC-SD-4a — Single SD_VERSION with `basic-exclusion-merge` mode when Full SD does not exist
- UC-SD-5 — Multiple SD_VERSION with `basic-merge` mode
- UC-SD-5a — Multiple SD_VERSION with `basic-merge` mode when Full SD does not exist
- UC-SD-6 — Multiple SD_VERSION with `basic-exclusion-merge` mode
- UC-SD-6a — Multiple SD_VERSION with `basic-exclusion-merge` mode when Full SD does not exist
- UC-SD-7 — Multiple SD_VERSION with `extended-merge` mode
- UC-SD-7a — Multiple SD_VERSION with `extended-merge` mode when Full SD does not exist
- UC-SD-8 — Multiple SD_VERSION with `replace` mode
- UC-SD-9 — Single SD_VERSION with SD_DELTA=true
- UC-SD-9a — Single SD_VERSION with SD_DELTA=true when Full SD does not exist
- UC-SD-10 — Single SD_VERSION with SD_DELTA=false
- UC-SD-11 — Single SD_DATA with `replace` mode
- UC-SD-12 — Single SD_DATA with `extended-merge` mode
- UC-SD-12a — Single SD_DATA with `extended-merge` mode when Full SD does not exist
- UC-SD-13 — Single SD_DATA with `basic-merge` mode
- UC-SD-13a — Single SD_DATA with `basic-merge` mode when Full SD does not exist
- UC-SD-14 — Single SD_DATA with `basic-exclusion-merge` mode
- UC-SD-14a — Single SD_DATA with `basic-exclusion-merge` mode when Full SD does not exist
- UC-SD-15 — Multiple SD_DATA with `basic-merge` mode
- UC-SD-15a — Multiple SD_DATA with `basic-merge` mode when Full SD does not exist
- UC-SD-16 — Multiple SD_DATA with `basic-exclusion-merge` mode
- UC-SD-16a — Multiple SD_DATA with `basic-exclusion-merge` mode when Full SD does not exist
- UC-SD-17 — Multiple SD_DATA with `extended-merge` mode
- UC-SD-17a — Multiple SD_DATA with `extended-merge` mode when Full SD does not exist
- UC-SD-18 — Multiple SD_DATA with `replace` mode
- UC-SD-19 — Single SD_DATA with SD_DELTA=true
- UC-SD-19a — Single SD_DATA with SD_DELTA=true when Full SD does not exist
- UC-SD-20 — Single SD_DATA with SD_DELTA=false
- UC-SD-21 — Input SD contains duplicate application entries
- UC-SD-22 — Existing sd.yaml contains duplicate application entries

</details>

<details>
<summary><code>system-certificate.md</code> — 9 UCs, none covered</summary>

- UC-SC-SRC-1 — Load and merge certificates from configured sources
- UC-SC-SRC-2 — Load default certificate when configured sources are empty
- UC-SC-MRG-1 — One source valid and one source invalid
- UC-SC-MRG-2 — Duplicate certificates from different sources
- UC-SC-VAL-1 — Invalid CI/CD bundle fails pipeline
- UC-SC-VAL-2 — Unreadable certificate file in folder fails pipeline
- UC-SC-VAL-3 — Invalid certificate files in folder fail pipeline
- UC-SC-VAL-4 — File with valid and invalid PEM blocks
- UC-SC-USG-1 — Template download from Artifactory with system certificates

</details>

<details>
<summary><code>template-inheritance.md</code> — 5 UCs, none covered</summary>

- UC-TI-PT-1 — Build child template using a single parent template
- UC-TI-PT-2 — Build child template composed from multiple parent templates
- UC-TI-CS-1 — Use explicit `composite_structure` from child Template Descriptor
- UC-TI-OV-1 — Override parent parameters for Cloud template
- UC-TI-OV-2 — Override parent parameters for Namespace template

</details>

<details>
<summary><code>template-version-update.md</code> — 2 UCs, none covered</summary>

- UC-TV-1 — Apply `ENV_TEMPLATE_VERSION` in `PERSISTENT` mode
- UC-TV-2 — Apply `ENV_TEMPLATE_VERSION` in `TEMPORARY` mode

</details>

## Code ahead of documentation

Scenarios whose title carries a `UC-<ID>` with no matching `## UC-<ID>:` heading anywhere in `docs/use-cases/`. Not necessarily a bug — the ID may simply belong to a different numbering scheme (e.g. `external-creds.feature` references `UC-EC-*`, but the repository has no separate `docs/use-cases/external-creds.md`, only a `docs/features/external-creds.md` with no UC numbering). Still, each batch deserves a one-time human decision — add the UC to the docs, or leave it as is — i.e. resolve it **with the user**, not silently.

<details>
<summary><code>calculator-cli.feature</code> — 32 scenarios with no doc UC</summary>

- UC-CC-AV-1 — App Chart Validation Enabled Fails When Chart Component Absent
- UC-CC-AV-2 — App Chart Validation Disabled Skips Chart Check
- UC-CC-CO-1 — Service-Named deployParameter Moved to Collision File
- UC-CC-CP-1 — CUSTOM_PARAMS Injected into Deployment Parameters
- UC-CC-CP-2 — CUSTOM_PARAMS with Unknown Namespace Fails
- UC-CC-CP-3 — CUSTOM_PARAMS with Mixed Top-Level and Namespace Keys Fails
- UC-CC-CP-4 — CUSTOM_PARAMS deployment override decomposes into root, global, and per-service
- UC-CC-CP-5 — CUSTOM_PARAMS deployment key matching a service name goes to collision-credentials.yaml
- UC-CC-CP-6 — CUSTOM_PARAMS Overrides Existing Namespace Parameter
- UC-CC-CP-7 — CUSTOM_PARAMS Injected into Runtime Context
- UC-CC-CP-8 — Namespace-Scoped CUSTOM_PARAMS Injected into Target Namespace
- UC-CC-DP-5 — BG Domain deployPostfix Peer Match
- UC-CC-DP-6 — Multiple Unmatched deployPostfix Values Fail The Same Way As A Single One
- UC-CC-EP-1 — DEPLOYMENT_SESSION_ID Injected into Deployment Parameters
- UC-CC-GI-1 — UniqForRun Application Gets Unique Generation Directory
- UC-CC-GI-2 — UniqForVersion Application Gets Version-Derived Generation Directory
- UC-CC-IM-1 — deploy_param Yields Image Parameter
- UC-CC-MR-3 — Multi-Step Macro Chain Resolution
- UC-CC-MR-4 — Macro Reference Resolved Across Hierarchy Levels
- UC-CC-NS-1 — No SBOMs Mode Generates Only Pipeline And Topology Contexts
- UC-CC-PD-1 — MANAGED_BY Defaults to argocd
- UC-CC-PM-1 — Namespace Parameter Overrides Cloud Parameter
- UC-CC-PM-2 — Cloud Parameter Overrides Tenant Parameter
- UC-CC-PM-3 — Namespace Parameter Overrides Tenant Parameter Directly
- UC-CC-PM-4 — Application Parameter Overrides Namespace Parameter
- UC-CC-SC-1 — creds.get Parameter Splits into Credentials File
- UC-CC-SC-2 — Nested Structure Splits Only Sensitive Subfields
- UC-CC-SO-1 — DEPLOYMENT_SESSION_ID Identical Across All Effective Set Files
- UC-CC-SO-2 — Deployment Parameters Are Sorted Alphabetically
- UC-CC-TP-1 — Composite Baseline-Only Topology Injects Baseline Namespace Parameters
- UC-CC-TP-2 — Composite With Satellites Injects Baseline References
- UC-CC-TP-3 — Blue-Green Domain In A Satellite Injects Per-Namespace Parameters

</details>

<details>
<summary><code>credential-rotation.feature</code> — 7 scenarios with no doc UC</summary>

- UC-CR-LCH-3 — Update shared credential file linked through Shared Credentials
- UC-CR-LCH-4 — Report affected parameter located in another environment under the same cluster
- UC-CR-TPR-4 — Rotate a secret credential field in force mode
- UC-CR-VAL-2 — Single invalid rotation_item fails the whole job and preserves state
- UC-CR-VAL-3 — Reject application specified together with pipeline context
- UC-CR-VAL-4 — Reject GET_PASSPORT combined with CRED_ROTATION_PAYLOAD
- UC-CR-VAL-5 — Fail when CRED_ROTATION_PAYLOAD contains invalid namespace

</details>

<details>
<summary><code>environment-inventory-generation.feature</code> — 8 scenarios with no doc UC</summary>

- UC-EINV-AT-ALL-2 — Rollback on invalid ENV_INVENTORY_CONTENT (schema validation failure)
- UC-EINV-AT-ALL-3 — Failed run does not reach git_commit
- UC-EINV-BASIC-1 — Generate minimal Environment Inventory (init)
- UC-EINV-CR-4 — Create credentials file at "<place>" scope
- UC-EINV-MULTI-1 — Apply combined payload with multiple object types in one run
- UC-EINV-PS-4 — Create paramset file at "<place>" scope
- UC-EINV-RP-4 — Create resource profile file at "<place>" scope
- UC-EINV-STV-4 — Create Shared Template Variable file at "<place>" scope

</details>

<details>
<summary><code>external-creds.feature</code> — 27 scenarios with no doc UC</summary>

- UC-EC-CTX-1 — Vault single-value create:true credential emits create_if_absent context entry with value field
- UC-EC-CTX-2 — Vault multi-field create:true credential emits create_if_absent context entry with property fields
- UC-EC-CTX-3 — create:false credential emits fail_if_absent context entry without data
- UC-EC-CTX-4 — GCP single-value create:true credential emits create_if_absent context entry with scalar data
- UC-EC-CTX-5 — Local-only environment produces no external credential context file
- UC-EC-CTX-6 — An Environment Instance with EXTERNAL_CREDENTIAL_PROVISIONING set to skip bypasses the provisioning CLI call
- UC-EC-D-1 — helm-values multi-field credential emits VALS references with property fragments
- UC-EC-D-10 — Credential referencing undefined secret store fails ES generation
- UC-EC-D-11 — helm-values multi-field credential emits openbao VALS references with property fragments
- UC-EC-D-1b — Legacy effective-set run emits VALS references
- UC-EC-D-2 — helm-values single-value vault credential emits a VALS reference with #/value
- UC-EC-D-3 — external-values multi-field credential emits an ESO reference object with secretKeys
- UC-EC-D-4 — external-values single-value credential emits an ESO reference object with no secretKeys
- UC-EC-D-5 — Mixed SECRET_FLOW shapes produce both VALS and ESO references in one effective set
- UC-EC-D-6 — helm-values single-value non-default-store credential omits the fragment
- UC-EC-D-7 — external-values with ESO disabled fails ES generation
- UC-EC-D-8 — Mixed external and local credentials at ES stage are rejected
- UC-EC-D-9 — credRef property absent from Credential.properties fails ES generation
- UC-EC-V-1 — External-only environment instance builds and writes external-only credentials
- UC-EC-V-1b — Legacy env build reaches external credential validation
- UC-EC-V-2 — Local-only environment instance builds and writes no external credentials
- UC-EC-V-3 — Unresolved external credential reference fails env build
- UC-EC-V-4 — External credential reference in a local-only environment fails env build
- UC-EC-V-5 — Local credential macro in an external-only environment fails env build
- UC-EC-V-6 — Mixed credential types in the merged credentials file fail env build
- UC-EC-V-7 — External credRef in technicalConfigurationParameters fails env build
- UC-EC-V-8 — Unreferenced external credential warns but does not fail env build

</details>

## How to regenerate

```bash
# from the qubership-agents root, only needs python (stdlib: re/subprocess/json) and git
python notes/architecture/test-documentation-matrix.py origin/main        # ground truth
python notes/architecture/test-documentation-matrix.py <pr-branch>        # check an unmerged PR
```
If `qubership-envgene` is not sitting next to `qubership-agents` (as it does on the author's machine), pass the checkout path as a second argument: `python notes/architecture/test-documentation-matrix.py origin/main /path/to/qubership-envgene`. Heading parsing rules: `## UC-<ID>: <title>` in docs, `Scenario: UC-<ID>: <title>` in features, `<ID>` = `UC-` plus any number of `-SEGMENT` parts plus a digit tail with an optional letter (`UC-01`, `UC-CC-DP-1`, `UC-SD-2a`, `UC-EC-V-1b` — every form in the repository is covered). The script prints JSON with the same fields this note renders; it never touches the hand-written notes (e.g. the UC-09 vs UC-06 duplicate) — that's a human call, not autogenerated.
