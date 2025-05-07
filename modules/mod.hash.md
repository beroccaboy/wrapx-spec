# Module: mod.hash

**Purpose**:  
Calculates and stores a checksum of the payload file to detect unauthorized modifications, support forensic comparison, or verify data integrity across disconnected systems.

---

## Supported Triggers

- `on_save`: Hash the saved payload
- `on_open`: Verify hash matches previous value (if present)
- `on_close`: Optionally re-verify or update hash

---

## Parameters (via `wrapx.json`)

```json
{
  "name": "mod.hash",
  "trigger": "on_save",
  "params": {
    "digest": "SHA-512",
    "store_to": "/meta/hash.json"
  }
}
