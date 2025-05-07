# Module: mod.compress

**Purpose**:  
Applies compression to the payload within a `.wrapx` container to reduce storage size and optimise bandwidth for edge, tactical, or disconnected environments.

---

## Supported Triggers

- `on_save`: Compress payload after edits
- `on_close`: Repack container with compression
- `on_open`: Decompress payload before launch

---

## Parameters (via `wrapx.json`)

```json
{
  "name": "mod.compress",
  "trigger": "on_save",
  "params": {
    "method": "zstd",
    "level": 5,
    "target": "/payload/file.docx"
  }
}
