# Data Models and Query Languages

Data models are one of the deepest ideas in distributed systems and data engineering:

> Data models are not merely storage formats.
>
> They are abstractions that shape:
> - system behavior
> - query patterns
> - scalability characteristics
> - engineering thinking

---

# Learning Goals

This repository focuses on understanding:

- relational vs document models
- query-driven data modeling
- abstraction layers
- how data models shape system behavior
- trade-offs between representations
- scalability implications of modeling decisions

---

# Core Mental Model

```text
Feature
    ↓
Access Pattern
    ↓
Queries
    ↓
Data Model
    ↓
Physical Optimization
    ↓
System Behavior
```

This chapter is being studied from a systems-thinking perspective rather than a schema-first perspective.

---

# Important Concepts

## Abstraction

Data models hide lower-level storage complexity and provide cleaner ways to reason about systems.

Example:

```text
Reality
→ Application Objects
→ Tables/Documents
→ Bytes
→ Hardware Signals
```

---

## Query-Driven Modeling

Data models should not be designed in isolation.

Instead:

```text
Application behavior
→ access patterns
→ queries
→ data model design
```

---

# Mini-Twitter System

Throughout this chapter, concepts are explored using a mini-twitter-system involving:

- users
- posts
- follows
- timelines
- likes
- feeds

The goal is to analyze how different data models affect:
- query complexity
- scalability
- read/write behavior
- architectural trade-offs

---

# Planned Experiments

- relational timeline modeling
- document-based timeline modeling
- indexing experiments
- normalization vs denormalization
- query pattern analysis
- fan-out-on-read vs fan-out-on-write

---

# Key Insight

A data model is not just a database structure.

It is:
- an abstraction
- a reasoning framework
- a set of trade-offs
- a way of thinking about system behavior

# Relational Model vs Document Model

## Core Insight

Data models are abstractions that shape:
- system behavior
- query flexibility
- scalability characteristics
- engineering thinking

---

# Why NoSQL Emerged

NoSQL systems emerged due to pressures from:
- internet-scale workloads
- massive write throughput
- flexible schemas
- distributed architectures
- specialized query patterns

This was fundamentally:
```text
changing application requirements
→ new data modeling pressures
```

---

# Polyglot Persistence

Modern systems often use multiple database models simultaneously.

Example:
- PostgreSQL for transactions
- Redis for caching
- Elasticsearch for search
- Neo4j for graph traversal

Database selection should follow:
```text
workload + query pattern
```

not hype.

---

# Object-Relational Mismatch

Applications naturally model data as:
- objects
- nested structures
- hierarchies

Relational systems model data as:
- tables
- rows
- normalized relationships

This creates translation complexity.

---

# Mental Model

```text
Application Objects
≠
Relational Representation
```

---

# ORM Insight

ORMs reduce translation boilerplate but cannot fully eliminate the conceptual mismatch between objects and relations.

---

# Systems Thinking Insight

Different representations optimize different things:

| Model | Optimizes |
|---|---|
| Relational | consistency, joins, normalization |
| Document | hierarchical representation, flexibility |
| Graph | relationship traversal |
| Key-value | fast lookup |

---

# Key Takeaway

There is no universally superior data model.

The correct model depends on:
- features
- access patterns
- scalability requirements
- query behavior
