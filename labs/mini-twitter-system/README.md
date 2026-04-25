# Mini Twitter System — Data Engineering Lab

## Overview

This project models a simplified social media system to explore **data modeling**, **query design**, and **read/write tradeoffs** in data systems.

The focus is not on building a full application, but on understanding how **data structures determine system behavior**.

Core feature implemented:
- User timelines (home feed)

Two architectures are explored:
- **Fan-out-on-read** (compute timeline at query time)
- **Fan-out-on-write** (precompute timeline at write time)

---

## Objectives

This lab is designed to build intuition for:

- Structuring data to represent real-world relationships
- Designing queries that drive application behavior
- Understanding **read vs write tradeoffs**
- Working with **derived state (precomputed data)**
- Thinking in terms of **systems, not just code**

---

## System Architecture

The system consists of three main layers:

### 1. Application Layer
- Python services
- Responsible for orchestrating reads and writes

### 2. Data Layer
- PostgreSQL database
- Stores system state and relationships

### 3. Interface Layer
- CLI-based execution (via Python scripts)
- Direct SQL inspection via `psql`

---

## Data Model

The system is built around four core tables:

| Table     | Purpose                                      |
|----------|----------------------------------------------|
| `users`   | Stores user identities                       |
| `posts`   | Stores user-generated content                |
| `follows` | Models the social graph (who follows who)    |
| `timeline`| Stores precomputed feed entries              |

---

## Timeline Architectures

### 1. Fan-out-on-read

**Approach:**
- Timeline is computed at query time
- Posts are fetched dynamically based on follow relationships

**Characteristics:**
- Cheap writes
- Expensive reads
- No duplication of feed data

---

### 2. Fan-out-on-write

**Approach:**
- Timeline entries are created when a post is written
- Each follower receives a feed entry

**Characteristics:**
- Expensive writes
- Cheap reads
- Introduces **derived state**

---

## Key Tradeoff

This project demonstrates a fundamental system design tradeoff:

> “Do we compute results when needed, or store them in advance?”

| Strategy            | Write Cost | Read Cost | Storage |
|--------------------|-----------|----------|--------|
| Fan-out-on-read     | Low       | High     | Low    |
| Fan-out-on-write    | High      | Low      | Higher |

---

## Repository Structure
mini-twitter-system/
│
├── README.md
├── sql/
│ ├── schema.sql
│ └── seed.sql
│
├── app/
│ ├── db.py
│ ├── main.py
│ └── services/
│ ├── users.py
│ ├── posts.py
│ ├── follows.py
│ └── timeline.py
│
└── images/
└── architecture.png


---

## Setup

### 1. Start PostgreSQL

Ensure PostgreSQL is running and accessible.

### 2. Apply schema

```bash
psql -U postgres -h <host-ip> -p 5432 -d mini_twitter -f sql/schema.sql


## Running the Project
Execute the main script:
This runs test flows such as:

- user creation
- post creation
- follow relationships
- timeline retrieval

## Observability
Inspect database state directly:
`psql -U postgres -h <host-ip> -p 5432 -d mini_twitter`

## Failure Modes
Introducing fan-out-on-write adds complexity:

- Partial fan-out (some followers receive entries, others don’t)
- Duplicate entries (guarded by constraints)
- Timeline inconsistency with source data
- Increased write amplification

This highlights a key principle:

*Derived data must be carefully maintained.*

## Key Learnings
- Data models define system capabilities
- Queries define application behavior
- Performance is a consequence of design choices
- Precomputation trades storage and write cost for read efficiency
- Systems become more complex as optimization increases


## Future Improvements
- Pagination for timelines
- Indexing strategies for performance
- Handling high-follower users (celebrity problem)
- Background jobs for asynchronous fan-out
-Event-driven architecture (Kafka-style)

## References
- Designing Data-Intensive Applications (DDIA)
- Real-world social feed architectures (Twitter, Facebook)

## Author
Darlington Maposa
Data Engineering Lab Series
