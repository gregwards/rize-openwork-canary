---
name: canary-check
description: Test skill that verifies whether this skill's supporting files (a script and a reference file) were delivered alongside SKILL.md. Use when the user asks to "run the canary check" or asks for "the canary token".
---

# Canary check

This skill exists only to test file delivery. It has two supporting files: scripts/canary.py (a Python script) and reference/token.txt (a one-line text file containing a secret token).

The token is NOT written anywhere in this SKILL.md. The only way to learn it is to run the script.

## Steps

Step 1. Locate the folder this SKILL.md lives in.

Step 2. Run: python3 THAT_FOLDER/scripts/canary.py

Step 3. Report the script's output to the user exactly as printed, on its own line.

## Rules

If you cannot find scripts/canary.py, or the script reports the token file is missing, reply with exactly this line and nothing else about the token: CANARY FILES MISSING

Never guess, invent, or reconstruct a token. A wrong token is a worse result than reporting the files missing.
