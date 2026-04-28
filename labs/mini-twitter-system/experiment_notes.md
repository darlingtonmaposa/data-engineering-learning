# 🧪 Experiment Notes — Timeline System

---

## 🧠 Purpose

This document explores how timeline generation behaves under different system designs.

We are comparing:

- Fan-out-on-Read (compute timeline at read time)
- Fan-out-on-Write (precompute timeline at write time)

Goal:

> Understand how design choices affect performance, scalability, and system behavior.

---

## ⚙️ System Designs

### Fan-out-on-Read

- Timeline generated using queries
- No data duplication
- Work happens at read time

---

### Fan-out-on-Write

- Timeline precomputed and stored
- Data duplicated across followers
- Work happens at write time

---

## 🧪 How Experiments Are Structured

Each experiment follows:

1. Hypothesis — What we expect
2. Setup — System state
3. Execution — What we run
4. Observation — What happens
5. Analysis — Why it happens
6. Insight — What we learn

---

# 🔬 Experiments

---

## Experiment 1 — Read Cost Scaling

### Hypothesis

As the number of followees increases, read queries become slower.

---

### Setup

User follows increasing number of users.

---

### Execution

Run timeline query using JOIN and filtering.

---

### Observation

- Query becomes slower
- More rows processed

---

### Analysis

- Query recomputes timeline each time
- Cost grows with data size

---

### Insight

> Fan-out-on-read shifts cost to reads.

---

## Experiment 2 — Write Amplification

### Hypothesis

Posting by a high-follower user results in many writes.

---

### Setup

User with many followers creates a post.

---

### Execution

Insert post into all follower timelines.

---

### Observation

- Number of writes increases with followers
- Write latency increases

---

### Analysis

- One logical write becomes many physical writes

---

### Insight

> Fan-out-on-write shifts cost to writes.

---

## Experiment 3 — Read Performance Stability

### Insight

> Precomputation simplifies reads and improves consistency.

---

## Experiment 4 — Sparse Graph

### Insight

> System cost depends on graph structure.

---

## Experiment 5 — Worst Case

### Insight

> High-follower users create system hotspots.

---

# ⚠️ Failure Modes

## Fan-out-on-Read

- Slow queries
- High read load
- Repeated computation

---

## Fan-out-on-Write

- Write amplification
- Hotspots
- Storage growth

---

# ⚖️ Trade-offs

| Aspect | Fan-out-on-Read | Fan-out-on-Write |
|--------|----------------|------------------|
| Reads  | Expensive      | Cheap            |
| Writes | Cheap          | Expensive        |
| Storage| Low            | High             |

---

# 🧠 Key Takeaways

1. You cannot eliminate cost — only move it
2. Data model determines system behavior
3. Real-world usage patterns shape performance

---

# 🔗 Real-World Implication

This leads to:

- Hybrid architectures
- Async processing
- Caching strategies

---

# 📌 Final Thought

> Systems are not defined by code.  
> They are defined by **data flow and trade-offs**.

---
