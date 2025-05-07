# WRAPX CLI Interface

wrapx-cli is the reference command-line tool for interacting with `.wrapx` containers. It enables users and developers to simulate real-world wrapping workflows, apply modules, inspect metadata, and enforce policy actions without GUI or OS integration.

---

## Basic Syntax

    wrapx [command] [options] <file>

---

## Supported Commands

| Command   | Purpose                                                |
|-----------|--------------------------------------------------------|
| wrap      | Package a file into a `.wrapx` container with metadata |
| open      | Open a `.wrapx` file, validate metadata, launch payload |
| save      | Re-wrap with updates after edit, apply on_save modules |
| inspect   | View metadata, audit logs, module outputs              |
| validate  | Verify integrity, hashes, signatures, module state     |
| config    | Show or update runtime and module configuration        |

---

## wrap

    wrapx wrap report.docx --profile tactical_edge_writer

- Creates `report.docx.wrapx`
- Applies modules from profile (based on `wrapx.json`)
- Prompts for metadata (interactive or form-driven)

---

## open

    wrapx open report.docx.wrapx

- Unpacks `.wrapx`
- Validates signature chain, digest, and policies
- Opens payload in associated application

---

## save

    wrapx save report.docx.wrapx

- Applies on_save modules
- Updates `/meta/manifest.json`, `/audit/`, and other configured outputs

---

## inspect

    wrapx inspect report.docx.wrapx

- Displays metadata
- Shows audit trail, compression stats, module traces

---

## validate

    wrapx validate report.docx.wrapx

- Verifies:
  - Manifest schema
  - Module outputs (e.g., sigchain, hash)
  - Runtime compatibility
  - Integrity status

---

## config

    wrapx config --show-defaults

- Displays system-wide defaults for module paths, logging, fallback policies

---

## Example Wrap Flow

    wrapx wrap missionplan.pptx --profile edge_chain
    wrapx open missionplan.pptx.wrapx
    wrapx save missionplan.pptx.wrapx
    wrapx inspect missionplan.pptx.wrapx

---

## Module Execution

- Modules are triggered per `wrapx.json`
- CLI logs all module input/output in `/audit/cli-run.log`
- Support for module debug mode: `--verbose`

---

## Planned Extensions

- Interactive mode: step through wrap/save workflows
- Upload audit trail or metadata for remote validation
- Signature authority integration (e.g., `wrapx sign --tsa`)
- `wrapx diff`: compare manifest or audit between two files

---

## Platform Notes

- Compatible with Windows CMD/PowerShell, Bash, Zsh
- Python or Go reference implementation (TBD)
- Designed for CLI-first deployment in DDIL or headless environments
