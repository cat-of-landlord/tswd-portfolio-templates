| [home page](https://cat-of-landlord.github.io/tswd-portfolio-templates/) | [ai critique](ai-critique) | [data viz examples](dataviz-examples) | [critique by design](critique-by-design) | [final project I](final-project-part-one) | [final project II](final-project-part-two) | [final project III](final-project-part-three) |

# AI Critique #1 — The Good Charts Matrix

*Telling Stories with Data, Fall 2026. This page documents my first graphic critique, evaluated using the Good Charts framework (Berinato, 2016) and a paired critique with Microsoft Copilot.*

*Original submitted document: [critique-1-submission.docx](critique-1-submission.docx)*

## The graphic I evaluated

I selected **Graphic #2**: a dark-themed Makeover Monday choropleth map, *"Written in 1839, Still the Law Today: Married Women's Property Act."* Each U.S. state is shaded by the year it adopted a married women's property law.

## First impressions

My first read was that this is a dark U.S. choropleth where each state is shaded by the year it adopted a law giving women the right to own property. The mint-teal cluster in the Northeast and the large dark-blue block across the West read like an east-to-west spread of the law over time, with the South and Florida adopting later.

Searching for more, I noticed several problems: there are seven unrelated fills that do not visually progress from early to late; a solid black background fills most of the frame; white and faint-outlined shapes in the bottom-right inset (likely Puerto Rico and other island territories) are never defined by the legend; the year bands are uneven — 1848-1859 (12 years), four 10-year bands, then 1900-1919 and 1940-1959 (20 years each) — with 1920-1939 missing entirely. There are no state labels, no data source, no as-of date, and a leftover "Switch View" button from the interactive tool.

Open question after first look: are the white territories places that never adopted a comparable law, places that were not U.S. states at the time, or simply missing data? The graphic does not say.

## What I like

- **Chart type fits the question.** A choropleth map is the right visualization for a geographic diffusion question. The reader can immediately see that the earliest adopters cluster in the Northeast while the Mountain West, South, Florida, Alaska and Hawaii adopted later.
- **Structure.** The title states the topic plainly ("Year States Adopted Laws Giving Women the Right to Own Property") and a legend with year ranges is provided. Alaska and Hawaii are moved to insets so their small size does not distort the contiguous states.
- **Regional signal.** The early-adopter Northeast cluster stands out enough to give a rough sense of the regional pattern at a coarse glance, and the source (Married Women's Property Act of 1839) is documented for further reference.

## What I dislike

- **Color.** The seven fills are unrelated categorical hues rather than an ordered scale — no light-to-dark or single-hue progression — so a viewer cannot read chronology at a glance and must decode every legend entry. Per Good Charts (Berinato), viewers expect saturation/lightness to indicate higher vs. lower values; arbitrary or reversed color scales lead to wrong conclusions. The red/green and mauve/olive pairs are also hard to separate for red-green color-blind viewers.
- **Background.** A solid black canvas creates heavy contrast and glare, competes with the state fills, and prints poorly.
- **Missing / excluded data.** The white (and some outline-only) territories in the inset have no legend entry, so it is unclear whether they never adopted a comparable law, were not U.S. states at the time, or are missing data — and the treatment is inconsistent across islands.
- **Scale.** The year bins are unequal (12 / 10 / 10 / 10 / 10 / 20 / 20 years) with a silent 1920-1939 gap, yet the legend swatches are equal size, implying equal intervals — a classic "improper binning" problem.
- **Cognition / typography.** With no direct state labels, the reader makes repeated eye trips between map and small legend text; no data source or as-of date appears; the floating "Switch View" button signals an unpolished export.

## What I wish I saw

- A sequential single-hue ramp (light = earliest, dark = latest, or the reverse with an explicit key), color-blind safe, on a white or light-gray background.
- Equal-width 10-year bins or a continuous sequential scale mapped to exact adoption year, with the 1920-1939 gap shown or explained.
- An explicit legend category for "Territory / no comparable property law / not a U.S. state in this period," applied consistently as a neutral gray or hatch.
- Direct labels for a few noteworthy states, the data source and as-of date printed on the figure, and removal of the "Switch View" widget.

## My three recommendations

1. **Replace the seven unrelated categorical hues with one sequential light-to-dark single-hue ramp** (e.g., ColorBrewer sequential blues, lightest for 1848, darkest for 1959) and move the canvas from black to white or very light gray, verifying the scheme with a color-blind simulator. *Ordered lightness lets readers rank states chronologically in seconds instead of decoding seven legend entries.*
2. **Rebuild the year encoding with equal-width bins** (10-year bands from the 1840s through the 1950s) or a continuous exact-year scale; show or explicitly explain the 1920-1939 gap, and make legend swatch weight reflect the time span each band represents. *Equal intervals make color differences correspond to equal time differences.*
3. **Define the uncolored inset territories explicitly** — a legend entry such as "Territory / no comparable property law / not a U.S. state in this period," applied consistently in neutral gray — and print the data source and as-of date on the figure; remove the leftover "Switch View" button.

## Copilot's three recommendations

1. Encode time with a perceptually ordered sequential palette: one light-to-dark blue ramp, legend ordered earliest → latest, thin white/gray state borders, and a separate neutral gray (#D9D9D9) reserved for non-data or missing territories.
2. Replace the irregular class structure with exact adoption year on a continuous scale or uniform decade bins; explicitly annotate the empty 1920-1939 period under the legend; give equal time spans equal swatch weight.
3. Add a narrow companion chart below the map: a horizontal decade histogram showing how many states adopted a law in each decade, using the same color scale as the map.

## Final synthesized recommendations

1. **(Synthesis — me + Copilot)** Replace the seven categorical hues with one ordered sequential light-to-dark blue ramp (lightest = earliest 1848, darkest = latest), move off black to white or light gray, order the legend earliest → latest, add thin neutral state borders, and reserve a distinct neutral gray for territories or missing values. Ordered lightness encodes time at a glance; the light background improves figure-ground separation and print legibility; contrast between adjacent colors should be checked for color-blind separability.
2. **(Synthesis — me + Copilot)** Rebuild the year encoding with equal-width decade bins or a continuous exact-year scale, annotate the empty 1920-1939 period instead of jumping over it, give equal time spans equal swatch weight, separate the different missing-data cases (missing, not applicable, territory, never adopted), and print the data source and as-of date on the figure.
3. **(Copilot's idea, adopted)** Add a narrow companion decade histogram beneath the map, counting how many states adopted a law each decade on the same color scale. The map shows geography well but hides the temporal distribution; this chart answers whether adoption clustered in a few periods or spread evenly over time.

## Score

- **Design execution: -3**
- **Contextual awareness: -4**

The map only delivers basic geographic presentation. Its unordered color palette mis-encodes sequential time data with low readability on a black canvas; uneven bins, undefined missing data and an absent source undermine its credibility.

## Reflection: how did AI go?

I relied on a **combination**. My own observations drove the main problems — the unrelated categorical colors, the black background, the uneven year bins, and the unexplained white territories — because those came straight from looking at the map. Copilot helped me sharpen implementation: keeping the missing-data gray visually separate from the lightest bin, adding thin borders as color differences narrow, and thinking through continuous scale versus bins. Its biggest new contribution was the companion decade histogram, which I had not thought of and adopted as my third final recommendation.

Copilot did not really get in the way; where it offered options I was unsure about (such as a fully continuous scale), I kept my own equal-bin framing instead of copying it. I feel fairly confident in the final decisions because each one ties back to something visible on the map or to the assigned readings, rather than being a generic suggestion.

## References

- Berinato, S. (2016). *Good Charts: The HBR Guide to Making Smarter, More Persuasive Data Visualizations.* Harvard Business Review Press.
- Source: "Map Monday: Written in 1839, Still the Law Today: Married Women's Property Act." Accessed August 3, 2026.

## AI acknowledgements

Beyond the required Microsoft Copilot critique, I used AI to summarize the main points of the assigned readings so I could understand them faster. Some sections of my writing were organized, translated, or polished with AI help, and when writing the supporting reasons I used AI to locate where key points appeared in the reading materials. The observations and final recommendations are my own and were checked against the source readings.
