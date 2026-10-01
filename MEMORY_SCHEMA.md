# Memory schema

A durable memory record should ideally contain:

- `id`
- `topic`
- `content`
- `source`
- `created_at`
- `updated_at`
- `confidence`
- `status` (fact, observation, hypothesis, decision)
- `links`

The schema is deliberately simple so it can be implemented in Markdown, SQL, JSON, or a vector store.
