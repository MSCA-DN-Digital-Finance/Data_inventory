# Contributing to the DIGITAL inventory

Use **Add a contribution** on the website to add an entry or **Suggest an update** in a record to prefill an existing entry. Prepare the proposal, review the JSON, then open and submit the GitHub issue. A GitHub account is required to submit an issue. You can also download the proposal JSON and attach it to an issue. Saving a draft stores it in your browser on your device; it does not send it to maintainers.

A source is a provider or platform. A dataset is a specific extract, panel or prepared research collection. Document access to the prepared dataset separately from access to the underlying provider.

## Metadata

| Field | Meaning |
| --- | --- |
| `id` | Stable lowercase slug, unique within sources or datasets. Do not change an existing ID when renaming. |
| `name` / `dataset_name` | Human-readable name; use `dataset_name` in the datasets CSV. |
| `short_description` | Contents, research scope and relevant variables. |
| `subjects` | Topics separated by semicolons. Reuse existing topic names where appropriate. |
| `region` | Geographic coverage; semicolons for multiple regions. |
| `IRP` | Contributing individual research project number; semicolons for multiple contributors. |
| `link` | Public HTTP(S) landing page for this provider or prepared dataset. Avoid temporary signed download URLs. |
| `access_category` | `public`, `request`, `institutional`, `restricted`, or `unknown`. Public does not establish an open licence. |
| `access_notes` | Required: route, approvals, account/key requirements, charges, quotas and restrictions. Specify what remains unknown. |
| `collection` | Source delivery route (API, download, terminal, email request). The form maps dataset delivery to legacy `availability`. |
| `formats` | Actual formats, separated by semicolons, e.g. `CSV;Parquet`. Leave unknown formats blank. |
| `frequency` | Observation frequency, or clearly labelled provider update frequency. |
| `publication_lag` | Delay from the reference observation period to publication. Specify product and uncertainty. |
| `first_date`, `last_date` | Coverage of the contributed dataset/version. Label forecast horizons and snapshots clearly. |
| `history` | Source-level historical coverage, if known. |
| `history_notes` | Coverage caveats, archived versions and reproducibility notes. |
| `quality_notes` | Missingness, preparation, validation evidence, selection bias and known limitations. |
| `revision_policy` | Whether/how historical values are revised; availability of real-time vintages. |
| `license_notes` | Evidence-backed reuse, citation and redistribution conditions. |
| `documentation_url` | Public provider documentation, terms, methodology or validation page. |
| `source_ids` | Dataset-only: related source IDs, separated by semicolons. These are relationships, not inherited permissions. |
| `unit_of_observation` | Dataset-only: level of detail, e.g. country × month. |
| `last_reviewed` | ISO date `YYYY-MM-DD` for an actual metadata review. Leave blank for unverified migrations. |
| `provenance` | What was verified, by which evidence, or clearly marked contributor experience. |

Existing `access`, `availability` and `clean` fields are retained for the generated README and old workflows. The website prioritizes `access_category`, `access_notes` and `quality_notes`; when editing CSV directly, keep legacy summaries consistent where applicable. Empty fields mean unknown, never unrestricted or no issues. Do not add passwords, tokens, private contact information, raw licensed data or unsubstantiated claims.

## Maintainer review

Check the evidence and access route before applying a proposal. Confirm that the entry ID matches the intended record. Do not mark a whole entry verified when only one field has been checked: describe the scope in `provenance`. Keep observation coverage separate from the metadata review date. Use immutable versions or DOIs where possible.

### Approve entirely on GitHub

1. Review the JSON proposal in the issue body, including the access conditions and evidence.
2. Apply the **`inventory-approved`** label to the open issue. You must have repository write, maintain or admin permission. Triage permission is insufficient.
3. The **Apply approved inventory proposal** workflow validates the proposal, updates the canonical CSV and generated README, commits the change to `main`, requests a Pages deployment, adds **`inventory-applied`**, and closes the issue.

No download, CSV editing or local commands are required. The proposal must be in exactly one fenced `json` code block in the issue body (the website already produces this). For attachment-only proposals, paste the JSON into that code block before approval. Free-text requests need a structured JSON proposal first.

The automation uses the issue body captured when the approval label was applied. If the author changes the body or approval is withdrawn before processing, it stops. Review the corrected proposal, remove `inventory-approved`, and re-add it to approve the new content. Reopening or closing an issue alone does not approve anything.

Check the issue's workflow run in **Actions → Apply approved inventory proposal** if it remains open. Invalid proposals leave the inventory unchanged. Fix the JSON, review it and reapply the label. If a repository configuration or deployment-dispatch error occurs after the CSV commit, fix that problem and rerun the failed workflow; the recorded proposal hash prevents importing the same approved proposal twice. The run summary links to the commit. `inventory-applied` means the change is committed and deployment requested; **Validate and deploy inventory** reports whether the website has finished publishing.

The workflow uses the repository's built-in `GITHUB_TOKEN`, with no personal token or external service required. It explicitly dispatches the Pages workflow because bot commits do not trigger ordinary push workflows. Direct pushes to `main` must be permitted for this workflow; branch protection is never bypassed. Separate approvals retry against the latest `main` if another change is pushed concurrently.

### Optional local import

You can still download or extract the JSON object to a local file and run:

```sh
python3 scripts/import_proposal.py /path/to/proposal.json
python3 scripts/import_proposal.py /path/to/proposal.json --write
python3 scripts/build_site.py
python3 -m unittest discover -s tests -v
python3 update_README.py
```

The importer validates fields, IDs, source references, URLs and dates before applying. It also refreshes legacy access and quality summaries from the proposal for the README. An update merges supplied fields into the existing record; supplied empty fields intentionally clear values. A new source should be imported before a dataset that references it. It is also fine to edit the CSVs directly with proper CSV quoting, then run the build to validate them.

For local imports, review the CSV diff, preview the website, and open a pull request. The automated path above commits only after a maintainer has explicitly approved the issue.
