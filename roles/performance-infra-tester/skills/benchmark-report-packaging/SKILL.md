---
name: benchmark-report-packaging
description: Use to turn benchmark results, charts, and fixed-point cases into a deliverable analysis report.
---

# Benchmark Report Packaging

## Goal

Turn raw benchmark results into a final report where data leads, charts support the story, and conclusions are explained, instead of merely stacking figures or reporting peak values.

## Workflow

1. Split scenarios by semantic variables and deployment variables before writing conclusions.
2. In each section, present data tables before charts.
3. Prefer line charts for trends and bar charts for summaries. Do not default to heatmaps unless density itself is the point.
4. Under every chart, add a short explanation that answers at least three questions:
   - What question is this chart answering?
   - What is the main trend?
   - Why does that trend matter?
5. End each section with a short summary that pulls the section's main thread together.
6. If there are fixed-point case studies, keep them in the main body and surface the key takeaway at the start of the final judgment.
7. If the report needs to align with a reference report, do not change only the headings:
   - align the heading style as well
   - align the section order
   - align the summary style
   - align the chart placement
   - align the explanation density

## Recommended Section Order

1. Document objective
2. Scenarios and test method
3. Executive summary
4. Performance results
5. `perf` or resource-side supplements
6. Mechanism explanation
7. Final judgment
8. Appendix or raw files
