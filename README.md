# Mobile App Privacy Research

**Working title:** Do Popular Android Apps Collect More Data Than Their Privacy Labels Disclose?

**Author:** <your name> | **Course:** <course> | **Supervisor:** <name>

## Research question
Do popular Android apps request permissions and embed third-party trackers that go beyond what their
Google Play "Data safety" declarations disclose?

## Pipeline
1. Choose apps -> `02-sample/app-list.csv`
2. Static analysis (MobSF + Exodus) -> save reports to `03-data/raw/`
3. Record Data safety labels -> `03-data/data-safety-labels/labels.csv`
4. Run scripts in `05-analysis/scripts/` (order below)
5. Write up in `07-paper/`

## Run order
```bash
pip install -r 05-analysis/requirements.txt
python 05-analysis/scripts/parse_mobsf.py      # -> permissions.csv, trackers.csv
python 05-analysis/scripts/parse_traffic.py    # -> domains-contacted.csv (optional, needs HAR files)
python 05-analysis/scripts/score_mismatch.py   # -> mismatch-scores.csv
python 05-analysis/scripts/make_charts.py      # -> 06-results/figures/
```

## Ethics
Own test device/emulator, throwaway accounts only. No APK redistribution. See `00-planning/scope-and-ethics.md`.
