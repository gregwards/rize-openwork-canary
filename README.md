# rize-openwork-canary

A throwaway plugin for one question: when a skill is delivered to a teammate through the OpenWork marketplace, do its scripts and reference files arrive, or only SKILL.md?

Contains no Rize material.

## The check

Step 1. In OpenWork (as org admin), preview a GitHub import of this repo into the marketplace and read the omitted-assets list. Note whether scripts/canary.py and reference/token.txt are listed as omitted.

Step 2. Publish it to the marketplace and grant access.

Step 3. On a machine or account with NO local copy of this skill, start a fresh OpenWork session and say: Run the canary check and give me the token.

Step 4. Compare the reply to skills/canary-check/reference/token.txt.

Exact token means the files were delivered. CANARY FILES MISSING means only SKILL.md was delivered. Any other token means the agent hallucinated; treat as a fail.
