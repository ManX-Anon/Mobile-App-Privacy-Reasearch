# Static Analysis Procedure

1. Download the APK of the exact version you recorded (legitimate source; keep in `03-data/raw/apks/`, local only).
2. Upload to MobSF (local Docker instance). Export the **JSON report** to `03-data/raw/mobsf-reports/<app_id>.json`.
3. Check the app's tracker list on Exodus Privacy; save to `03-data/raw/exodus-reports/<app_id>.txt` (or use MobSF's tracker section).
4. Record tool versions in `tools-and-versions.md`.
5. Run `parse_mobsf.py` to build `permissions.csv` and `trackers.csv`.
