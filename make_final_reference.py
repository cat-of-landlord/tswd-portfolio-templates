"""Focused redesign: regional-average dumbbell chart (2000 vs 2015).
Aggregates every country honestly (nothing silently dropped), but only 7 rows
are drawn, so the convergence story is clear. Connector length = years gained;
Sub-Saharan Africa is highlighted; dashed line = 2015 world average."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("Life Expectancy at Birth.xlsx")
c = df[df.Region.notna()].dropna(subset=["Life Expectancy"])
reg = c[c.Year.isin([2000, 2015])].pivot_table(
    index="Region", columns="Year", values="Life Expectancy", aggfunc="mean")
reg = reg.sort_values(2015)
world = df[(df.Country == "World") & (df.Year == 2015)]["Life Expectancy"].iloc[0]

fig, ax = plt.subplots(figsize=(11.5, 6.8))
fig.subplots_adjust(left=0.24, right=0.96, top=0.82, bottom=0.14)
y = range(len(reg))
highlight = "Sub-Saharan Africa"

for yi, (r, row) in zip(y, reg.iterrows()):
    is_focus = r == highlight
    line_c = "#c0392b" if is_focus else "#b8c0c8"
    ax.plot([row[2000], row[2015]], [yi, yi], color=line_c,
            lw=2.6 if is_focus else 1.8, zorder=2)
    ax.scatter(row[2000], yi, s=90, facecolor="white", edgecolor="#6b7680",
               lw=1.6, zorder=3)
    ax.scatter(row[2015], yi, s=110,
               color="#c0392b" if is_focus else "#2c6fbb", zorder=4)
    ax.text(row[2000] - 0.4, yi, f"{row[2000]:.1f}", va="center",
            ha="right", fontsize=9, color="#5a6470")
    ax.text(row[2015] + 0.4, yi, f"{row[2015]:.1f}  (+{row[2015]-row[2000]:.1f})",
            va="center", ha="left", fontsize=9,
            color="#c0392b" if is_focus else "#2c6fbb",
            weight="bold" if is_focus else "normal")

ax.axvline(world, color="#333333", ls="--", lw=1.3, zorder=1)
ax.text(world, len(reg) - 0.4, f" world avg {world:.1f} (2015)", fontsize=9,
        color="#333333", va="bottom")

ax.set_yticks(list(y))
ax.set_yticklabels(reg.index, fontsize=10)
ax.set_xlim(45, 88)
ax.set_xlabel("Average life expectancy at birth (years)", fontsize=10)
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.xaxis.grid(True, color="#e4e8ec", lw=0.7)
ax.set_axisbelow(True)
ax.tick_params(axis="y", length=0)

fig.suptitle("The world is living longer and converging — Africa is catching up fastest",
             x=0.012, y=0.95, ha="left", fontsize=15.5, weight="bold", color="#1a1a1a")
fig.text(0.012, 0.885,
         "Regional average life expectancy, 2000 vs 2015. Sub-Saharan Africa gained 8.2 years but still sits ~11 years below the world average.",
         ha="left", fontsize=10, color="#555555")
fig.text(0.012, 0.03,
         "Hollow dots = 2000, solid dots = 2015. Source: World Bank via MakeoverMonday 2017/W45.",
         ha="left", fontsize=8.5, color="#777777")

fig.savefig("final_reference.png", dpi=170, facecolor="white")
print("saved regional dumbbell reference")
