# New Work — CLM Kafka Phoenix Retry Library & Kafka Observability

## CLM Kafka Phoenix Retry Library

### What it is
A reusable Spring Boot library providing cluster-safe, exponential backoff retry mechanism for both producer and consumer Kafka messages. Handles message processing failures without hammering external services or writing custom retry logic.

### How it Works
The library intercepts Kafka failures from two primary sources:
- **Consumer Failures** — via a global error channel (@ServiceActivator) that catches exceptions from any @KafkaListener
- **Producer Failures** — via a matched and paired configuration patterns

In failed cases:
1. The failed message's topic is matched against configured retry patterns
2. A retry record (including original header, retry count) is stored in a database table (kafka_message_database table)
3. A single, cluster-safe scheduler (distributed lock + scheduled task) periodically scans the retry table
4. Records are retried based on exponential backoff algorithm
5. The library invokes the correct RetryMessageHandler Spring bean to re-process the message

### Key Features
- **Auto-Configurable** — enable with single property (`clm.kafka.retry.enabled=true`)
- **Exponential Backoff** — automatically increases delay between retries to avoid overwhelming downstream systems (e.g., 5m → 10m → 20m → 40m...)
- **Exception-Aware & Topic-Specific Policies** — configure global or topic-specific retry policies based on exception thrown during message processing
- **Pluggable Architecture** — provides implementation for fetching data and processing it, library handles the orchestration
- **Producer-Retry Logic** — handles both producer and consumer failures
- **Topic-to-Handler Mapping** — automatically maps topics to specific handler beans using application.yml
- **Cluster Safe** — uses distributed lock to ensure only one instance of the scheduler runs in multi-node environments
- **Configurable Controls** — max retries, backoff time, handler mappings all via yml
- **Direct Logic Invocation** — retries call Java business logic directly, not by re-publishing to Kafka

### Business Impact
- **Before:** Failed messages sitting in database with no automated retry, daily lags in state/validity calculation, users waiting 30-60 minutes for shopping list calculation results
- **After:** 500,000 messages processed efficiently per day, everything happens within seconds
- Reduced failed messages sitting in database
- Eliminated daily Kafka lag in state calculation/validity calculation
- Dramatically improved user experience — no more waiting

### Scope of Impact
- **Business unit level initiative (dbCLM)** — not just project/team level
- Multiple teams across dbCLM are using this library
- Component Guardian of Kafka — responsible for Kafka across teams

---

## Kafka Spring Cloud Stream Library

Introduced new Kafka library using Spring Cloud Stream which helped:
- Reduce lags efficiently
- Process 500,000 messages per day in state validation
- Before: daily lags in state/validity calculation delaying shopping list calculation
- After: everything processed within seconds

---

## Kafka Messages Observability

### What it is
Introduced full lifecycle observability/tracing for Kafka messages in both the old library and the new library.

### Business Impact
- **Before:** No way to trace Kafka message lifecycle in production, no visibility into message flow
- **After:** Full end-to-end traceability of every Kafka message
- Helped find bugs in production that were previously undetectable
- Full tracing capability for debugging and audit

### ECDF Mapping

| ECDF Dimension | How This Maps |
|---|---|
| **Thinks** | Identified the gap in Kafka reliability and observability, designed innovative solution |
| **Designs** | Architected reusable library with pluggable architecture, exponential backoff, cluster-safe scheduling |
| **Delivers** | Built and shipped library used across dbCLM business unit |
| **Operates** | Kafka observability — full message lifecycle tracing, production bug detection |
| **Controls** | Cluster-safe distributed locking, configurable retry policies, audit trail |
| **Influences** | Drove adoption across multiple teams at business unit level |
| **Achieves** | 30-60 min wait → seconds, 500K msgs/day, eliminated daily Kafka lags |
| **Engages** | Collaborated with multiple teams for adoption and integration |

### Panel Feedback Addressed

| Feedback Gap | How This Addresses It |
|---|---|
| "Show business impact in simple terms" | Users waited 30-60 mins, now get results in seconds |
| "Firmwide/division contribution weak" | Used by multiple teams across entire dbCLM business unit |
| "Show solution design ownership" | Designed and built this library from scratch |
| "Leadership beyond your team" | Component Guardian of Kafka, teams depend on this library |
| "Show cooperation" | Collaborated with multiple teams for adoption |

---

## Screenshots Reference
- Kafka Phoenix Retry Library: framework/IMG_3483.jpg, IMG_3484.jpg
