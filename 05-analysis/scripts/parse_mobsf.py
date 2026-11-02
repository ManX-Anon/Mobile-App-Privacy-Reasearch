"""Parse MobSF JSON reports into permissions.csv and trackers.csv."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "03-data" / "raw" / "mobsf-reports"
OUT = ROOT / "03-data" / "processed"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    perm_rows, tracker_rows = [], []

    for report in sorted(REPORTS.glob("*.json")):
        app_id = report.stem
        data = json.loads(report.read_text(encoding="utf-8"))
        package = data.get("package_name", "")

        permissions = data.get("permissions", {}) or {}
        for perm, info in permissions.items():
            status = info.get("status", "unknown") if isinstance(info, dict) else "unknown"
            perm_rows.append([app_id, package, perm, status])

        trackers = data.get("trackers", {}) or {}
        for t in trackers.get("trackers", []) or []:
            tracker_rows.append([app_id, t.get("name", "")])

    with open(OUT / "permissions.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["app_id", "package", "permission", "status"])
        w.writerows(perm_rows)

    with open(OUT / "trackers.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["app_id", "tracker_name"])
        w.writerows(tracker_rows)

    print(f"Wrote {len(perm_rows)} permission rows, {len(tracker_rows)} tracker rows.")


if __name__ == "__main__":
    main()
