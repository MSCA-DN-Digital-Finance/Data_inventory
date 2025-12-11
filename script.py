import csv
import collections
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[0]

# Adjust these paths if you keep the CSVs elsewhere
DATA_SOURCES_CSV = ROOT / "data-sources.csv"
DATASETS_CSV = ROOT / "datasets.csv"
README_PATH = ROOT / "README.md"


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def make_table(rows, columns, header_labels=None):
    """
    rows: list of dicts
    columns: list of dict keys in desired order
    header_labels: optional list of header names to show (same length as columns)
    """
    header = header_labels or [col.replace("_", " ").title() for col in columns]
    lines = []

    # Header row
    lines.append("| " + " | ".join(header) + " |")
    # Separator row
    lines.append("|" + "|".join(["---" for _ in header]) + "|")

    # Data rows
    for r in rows:
        vals = [r.get(col, "") or "" for col in columns]
        vals = [str(v).replace("\n", " ").strip() for v in vals]
        lines.append("| " + " | ".join(vals) + " |")

    return "\n".join(lines)


def split_subjects(subjects_value):
    if not subjects_value:
        return []
    import re as _re
    out = []
    for s in _re.split(r"[;,]", subjects_value):
        s = s.strip()
        if s:
            out.append(s)
    return out


def slugify_github(text: str) -> str:
    """
    Approximate GitHub-style anchor generation:
    - lowercase
    - remove characters that are not a-z, 0-9, space, or hyphen
    - replace spaces with hyphens
    - collapse multiple hyphens
    """
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9 -]", "", text)
    text = text.replace(" ", "-")
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def build_toc(markdown: str) -> str:
    """
    Build a TOC for H2-level headings (##) in the given markdown string.
    Skips H1 and deeper levels to avoid duplicate anchor issues.
    """
    lines = markdown.splitlines()
    toc_lines = []

    for line in lines:
        m = re.match(r"^(#{1,6})\s+(.*)", line)
        if not m:
            continue
        level = len(m.group(1))
        title = m.group(2).strip()
        if (level == 2) or (level == 3) : 
            anchor = title.split('<')[1].split('\'')[1]
            indent = "  " * (level - 2) 
            toc_lines.append(f"{indent}- [{title.split('<')[0]}](#{anchor})")
        else: 
            continue

    return "\n".join(toc_lines)


# ---------- DATA SOURCES SECTION ----------

def build_data_sources_markdown(rows):
    # Sort by name
    rows_sorted = sorted(rows, key=lambda r: r["name"].lower())

    parts = []

    # 1) Master list
    parts.append("## Data Sources – Full List <a name='data-sources-full-list'></a>\n")
    parts.append(
        make_table(
            rows_sorted,
            columns=[
                "name",
                "short_description",
                "subjects",
                "IRP",
                "link",
                "access",
                "collection",
            ],
            header_labels=[
                "Name",
                "Short Description",
                "Subject(s)",
                "IRP",
                "Link",
                "Access",
                "Collection",
            ],
        )
    )

    # 2) By subject
    parts.append("\n\n## Data Sources by Subject <a name='data-sources-by-subject'></a>")
    subject_index = collections.defaultdict(list)
    for r in rows_sorted:
        for s in split_subjects(r.get("subjects", "")):
            subject_index[s].append(r)

    for subject in sorted(subject_index.keys()):
        parts.append(f"\n\n### {subject} <a name='sources-{subject}'></a>\n")
        parts.append(
            make_table(
                subject_index[subject],
                columns=[
                    "name",
                    "short_description",
                    "IRP",
                    "link",
                    "access",
                    "collection",
                ],
                header_labels=[
                    "Name",
                    "Short Description",
                    "IRP",
                    "Link",
                    "Access",
                    "Collection",
                ],
            )
        )

    # 3) By IRP
    parts.append("\n\n## Data Sources by IRP <a name='data-sources-by-irp'></a>")
    irp_index = collections.defaultdict(list)
    for r in rows_sorted:
        irp_index[r.get("IRP", "")].append(r)

    def _irp_sort_key(x):
        try:
            return int(x)
        except ValueError:
            return 9999

    for irp in sorted(irp_index.keys(), key=_irp_sort_key):
        if not irp:
            continue
        parts.append(f"\n\n### IRP {irp} <a name='sources-{irp}'></a>\n")
        parts.append(
            make_table(
                irp_index[irp],
                columns=[
                    "name",
                    "short_description",
                    "subjects",
                    "link",
                    "access",
                    "collection",
                ],
                header_labels=[
                    "Name",
                    "Short Description",
                    "Subject(s)",
                    "Link",
                    "Access",
                    "Collection",
                ],
            )
        )

    return "\n".join(parts)


