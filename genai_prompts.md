# Real GenAI prompts — run these yourself in a CMU-approved tool

**Recommended tool: Google Gemini** — provided free through CMU (with usage limits).
Microsoft Copilot (also free through CMU) and ChatGPT (free tier) work as substitutes.
You must actually run this conversation and save the real chat. Do not paste in a fabricated transcript.

## Step 0 — Set up

1. Open Google Gemini (or Copilot) and start a **new chat**.
2. Use the attachment button to upload **`Life Expectancy at Birth.xlsx`** from this folder.
3. Send the prompts below one at a time; wait for each response, then send the next. This produces a genuine multi-round transcript you can submit.
4. The spreadsheet is the single source of truth. If a number is not in the file, ask the tool to recompute rather than accept it.

---

## Prompt 1 — load, verify, and aggregate

> I'm redesigning a data visualization for a course and I've attached `Life Expectancy at Birth.xlsx` (World Bank life expectancy, 1960–2015). Columns: Country, Country Code, Region, Income Group, Year, Life Expectancy. First load it and confirm in text: (1) the number of rows and columns; (2) how many countries have a non-null value for 2015 (rows where Region is not null); (3) the 2015 "World" average; and (4) the mean life expectancy for each of the seven regions in 2000 and in 2015, plus the change between them.

## Prompt 2 — build the focused chart

> Now build a dumbbell chart (connected range dots) of the regional averages. One row per region, sorted by the 2015 value. For each region, draw a hollow dot for 2000 and a solid dot for 2015 connected by a line; label the 2000 and 2015 values and the gain in years. Add a vertical dashed reference line at the 2015 World average (71.7) labeled "world avg 71.7". Use a clean sans-serif font, remove the top/right/left spines, and use light horizontal gridlines.

## Prompt 3 — emphasize the story and export

> Refine it to make the argument clear. Highlight Sub-Saharan Africa in a distinct accent color (its connector and 2015 dot) and keep the other regions a single muted blue. Use the declarative title "The world is living longer and converging — Africa is catching up fastest" and a subtitle noting that Sub-Saharan Africa gained 8.2 years but still sits about 11 years below the world average. Add a source line: "Source: World Bank via MakeoverMonday 2017/W45". Verify the palette is distinguishable in grayscale and export a high-resolution PNG (at least 1600 px on the short edge) on a white background. Before finalizing, recompute and report the min, max, and mean so I can confirm nothing was invented.

## Prompt 4 (optional) — add named-country nuance

> As a companion view, build a small slopegraph for 2000 and 2015 of these countries: Ethiopia, Nigeria, Swaziland, Lesotho, India, China, United States, Japan. I want to show that the regional average hides variation — Ethiopia gained 12.6 years while Swaziland gained only 0.2.

---

## Step 4 — save the real evidence

1. **Download the final image** and save it in this folder as **`final_redesign.png`**.
2. **Save the conversation:** use Gemini's share/copy option (or copy the full chat) into a document named `ai_chat_transcript.md`. This is the real artifact the portfolio references.
3. Cross-check the saved PNG against `final_reference.png` (the design target): seven regions, hollow 2000 / solid 2015 dots, world-average line, Sub-Saharan Africa highlighted, matching values.
