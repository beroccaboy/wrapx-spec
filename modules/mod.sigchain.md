# Module: mod.sigchain

**Purpose**:  
Ensures tamper-evident integrity for metadata, audit logs, or other module outputs using cryptographically chained signatures. This is critical for disconnected operations where centralised trust anchors may not be available.

---

## Supported Triggers

- `on_save`: Sign and seal current state
- `on_close`: Append closing hash/signature to chain
- `on_open`: Verify signature chain (optional)

---

## Parameters (via `wrapx.json`)

```json
{
  "name": "mod.sigchain",
  "trigger": "on_close",
  "params": {
    "target": ["/meta/manifest.json", "/audit/accesslog.json", "/meta/hash.json"],
    "key_id": "default_signing_key",
    "chain_to": "/meta/sigchain.json"
  }
}
