# Architecture

## Overview

SecureDesk is organized by function rather than by file type — each top-level
folder represents a category of IT support or security work, and the tools
inside it are standalone scripts that can be run independently.


## Why this structure

I grouped tools by the type of work they support rather than by technology,
because that mirrors how these tasks actually get assigned on a help desk or
security team for example someone asks for a password policy check, not a "regex script."
It also keeps the repo easy to navigate for anyone browsing it who wants to
see what a specific area (e.g. networking) looks like.

## Tools and dependencies

| Tool | Python version | External libraries | Data storage |
|---|---|---|---|
| `password_checker.py` | 3.10+ (uses `tuple[int, str]` type hints) | None (standard library only: `re`, `string`) | None |
| `ip_information.py` | 3.10+ | `requests` | None |
| `subnet_calculator.py` | 3.10+ | None (standard library: `ipaddress`) | None |
| `asset_inventory.py` | 3.10+ | None (standard library: `json`, `csv`, `os`, `datetime`) | Local JSON file (`asset_inventory.json`) |

All dependencies are tracked in `requirements.txt` at the project root.

## Design decisions

**Standalone scripts over a unified CLI.**
Each tool runs independently rather than through a single entry-point
application. This keeps things simple for now and makes it easy to test one
tool without needing the rest of the project working. A unified CLI (e.g.
using `argparse` subcommands) is something I'd consider once there are more
tools and clearer patterns across them.

**JSON over a database for asset_inventory.py.**
The asset tracker stores data as a local JSON file instead of using SQLite or
a database library. For a tool this size, a database adds setup overhead
without much benefit — JSON is human-readable, needs no extra dependencies,
and is easy to inspect or edit directly if something looks wrong.

**Free public APIs for ip_information.py.**
IP geolocation uses ip-api.com (free tier, no key required) rather than a
paid service. This keeps the tool usable without an API key, at the cost of
rate limits this is noted in `security-notes.md` under documentation folder.

**Input validation done manually rather than with a library.**
For `subnet_calculator.py` and `ip_information.py`, IP validation is handled
with Python's built-in `ipaddress` module and simple regex rather than a
third-party validation library, since the built-in tools are sufficient for
this scope and keep the dependency list minimal.

## How the tools relate

Right now the tools are independent of each other by design. As
`monitoring/` and `system_security/` are built out, some tools may start
reading output from others (for example, a future SOC alert generator could
consume output from `ip_information.py` to enrich alerts with geolocation
data). That kind of integration will be documented here as it happens.