# ---------- DATASETS SECTION ----------

def build_datasets_markdown(rows):
    # Sort by dataset_name
    rows_sorted = sorted(rows, key=lambda r: r["dataset_name"].lower())

    parts = []

    # 1) Master list
    parts.append("## Datasets – Full List <a name='datasets-full-list'></a>\n")
    parts.append(
        make_table(
            rows_sorted,
            columns=[
                "dataset_name",
                "short_description",
                "subjects",
                "IRP",
                "frequency",
                "first_date",
                "last_date",
                "clean",
                "availability",
            ],
            header_labels=[
                "Dataset Name",
                "Short Description",
                "Subject(s)",
                "IRP",
                "Frequency",
                "First Date",
                "Last Date",
                "Clean",
                "Availability",
            ],
        )
    )

    # 2) By subject
    parts.append("\n\n## Datasets by Subject <a name='datasets-by-subject'></a>")
    subject_index = collections.defaultdict(list)
    for r in rows_sorted:
        for s in split_subjects(r.get("subjects", "")):
            subject_index[s].append(r)

    for subject in sorted(subject_index.keys()):
        parts.append(f"\n\n### {subject} <a name='sets-{subject}'></a>\n")
        parts.append(
            make_table(
                subject_index[subject],
                columns=[
                    "dataset_name",
                    "short_description",
                    "IRP",
                    "frequency",
                    "first_date",
                    "last_date",
                    "clean",
                    "availability",
                ],
                header_labels=[
                    "Dataset Name",
                    "Short Description",
                    "IRP",
                    "Frequency",
                    "First Date",
                    "Last Date",
                    "Clean",
                    "Availability",
                ],
            )
        )

    # 3) By IRP
    parts.append("\n\n## Datasets by IRP <a name='datasets-by-irp'></a>")
    irp_index = collections.defaultdict(list)
    for r in rows_sorted:
        irp_index[r.get("IRP", "")].append(r)

    def _irp_sort_key(x):
        try:
            return int(x)
        except ValueError:
            return 9999

    for irp in sorted(irp_index.keys(), key=_irp_sort_key):
        if not irp:
            continue
        parts.append(f"\n\n### IRP {irp} <a name='sets-{irp}'></a>\n")
        parts.append(
            make_table(
                irp_index[irp],
                columns=[
                    "dataset_name",
                    "short_description",
                    "subjects",
                    "frequency",
                    "first_date",
                    "last_date",
                    "clean",
                    "availability",
                ],
                header_labels=[
                    "Dataset Name",
                    "Short Description",
                    "Subject(s)",
                    "Frequency",
                    "First Date",
                    "Last Date",
                    "Clean",
                    "Availability",
                ],
            )
        )

    return "\n".join(parts)


# ---------- MAIN: build inventory + TOC and write into README ----------

def build_inventory_markdown():
    data_sources_rows = read_csv(DATA_SOURCES_CSV)
    datasets_rows = read_csv(DATASETS_CSV)

    intro_heading = "# Data Inventory\n"
    intro_text = (
        "_This section is auto-generated from "
        "`data-sources.csv` and `datasets.csv`. "
        "Please edit those CSV files instead of the tables below._"
    )

    data_sources_md = build_data_sources_markdown(data_sources_rows)
    datasets_md = build_datasets_markdown(datasets_rows)

    # First build full content WITHOUT TOC to detect headings
    body_without_toc = (
        f"{intro_heading}\n\n"
        f"{intro_text}\n\n"
        "---\n\n"
        f"{data_sources_md}\n\n"
        "---\n\n"
        f"{datasets_md}"
    )

    toc = build_toc(body_without_toc)

    # Now assemble final content with TOC inserted after intro
    final_md = (
        f"{intro_heading}\n\n"
        f"{intro_text}\n\n"
        "## 🧭 Table of Contents\n\n"
        f"{toc}\n\n"
        "---\n\n"
        f"{data_sources_md}\n\n"
        "---\n\n"
        f"{datasets_md}"
    )

    return final_md


def main():
    inventory_md = build_inventory_markdown()
    readme_text = README_PATH.read_text(encoding="utf-8")

    pattern = r"(?s)(<!-- BEGIN INVENTORY -->).*?(<!-- END INVENTORY -->)"
    replacement = r"\1\n" + inventory_md + r"\n\2"

    new_readme = re.sub(pattern, replacement, readme_text)

    README_PATH.write_text(new_readme, encoding="utf-8")


if __name__ == "__main__":
    main()