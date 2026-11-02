"""Generate figures from processed CSVs."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
PROCESSED = ROOT / "03-data" / "processed"
FIGS = ROOT / "06-results" / "figures"
FIGS.mkdir(parents=True, exist_ok=True)

apps = pd.read_csv(ROOT / "02-sample" / "app-list.csv")[["app_id", "category"]]


def bar_by_category(series_by_app, ylabel, title, filename):
    df = apps.merge(series_by_app.rename("value"), on="app_id", how="left").fillna({"value": 0})
    means = df.groupby("category")["value"].mean().sort_values(ascending=False)
    ax = means.plot(kind="bar", figsize=(7, 4))
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(FIGS / filename, dpi=200)
    plt.close()


def main():
    perms = pd.read_csv(PROCESSED / "permissions.csv")
    dangerous = perms[perms["status"] == "dangerous"].groupby("app_id").size()
    bar_by_category(dangerous, "Avg. dangerous permissions per app",
                    "Dangerous permissions by app category", "fig1-permissions-by-category.png")

    trackers = pd.read_csv(PROCESSED / "trackers.csv").groupby("app_id").size()
    bar_by_category(trackers, "Avg. trackers per app",
                    "Embedded trackers by app category", "fig2-trackers-per-app.png")

    mm_path = PROCESSED / "mismatch-scores.csv"
    if mm_path.exists():
        mm = pd.read_csv(mm_path).set_index("app_id")["score"]
        bar_by_category(mm, "Avg. undisclosed categories",
                        "Label mismatch score by category", "fig3-label-mismatch.png")
    print("Figures saved to", FIGS)


if __name__ == "__main__":
    main()
