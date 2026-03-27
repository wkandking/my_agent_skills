---
name: mechanism-analysis-workflow
description: Use when explaining why a database, planner, or execution operator behaves the way it does, especially when you need to separate semantics, plan shape, execution strategy, and expression/kernel details.
---

# Mechanism Analysis Workflow

## Goal

Turn a vague "why does it work like this?" question into a defensible mechanism explanation with a minimal evidence chain.

The output should not be a pile of observations. It should answer:

1. what behavior is being explained
2. which layer causes it
3. what is proven versus inferred

## Use This Skill When

- a query engine, database, or operator behaves in a surprising way
- you need to explain whether behavior comes from semantics, planning, execution, or a lower-level kernel
- the user keeps forcing narrower distinctions such as:
  - VLE vs matrix multiplication
  - DISTINCT semantics vs operator behavior
  - path enumeration vs end-node reachability

## Core Rule

Do not jump from one observed query result straight to implementation claims.

Always separate these layers first:

1. result semantics
2. plan/operator selection
3. execution strategy
4. expression/kernel construction

## Minimal Evidence Chain

Every accepted explanation should include:

1. phenomenon
2. minimal reproduction
3. `EXPLAIN`/`PROFILE` or equivalent intermediate state
4. source-level implementation evidence
5. boundary of the conclusion

## Workflow

1. Narrow the question until it is binary or near-binary.
   - Good: "Does `*2..2` use VLE or matrix multiplication?"
   - Better: "At operator-selection level, does `*2..2` enter the VLE family? At expression level, is it compiled as matrix multiplication?"

2. Define the analysis layers before answering.
   - semantics
   - plan
   - execution
   - expression/kernel

3. Build one minimal graph and a few canonical queries.
   - keep the graph small enough that duplicate paths, shortest paths, and label filtering are all visible
   - use one example per claim whenever possible

4. Compare paired queries that isolate one variable at a time.
   - `RETURN x` vs `RETURN DISTINCT x`
   - `[*1..1]` vs `[*2..2]`
   - path-returning vs node-returning queries
   - shortest-path syntax vs ordinary variable-length syntax

5. Check plan shape.
   - identify which logical or physical operator family is selected
   - do not assume the operator name fully determines lower-level behavior

6. Check execution strategy.
   - identify whether traversal is DFS, BFS, pruning DFS, row-iterator DFS, or something else
   - inspect how state is stored: stack, queue, visited set, path buffer, per-level iterators

7. Check expression/kernel construction.
   - ask whether the operator internally uses an algebraic expression, matrix multiplication, repeated expansion, or a special cursor
   - do not force a false binary between operator family and kernel

8. Separate confirmed facts from inferences.
   - confirmed: directly supported by source or reproducible output
   - inferred: engineering interpretation from source shape or behavior

9. Rewrite the findings into a stable document structure.
   - scope and terminology
   - minimal reproduction
   - semantics
   - plan
   - execution
   - data structure or kernel
   - optimizations and exceptions
   - comparison or boundaries

## Stable Heuristics

- If two explanations can both be true at different layers, do not collapse them into one binary answer.
- If the user asks an overloaded question, split it into layer-specific answers before writing prose.
- If a result depends on duplicate end-nodes or path multiplicity, test the `DISTINCT` version immediately.
- If a query uses fixed-hop syntax like `*2..2`, check both:
  - whether it still enters the variable-length operator family
  - whether its relationship expression is compiled into matrix multiplication

## Output Shape

A good mechanism explanation should end with:

- one short answer to the exact user question
- one paragraph that explains the layer split
- a small list of source references
- a short "what this does not prove" boundary when needed
