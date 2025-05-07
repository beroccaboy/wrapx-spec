# WRAPX Specification

**WRAPX** is a universal file wrapper format — like ZIP, but metadata-native. It’s designed to let files carry their own context: classification, tags, policies, audit info — and survive across systems, networks, and workflows.

WRAPX makes files self-describing, policy-aware, and portable — even in disconnected, zero-trust, or legacy environments.

---

## 🌍 What It Does

- Wraps any file (Word, Excel, PDF, images, etc.)
- Binds metadata and policies directly to the file
- Works transparently with your existing apps
- Hooks into open/save/rename operations
- Supports modules for encryption, audit, compression, and more
- Runs on Windows, macOS, Linux — mobile (Android) support planned

---

## 🧩 Modular by Design

WRAPX supports a plug-in architecture. That means:

- You can **orchestrate your own file workflows**
- Vendors (e.g. Oracle, Red Hat) can publish modules for:
  - Encryption (`mod.encrypt`)
  - Checksum validation (`mod.hash`)
  - Audit trail (`mod.audit`)
  - Tactical edge enforcement (`mod.edge`)
  - Compression (`mod.compress`)
- The base runtime is free and open. Modules are opt-in.

---

## 💡 Why It Exists

Metadata shouldn't get lost when you hit “Save As.”

WRAPX is for:
- Architects who want **data-centricity**
- Operators who work in **disconnected or DDIL conditions**
- Organisations implementing **zero trust at the file level**
- Anyone who’s sick of rebuilding metadata pipelines or managing sidecar files

---

## 📄 Example

```bash
wrapx.zip
│
├── /payload/          # The actual file (e.g. report.docx)
│   └── file.docx
│
├── /meta/             # Metadata (classification, tags, etc.)
│   └── manifest.json
│
├── /policy/           # Optional: TTLs, caveats, role rules
│   └── policy.json
│
├── /signature/        # Optional: digital signature block
│   └── sigblock.sig
│
└── /audit/            # Optional: access logs, chain of custody
    └── accesslog.json
