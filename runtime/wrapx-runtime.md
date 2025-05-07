# WRAPX Runtime Specification

The WRAPX Runtime is a lightweight enforcement layer that handles metadata updates, module execution, and file system hooks associated with `.wrapx` files.

---

## 1. Responsibilities

- Mount and unpack `.wrapx` containers
- Interpret `wrapx.json` workflow profiles
- Load and execute modules on defined triggers (e.g., on_save)
- Pass the original file to native applications (e.g., Word, Excel)
- Update metadata on save, rename, or close events
- Optionally show metadata overlays or classification banners

---

## 2. Runtime Triggers

Supported triggers (defined in `wrapx.json`):

- `on_open` – triggered before the file is passed to the native application
- `on_save` – triggered after the user saves the file
- `on_close` – triggered after application exit
- `on_rename` – triggered if the file name changes
- `on_copy` – optional future trigger

Each trigger can chain multiple modules.

---

## 3. Metadata Update Workflow

1. On open:
   - Load manifest and `wrapx.json`
   - Apply any `on_open` modules
   - Inject visible classification banner (if configured)

2. On save:
   - Run `on_save` modules (e.g., checksum, encryption)
   - Prompt user for new metadata if required
   - Repack `.wrapx` structure with updated `/meta/manifest.json`

3. On close:
   - Run `on_close` modules (e.g., summarise, log to audit)
   - Seal the container and clean up any temp artefacts

---

## 4. Module Loading

Modules can be:
- Native shell extensions
- Runtime scripts (Python, PowerShell, Bash)
- Binary executables (with stdin/out contract)
- Dockerized microservices (TBD)

Modules must declare:
- Name
- Supported triggers
- Parameter schema
- Return codes (success, error, skip, etc.)

---

## 5. Shell Integration

- On double-click:
  - Runtime opens `.wrapx`, runs `on_open` modules, then passes payload to the native app
- On save
