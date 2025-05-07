#!/usr/bin/env python3

import argparse
import json
import os
import sys
from pathlib import Path

VERSION = "0.1"

def load_wrapx_config(config_path="examples/wrapx.json"):
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"[ERROR] Failed to load wrapx.json: {e}")
        sys.exit(1)

def wrap(file, profile):
    print(f"[wrapx] Wrapping {file} using profile '{profile}'")
    config = load_wrapx_config()
    for module in config.get("modules", []):
        print(f" - [TRIGGER: {module['trigger']}] Running module: {module['name']} with params {module.get('params', {})}")
    print(f"[wrapx] Created {file}.wrapx (simulated)")

def open_wrapx(file):
    print(f"[wrapx] Opening {file}")
    # You could unpack a .zip here in a real version
    print(" - Validating manifest...")
    print(" - Running on_open modules...")
    print(" - Launching payload in native app (simulated)")

def save(file):
    print(f"[wrapx] Saving updates to {file}")
    print(" - Running on_save modules...")

def inspect(file):
    print(f"[wrapx] Inspecting {file}")
    print(" - Reading manifest, metadata, and logs (simulated)")
    print(" - Detected modules: mod.audit, mod.hash, mod.sigchain, mod.compress, mod.encrypt")

def validate(file):
    print(f"[wrapx] Validating {file}")
    print(" - Checking manifest schema")
    print(" - Verifying digests and signatures (simulated)")
    print(" - Module state: OK")

def config():
    print("[wrapx] Showing default runtime configuration:")
    print(" - wrapx.json path: ./examples/wrapx.json")
    print(" - Module root: ./modules")
    print(" - Output logs: ./runtime/")

def main():
    parser = argparse.ArgumentParser(description="WRAPX Runtime CLI")
    parser.add_argument("command", help="Command to run (wrap, open, save, inspect, validate, config)")
    parser.add_argument("file", nargs="?", help="Target file (optional for some commands)")
    parser.add_argument("--profile", help="Workflow profile name (for wrap)")

    args = parser.parse_args()

    match args.command:
        case "wrap":
            if not args.file or not args.profile:
                print("[ERROR] wrap requires a file and --profile")
                sys.exit(1)
            wrap(args.file, args.profile)
        case "open":
            if not args.file:
                print("[ERROR] open requires a file")
                sys.exit(1)
            open_wrapx(args.file)
        case "save":
            if not args.file:
                print("[ERROR] save requires a file")
                sys.exit(1)
            save(args.file)
        case "inspect":
            if not args.file:
                print("[ERROR] inspect requires a file")
                sys.exit(1)
            inspect(args.file)
        case "validate":
            if not args.file:
                print("[ERROR] validate requires a file")
                sys.exit(1)
            validate(args.file)
        case "config":
            config()
        case _:
            print(f"[ERROR] Unknown command: {args.command}")
            parser.print_help()

if __name__ == "__main__":
    main()
