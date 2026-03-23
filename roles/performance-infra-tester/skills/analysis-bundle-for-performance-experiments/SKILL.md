---
name: analysis-bundle-for-performance-experiments
description: Use to package a performance experiment into a reusable analysis bundle for offline analysis, review, and sharing.
---

# Analysis Bundle For Performance Experiments

## Goal

Turn a performance experiment into a stable, evidence-complete analysis bundle instead of leaving behind only averages or a few charts.

## Minimum Inputs

- input samples or candidate points
- workload or request definitions
- raw execution results
- aggregated summary

## Output Layout

- `inputs/`
  - input samples
  - workload
  - generation scripts
- `results/raw/`
  - raw records
  - summary
- `results/derived/`
  - input-size tables
  - request catalog
  - per-item comparison tables
  - aggregated comparison tables
- `README.md`
  - experiment objective
  - execution method
  - metric definitions
  - directory guide

## Workflow

1. Organize the input samples and preserve the size information for each sample.
2. Organize the workload or request definitions, including names, parameters, and text.
3. Run the experiment and keep the raw records instead of saving only averages.
4. Generate per-item comparison tables that connect input size to latency.
5. Generate an aggregated summary for quick comparison.
6. Write a `README.md` that explains the experiment objective, execution method, and metric definitions.

## Core Requirements

1. Raw records must be retained. Do not keep only averages.
2. Input-size information must be stored alongside latency results, or later performance differences will be hard to explain.
3. The final deliverable should let someone review the analysis bundle directory alone and still reconstruct the experiment inputs, execution method, and main conclusions.
