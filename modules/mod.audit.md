# Module: mod.audit

**Purpose**:  
Captures access, usage, and modification events for `.wrapx` files and records them in a tamper-evident audit log. This module is critical for compliance, forensic analysis, DDIL operations, and cross-domain accountability.

---

## Supported Triggers

- `on_open`: Log access event with timestamp, user ID (if known), and environment context
- `on_save`: Log modification event with hash diff (if enabled)
- `on_close`: Log session duration and close reason
- `on_copy` (planned): Log duplication and path

---

## Parameters (via `wrapx.json`)

```json
{
  "name": "mod.audit",
  "trigger": "on_open",
  "params": {
    "log_to": "/audit/accesslog.json",
    "append_only": true,
    "hash_payload": true
  }
}
