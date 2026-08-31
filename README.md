# SecureDesk

A set of Python tools I built to practice core IT support and cybersecurity skills, the kind of day-to-day work a help desk or junior security role may actually involve: checking password strength, looking up IP info, calculating subnets, and keeping track of assets.

I started this project to get hands-on with problems I'd likely run into on the job, rather than just reading about them. Each tool is small and focused, and I'm adding new ones as I build out more of the toolkit.

## What's in here

- **helpdesk/** — day-to-day support tools (password checking, IP lookups, subnetting, asset tracking)
- **system_security/** — auditing and file integrity scripts *(in progress)*
- **networking/** — network diagnostics and packet analysis *(in progress)*
- **web_security/** — basic web vulnerability demos and header checks *(in progress)*
- **monitoring/** — log analysis and alerting *(in progress)*
- **documentation/** — notes on architecture, security decisions, and incident response

## Tools so far

| Tool | What it does |
|---|---|
| `helpdesk/password_checker.py` | Rates password strength and flags common weak patterns (repeated characters, sequences, dictionary passwords) |
| `helpdesk/ip_information.py` | Looks up geolocation and ISP info for any IP, or fetches your own public IP |
| `helpdesk/subnet_calculator.py` | Works out network address, broadcast address, usable host range, and subnet mask from CIDR notation |
| `helpdesk/asset_inventory.py` | Simple CLI for tracking IT assets — add, update, remove, and export to CSV |

## Running the tools

Each script runs on its own. For example:

```bash
cd helpdesk
python password_checker.py
```

Some tools need a couple of extra packages — set up a virtual environment and install them with:

```bash
python -m venv venv
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

## Why I built this

I wanted a project that reflects real IT support and security work rather than just tutorials that includes scripting for automation, understanding networking fundamentals, and thinking about security from a practical, defensive angle. More tools are on the way as I keep building this out.