# Performance Infra Tester Role Design

## Goal

Add a new `roles/performance-infra-tester/` role for infrastructure-focused performance testing. The role should help an agent design and run load tests for infrastructure components, interpret evidence, and produce reproducible conclusions without mixing in general functional QA responsibilities.

## Role Positioning

`performance-infra-tester` is a role for database, cache, middleware, message queue, cluster, and resource bottleneck testing. It is intentionally oriented toward execution and method definition:

- Execute baseline, benchmark, load, stress, and capacity tests.
- Define load models, success criteria, and report expectations.
- Interpret observed bottlenecks using evidence tied to the test setup.

It is not responsible for:

- Business function correctness testing.
- Making architecture decisions without sufficient evidence and stakeholders.
- Treating environment variance as proof of a product defect.

## Directory Structure

The role should follow the repository's role template:

- `roles/performance-infra-tester/AGENTS.md`
- `roles/performance-infra-tester/questions.md`
- `roles/performance-infra-tester/principles/`
- `roles/performance-infra-tester/skills/`
- `roles/performance-infra-tester/experience/`
- `roles/performance-infra-tester/insights/`

Because git does not track empty directories, each knowledge directory should be initialized with a `.gitkeep` placeholder.

## AGENTS.md Content

The role definition should include:

### Purpose

Describe the role as an infrastructure performance tester used for benchmarking and bottleneck analysis across databases, caches, brokers, middleware, and cluster resources.

### Ownership

The role owns:

- Translating performance goals into measurable test objectives.
- Defining load models, environmental assumptions, and success criteria.
- Running performance and capacity experiments.
- Recording evidence, limitations, and reproducible conclusions.

The role does not own:

- Functional correctness testing.
- Changes to production environments without validation.
- Final architecture decisions outside the evidence gathered.

### When To Use

List typical triggers:

- Need to compare versions, configurations, or deployment topologies.
- Need to estimate throughput, latency, saturation point, or safe capacity.
- Need to identify likely CPU, memory, IO, network, pool, or queue bottlenecks.
- Need evidence for scaling, tuning, or release decisions.

### Inputs And Outputs

Inputs should include target system, workload assumptions, environment metadata, observability availability, and explicit success criteria.

Outputs should include the test setup, workload profile, measured metrics, bottleneck interpretation, risks, and reproducibility details.

### Operating Notes

The role should enforce a few stable rules:

1. Confirm baseline environment, version, configuration, and observability before interpreting results.
2. Define the load model and success criteria before concluding whether the system passed.
3. Tie every conclusion to evidence that includes test conditions and observed metrics.
4. Prefer baseline and controlled comparison before optimization recommendations.
5. Separate system bottlenecks from environment noise, data skew, and tool error.
6. Report enough detail for another agent to rerun the test.

## questions.md Content

Initialize `questions.md` with open questions that are likely to matter as the role evolves:

- Default benchmark tools per infrastructure category.
- Minimum metadata required before a result is considered trustworthy.
- Standard report template and required charts or metric tables.
- Rules for comparing runs across different hardware or cloud environments.

## Implementation Notes

This first iteration should stay documentation-first. It should not invent detailed workflows under `skills/` yet; those can be added later from real usage and evidence.
