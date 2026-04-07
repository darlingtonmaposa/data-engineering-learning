#  Scalability 

Scalability refers to a system's ability to handle increased load.

Even if a system works reliably today, growth in users or data volume may cause performance degradation.

## Examples of Load Growth

- concurrent users increasing (10,000 → 100,000)
- data volume increasing (1 million → 10 million records)

## Key Idea

Scalability is not a fixed attribute of a system.

Instead, engineers must consider how systems can handle growth by adding resources.

Typical questions include:

- How will the system behave under increased load?
- What options exist for adding computing resources?

## Describing Load

Before discussing scalability, engineers must understand the system's load.

Load is described using **load parameters**, such as:

- requests per second
- read/write ratio
- number of active users
- cache hit rate

### Twitter Example

Twitter handles two main operations:

Post tweet  
~4.6k tweets/sec average  
~12k tweets/sec peak

Read home timeline  
~300k requests/sec

Because reads greatly exceed writes, Twitter optimized for fast reads.

### Fan-Out

A tweet must be delivered to followers.

Example:

4.6k tweets/sec × 75 followers ≈ 345k timeline updates/sec.

### Architectural Approaches

**Fan-out on read**

- compute timeline when user requests it
- cheap writes but expensive reads

**Fan-out on write**

- precompute timelines when tweets are posted
- expensive writes but fast reads

### Hybrid Approach

Twitter uses a hybrid model:

- normal users → fan-out on write
- celebrities → fan-out on read

# Describing Performance

Understanding system scalability requires analyzing both workload and performance behavior.

## 1. Load Parameters

Load parameters describe the demand placed on a system.

Examples include:

- Requests per second
- Read/write ratio
- Concurrent users
- Data size
- Cache hit rate
- Fan-out

Example (Twitter):
- Tweet posting: ~4.6k writes/sec
- Timeline reads: ~300k reads/sec

---

## 2. Performance Metrics

Performance metrics describe how well a system handles the workload.

### Throughput

Amount of work processed per unit time.

Examples:
- records/sec
- transactions/sec

Used primarily in batch processing systems.

---

### Response Time

Time between a client sending a request and receiving a response.

Response time includes:

response time = latency + service time

---

### Latency

Latency refers to the waiting time before processing begins.

---

## 3. Response Time Distribution

Response time varies due to system and network factors.

Examples:
- network delays
- disk reads
- CPU scheduling
- garbage collection

Therefore, response time must be treated as a distribution.

---

## 4. Percentiles

Percentiles describe response time distributions.

Common metrics:

- p50 (median)
- p95
- p99
- p999

Example:

p50 = 200 ms  
p95 = 600 ms  
p99 = 1.5 s

---

## 5. Tail Latency

High percentiles represent slow outliers and are known as tail latencies.

These strongly impact user experience.

---

## 6. Queueing Effects

Servers can process only a limited number of requests in parallel.

Slow requests can delay others in the queue.

This is called head-of-line blocking.

---

## 7. Performance Testing

Load testing should generate requests independently of response times.

Waiting for each response before sending the next request leads to unrealistic results.
