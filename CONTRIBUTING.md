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

Download or extract the JSON object from the issue to a local file, then run:

```sh
python3 scripts/import_proposal.py /path/to/proposal.json
python3 scripts/import_proposal.py /path/to/proposal.json --write
python3 scripts/build_site.py
python3 -m unittest discover -s tests -v
python3 update_README.py
```

The importer validates fields, IDs, source references, URLs and dates before applying. It also refreshes legacy access and quality summaries from the proposal for the README. An update merges supplied fields into the existing record; supplied empty fields intentionally clear values. A new source should be imported before a dataset that references it. It is also fine to edit the CSVs directly with proper CSV quoting, then run the build to validate them.

Review the CSV diff, preview the website, and open a pull request. CI validates the build before deployment. Proposals never trigger automatic commits: external submissions remain under maintainer review.
