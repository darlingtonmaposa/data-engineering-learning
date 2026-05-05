# 🐦 Mini Twitter System  
## Timeline Architecture & Data Model Trade-off Exploration

> A systems-first data engineering lab that explores how **data models and query patterns shape system behavior at scale**.

---

![Cover](images/cover.png)

---

# 🧭 1. Why This Project Exists

Most data engineering projects answer:

> “Can you build a pipeline?”

This project answers a deeper question:

> **“Do you understand how systems behave under different data modeling choices?”**

---

## The Core Idea

This project is built around a fundamental systems principle:

**Data Model → Query Pattern → System Behavior → Trade-offs → Scaling Limits**

---

# 🧠 2. Problem Statement

We model a simplified social system:

- Users follow other users  
- Users create posts  
- Each user retrieves a **timeline (feed)**  

At small scale, this is trivial.

At large scale, it becomes a **distributed systems problem**.

---

## The Real Question

> **Where should the cost of generating timelines live?**

---

# ⚖️ 3. The Core Trade-off

## 🟦 Fan-out-on-Read (Compute on Demand)

**Read Path:**
- User requests timeline  
- System queries posts from followees  
- Results are sorted and returned  

### Characteristics
- No data duplication  
- Heavy read queries (joins + sorting)  
- Cheap writes  

---

## 🟥 Fan-out-on-Write (Precompute Timeline)

**Write Path:**
- User creates post  
- System distributes post to followers  
- Timeline is stored ahead of time  

### Characteristics
- Data duplication  
- Expensive writes  
- Extremely fast reads  

---

## 🔑 Key Insight

> You are not choosing an implementation.  
> You are choosing **where the system pays the cost**.

---

# 🏗️ 4. System Architecture

![Architecture](images/architecture.png)

---

## System Layers

### Layer 1 — Data Model (State)
- Users
- Posts
- Social graph (follows)
- Timeline (optional, precomputed)

---

### Layer 2 — Query Patterns (Access)
- “Get posts from users I follow”
- “Insert post”
- “Distribute post to followers”

---

### Layer 3 — System Behavior (Emergent)
- Read latency
- Write amplification
- Storage growth
- Load distribution

---

# 🧪 5. Experiments (Core of This Project)

> The code is not the product.  
> **The experiments and observations are the product.**

---

## What This Project Explores

- Read vs write amplification  
- Query complexity vs data duplication  
- Impact of follower count distribution  
- Performance implications of different designs  

---

## Where to Find Results

👉 Full analysis: [`experiment_notes.md`](experiment_notes.md)

---

## Example Observations

### Fan-out-on-Read
- Scales poorly under heavy read load  
- Simpler system (fewer moving parts)  

---

### Fan-out-on-Write
- Write amplification for users with many followers  
- Introduces uneven load and hotspots  

---

## Senior-Level Insight

> Systems fail where **pressure accumulates**.

---

# 🗃️ 6. Data Model

## Core Tables

- `users` → system users  
- `posts` → content created by users  
- `follows` → social graph (who follows who)  
- `timeline` → precomputed feed (fan-out-on-write)  

---

## Key Relationships

- One user → many posts  
- Many users ↔ many users (follows)  
- One post → many timeline entries  

---

## Critical Observation

> The `timeline` table is not required.  
> It exists only because of a **query optimization decision**.

---

# 📦 7. Project Structure

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

## Structure Philosophy

| Layer | Responsibility |
|------|---------------|
| SQL | Defines system state |
| App | Executes behavior |
| Experiments | Captures system insights |

---
## ⚠️ Failure Modes (Preview)

Each design introduces different system risks:

- **Fan-out-on-read**
  - Slow timeline queries
  - High read load under traffic spikes

- **Fan-out-on-write**
  - Write amplification for high-follower users
  - Hotspots and uneven load distribution

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

`psql -U postgres -d mini_twitter -f sql/schema.sql`<br>
`psql -U postgres -d mini_twitter -f sql/seed.sql`

### 3. Run Application
`python app/main.py`


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
