# 🐦 Mini Twitter System — Timeline Architecture Exploration

> A data engineering lab exploring timeline architectures and read/write tradeoffs in data systems.

![Cover](images/cover.png)

---

## 🧭 Overview

This project is a simplified Twitter-like system built to explore a fundamental distributed systems question:

> **How should a timeline be generated at scale?**

Specifically:

- Should timelines be **computed on demand (fan-out-on-read)**?
- Or **precomputed at write time (fan-out-on-write)**?

This project is not about features.

It is about understanding how **data models and query patterns shape system behavior**.

---

## 🧠 Problem Statement

In a social system:

- Users follow other users
- Users create posts
- Each user expects a **timeline (feed)** of posts from people they follow

At small scale, this is simple.

At large scale, it becomes a **systems design problem**.

---

## ⚖️ The Core Trade-off

We explore two competing approaches:

### 🟦 Fan-out-on-Read (Compute on Demand)

- Timeline generated when the user requests it
- Data is not duplicated
- Heavy read queries (joins, filtering, sorting)

### 🟥 Fan-out-on-Write (Precompute)

- Timeline generated when a post is created
- Data is duplicated into follower timelines
- Writes become expensive, reads become fast

---


## 🏗️ System Architecture (High-Level)

![Architecture](images/architecture.png)

---
---

## 🔬 What This Project Explores

This repository investigates:

- Read vs write amplification
- Query complexity vs data duplication
- Impact of social graph structure (followers/followees)
- Performance implications of different designs

---

## 🧪 Experiments (Core of This Project)

The most important part of this project is not the code.

It is the **experiments and observations**.

👉 **Read the full experiment analysis here:**

➡️ [`experiment_notes.md`](experiment_notes.md)

Inside, you will find:

- Structured experiments
- Hypotheses and observations
- System-level insights
- Trade-off analysis 
---

## 📦 Project Structure

```
mini-twitter-system /
├── README.md
├── app
│   ├── db.py
│   ├── main.py
│   └── services
├── experiment_notes.md
├── requirements.txt
└── sql
    ├── schema.sql
    └── seed.sql
└── images
```


### Structure Overview

- **`sql/`**  
  Contains database definitions and seed data  
  - `schema.sql` → database schema (tables, constraints)  
  - `seed.sql` → sample data for testing  

- **`app/`**  
  Application logic for interacting with the database  
  - `db.py` → database connection management  
  - `main.py` → entry point for running the system  
  - `services/` → domain logic (users, posts, follows, timeline)  

- **`experiment_notes.md`**  
  Observations and findings from comparing timeline strategies  

- **`requirements.txt`**  
  Python dependencies  


---

## ⚙️ Data Model

Core tables:

- `users` → system users
- `posts` → content created by users
- `follows` → social graph (who follows who)
- `timeline` → precomputed feed (fan-out-on-write)

---

## 🧠 Key Engineering Insights

From this project:

- **Data model + query pattern = system behavior**
- There is no “best” architecture — only trade-offs
- Systems shift cost between:
  - reads
  - writes
  - storage
- Real-world performance depends on:
  - user behavior
  - graph structure
  - access patterns

---

## 🔗 Mapping to Distributed Systems Concepts

This project connects directly to concepts from:

- Scalability
- Reliability
- Maintainability
- Trade-offs in system design

---

## 🚀 How to Run

### 1. Environment

- WSL (Linux)
- Python
- PostgreSQL

---

### 2. Setup Database

psql -U postgres -d mini_twitter -f sql/schema.sql
psql -U postgres -d mini_twitter -f sql/seed.sql

### 3. Run Application
python app/main.py


## 🔍 What To Look For When Running
- How timeline queries behave as data grows
- Difference between:
  - dynamic timeline generation
  - precomputed timeline
- Cost of writes vs reads

## Why This Project Matters
This is a toy system with real-world implications.
The same trade-offs explored here appear in:
- Social media feeds
- Notification systems
- Event-driven architectures
- Data pipelines

## 🧭 Next Steps (Future Work)
- Introduce async fan-out using queues
- Simulate high follower counts
- Add performance measurements (latency)
- Explore hybrid approaches

📎 Final Thought

|  You don’t start by designing features.
|  You start by designing data models and access patterns.

Everything else emerges from that.

## References
- Designing Data-Intensive Applications (DDIA)
- Real-world social feed architectures (Twitter, Facebook)

## Author
Darlington Maposa
Data Engineering Lab Series
