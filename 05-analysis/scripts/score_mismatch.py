"""Compare data categories implied by dangerous permissions with Data safety declarations."""
import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROCESSED = ROOT / "03-data" / "processed"
MAP_FILE = ROOT / "04-methodology" / "permission-category-map.csv"
LABELS = ROOT / "03-data" / "data-safety-labels" / "labels.csv"


def split(value):
    return {x.strip() for x in (value or "").split(";") if x.strip()}


def main():
    perm_to_cat = {}
    with open(MAP_FILE, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            perm_to_cat[r["permission"]] = r["data_category"]

    observed = defaultdict(set)
    with open(PROCESSED / "permissions.csv", newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["status"] == "dangerous" and r["permission"] in perm_to_cat:
                observed[r["app_id"]].add(perm_to_cat[r["permission"]])

    declared = {}
    with open(LABELS, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            declared[r["app_id"]] = split(r["declared_collected"]) | split(r.get("declared_shared"))

    rows = []
    for app_id in sorted(set(observed) | set(declared)):
        obs = observed.get(app_id, set())
        dec = declared.get(app_id, set())
        undisclosed = obs - dec
        rows.append([
            app_id,
            ";".join(sorted(obs)),
            ";".join(sorted(dec)),
            ";".join(sorted(undisclosed)),
            len(undisclosed),
        ])

    with open(PROCESSED / "mismatch-scores.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["app_id", "observed_categories", "declared_categories", "undisclosed", "score"])
        w.writerows(rows)
    print(f"Scored {len(rows)} apps.")


if __name__ == "__main__":
    main()
