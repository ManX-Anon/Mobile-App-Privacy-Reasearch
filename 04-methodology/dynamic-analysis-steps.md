# Dynamic Analysis Procedure (optional)

**Setup:** Android emulator/test device, throwaway account, mitmproxy (or Burp) on laptop, proxy configured on device.

**Fixed test script (same for every app, ~5 minutes):**
1. Fresh install, launch app
2. Go through onboarding; deny optional permissions first run (Run A), then accept all (Run B)
3. Browse main features for 3 minutes
4. Leave app idle in background for 1 minute
5. Close app

**Capture:** export flows as HAR (mitmproxy: `mitmdump -nr flows --set hardump=app01.har`) to `03-data/raw/traffic/<app_id>.har`.

**Record:** domains contacted, and whether the domain belongs to a known tracker/ad network.

**Limitations to report:** certificate pinning (mark app as "pinned - not analyzed"), apps that refuse to run on emulators, traffic that is not HTTP(S).
