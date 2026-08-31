# Security Notes

This file documents the security reasoning behind each tool, along with
known limitations. The goal is to be upfront about what each tool does and
doesn't protect against — a script that "checks passwords" isn't useful if
you don't know what it's actually checking for.

## password_checker.py

**What it checks and why:**
- Length and character variety, because these are the baseline factors most
  password policies are built around (NIST and most corporate policies
  reference both).
- Repeated characters and sequential patterns (e.g. `1234`, `aaa`), because
  these pass basic length/variety checks but are still weak in practice for example
  a password like `Aaaa1111!` scores well on variety alone but is trivial
  to guess.
- A small hardcoded list of common passwords, to catch the most obvious
  weak choices. This is not a substitute for checking against a real breach
  database.

**Limitations:**
- The common-password list is a small sample, not a comprehensive breach
  database. A production tool would check against something like the
  Have I Been Pwned Pwned Passwords API.
- This tool only rates password strength — it doesn't check whether a
  password has actually appeared in a known breach.
- Entered passwords are not logged or stored anywhere by this script, but
  since input happens via a plain terminal prompt, anyone running it should
  be mindful of shoulder-surfing in the same way as any password entry.

## ip_information.py

**What it checks and why:**
- Basic IP format validation before making any external request, to avoid
  sending malformed input to the API and to catch typos early.
- Geolocation and ISP lookups via a free public API, useful for quickly
  contextualizing a suspicious IP during triage (e.g. "is this login from
  the expected country?").

**Limitations:**
- Relies on a free third-party service (ip-api.com) with rate limits —
  not suitable for high-volume or production use without a paid tier or a
  self-hosted alternative.
- Geolocation data from any IP lookup service is approximate and can be
  inaccurate, especially for VPNs, proxies, or mobile carriers. It should be
  treated as a starting point for investigation, not definitive proof of a
  user's location.
- No caching is implemented, so repeated lookups of the same IP will hit
  the API each time.

## subnet_calculator.py

**What it checks and why:**
- Accepts both CIDR notation and full subnet masks, and validates input
  using Python's `ipaddress` module rather than custom parsing, to avoid
  reinventing (and possibly getting wrong) IP validation logic.

**Limitations:**
- IPv4 only — no IPv6 support yet.
- Purely a calculation tool; it doesn't verify that a subnet is actually
  reachable or correctly configured on a real network.

## asset_inventory.py

**What it checks and why:**
- Stores asset records locally with basic required fields (ID, type,
  assignee, location, status) to mirror what a lightweight asset tracker
  needs for a small environment.

**Limitations:**
- Data is stored unencrypted in a local JSON file
  (`asset_inventory.json`). This is fine for a demo/portfolio tool, but not
  appropriate for real sensitive asset data without adding encryption at
  rest or moving to a proper database with access controls.
- No authentication or access control — anyone with access to the machine
  can view or edit the inventory file directly.
- Not designed for concurrent multi-user use; it's a single-user CLI tool.

## General practices followed across this project

- No hardcoded credentials, API keys, or secrets anywhere in the codebase.
- `.gitignore` excludes generated data files (e.g. `asset_inventory.json`,
  CSV exports) and environment files (`.env`) so nothing sensitive or
  machine-specific gets committed by accident.
- User input is validated before use (IP format checks, non-empty checks)
  rather than trusted blindly.
- External API calls include timeouts and error handling, so a failed or
  slow request doesn't hang the tool indefinitely.