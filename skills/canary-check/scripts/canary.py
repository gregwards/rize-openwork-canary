#!/usr/bin/env python3
# Prints the canary token. Succeeds only if this script AND reference/token.txt were delivered together.
import pathlib, sys
here = pathlib.Path(__file__).resolve().parent.parent
token_file = here / "reference" / "token.txt"
if not token_file.exists(): print("CANARY FILES MISSING: token.txt not found at", token_file); sys.exit(1)
print("CANARY TOKEN:", token_file.read_text().strip())

