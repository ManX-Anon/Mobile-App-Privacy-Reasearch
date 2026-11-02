"""Parse HAR captures (one per app) into domains-contacted.csv."""
import csv
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[2]
TRAFFIC = ROOT / "03-data" / "raw" / "traffic"
OUT = ROOT / "03-data" / "processed"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    for har in sorted(TRAFFIC.glob("*.har")):
        app_id = har.stem
        data = json.loads(har.read_text(encoding="utf-8"))
        entries = data.get("log", {}).get("entries", [])
        hosts = Counter(
            urlparse(e["request"]["url"]).hostname or "" for e in entries
        )
        for host, count in hosts.most_common():
            rows.append([app_id, host, count])

    with open(OUT / "domains-contacted.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["app_id", "host", "request_count"])
        w.writerows(rows)
    print(f"Wrote {len(rows)} app-host rows.")


if __name__ == "__main__":
    main()
