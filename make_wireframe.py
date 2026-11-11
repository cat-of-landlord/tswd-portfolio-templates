"""Redesign wireframe for MakeoverMonday 2017/W45: WHO Life expectancy at birth, 2015.
Original: WHO dashboard = left country table + green choropleth + unlabeled 'country ranking' area chart.
Redesign: a readable, SORTED horizontal bar chart of life expectancy (years) for the
longest- and shortest-lived countries, region-colored, with a world-average reference line.
Values are illustrative 2015 WHO figures for a wireframe; use the official XLSX for the build."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

# (country, life expectancy 2015, region)  -- illustrative WHO 2015 values
rows = [
    ("Central African Rep.", 52, "Africa"),
    ("Sierra Leone",         52, "Africa"),
    ("Chad",                 53, "Africa"),
    ("Nigeria",              53, "Africa"),
    ("Lesotho",              53, "Africa"),
    ("Somalia",              56, "Africa"),
    ("Mozambique",           57, "Africa"),
    ("South Africa",         57, "Africa"),
    ("India",                68, "SE Asia"),
    ("China",                76, "W. Pacific"),
    ("United States",        79, "Americas"),
    ("Brazil",               75, "Americas"),
    ("United Kingdom",       81, "Europe"),
    ("Australia",            82, "W. Pacific"),
    ("Italy",                83, "Europe"),
    ("Japan",                84, "W. Pacific"),
]
rows = sorted(rows, key=lambda r: r[1])
region_colors = {"Africa": "#d6604d", "SE Asia": "#e6a23c", "Americas": "#4e9a94",
                 "Europe": "#5b7db1", "W. Pacific": "#6aa84f"}
labels=[r[0] for r in rows]; vals=[r[1] for r in rows]; cols=[region_colors[r[2]] for r in rows]

fig, ax = plt.subplots(figsize=(12.5, 7.6))
fig.subplots_adjust(left=0.20, right=0.96, top=0.82, bottom=0.27)
y=np.arange(len(rows))
ax.barh(y, vals, color=cols, height=0.66, zorder=3)
for yi,v in zip(y,vals):
    ax.text(v+0.4, yi, f"{v}", va="center", fontsize=9, color="#22303c", zorder=4)
ax.axvline(72, color="#444", ls="--", lw=1.2, zorder=2)
ax.text(72, len(rows)-0.3, " world avg ≈72", fontsize=8.5, color="#444", va="bottom")
ax.set_yticks(y); ax.set_yticklabels(labels, fontsize=9.5, color="#22303c")
ax.set_xlim(45, 88); ax.set_xticks([50,60,70,80])
ax.set_xticklabels(["50","60","70","80 years"], fontsize=8.5, color="#5a6a78")
for s in ["top","right","left"]: ax.spines[s].set_visible(False)
ax.xaxis.grid(True, color="#d9dee3", lw=0.8, zorder=0); ax.set_axisbelow(True)

fig.suptitle("Life expectancy spans 30 years: from the low 50s in parts of Africa to the mid-80s in Japan",
             x=0.02, y=0.95, ha="left", fontsize=13, weight="bold", color="#22303c")
fig.text(0.02, 0.895, "Life expectancy at birth, both sexes, 2015 (illustrative)   ·   Source: World Health Statistics 2016, WHO",
         ha="left", fontsize=9, color="#5a6a78")

from matplotlib.patches import Patch
handles=[Patch(color=c, label=r) for r,c in region_colors.items()]
ax.legend(handles=handles, loc="lower right", frameon=False, fontsize=8.5, title="WHO region", title_fontsize=8.5)

fig.patches.append(FancyBboxPatch((0.20, 0.02), 0.74, 0.15,
                     boxstyle="round,pad=0.012", transform=fig.transFigure,
                     fc="#fff4e5", ec="#e0a04f", lw=1.0, zorder=5))
fig.text(0.215, 0.135,
         "WIREFRAME NOTE  ·  Replace the 3-panel dashboard (long table + green map + unlabeled area chart) with ONE sorted bar chart.",
         fontsize=8.5, color="#7a4a12", va="center", zorder=6)
fig.text(0.215, 0.092,
         "The original's 'country ranking' area chart had no country labels — here every bar is labeled, on a common 45–88 scale,",
         fontsize=8.5, color="#7a4a12", va="center", zorder=6)
fig.text(0.215, 0.050,
         "region-colored, with a world-average reference line, so the 30-year gap between Africa and the richest countries is visible.",
         fontsize=8.5, color="#7a4a12", va="center", zorder=6)

fig.savefig("redesign_wireframe.png", dpi=170, facecolor="white")
print("saved")
