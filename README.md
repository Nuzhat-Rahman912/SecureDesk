# IT Support & Cybersecurity Toolkit

A collection of practical scripts and tools built to demonstrate core
IT support and cybersecurity fundamentals — password auditing, network
diagnostics, log analysis, and basic web security checks.

## Structure

- `helpdesk/` — everyday IT support utilities (password checking, IP info, subnetting)
- `system_security/` — system auditing and file integrity tools
- `networking/` — network diagnostics and packet analysis
- `web_security/` — web vulnerability demos and header checks
- `monitoring/` — log analysis and SOC-style alerting
- `documentation/` — architecture notes, security notes, incident response guide

## Tools

| Tool | Description | Status |
|---|---|---|
| `helpdesk/password_checker.py` | Evaluates password strength and flags weak patterns | ✅ Complete |
| `helpdesk/ip_information.py` | Looks up geolocation/network info for an IP address | ✅ Complete |
| `helpdesk/subnet_calculator.py` | Calculates subnet details from CIDR or subnet mask | ✅ Complete |
| `helpdesk/asset_inventory.py` | Simple CLI tool to track IT assets, with CSV export | ✅ Complete |

## How to run

Each script is standalone. Example:

```bash
cd helpdesk
python password_checker.py
```

## Why this project

Built to practice and demonstrate real-world IT support and security
skills: scripting, network fundamentals, log/alert analysis, and secure
coding practices.