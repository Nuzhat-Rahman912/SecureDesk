# Incident Response Reference

This is a working reference for how I'd approach incident response, along
with one worked example. It's based on the standard IR lifecycle used across
most security teams, adapted to a small-scale/help-desk context relevant to
this project.

## The IR lifecycle

1. **Identify** — Detect and confirm that an incident is actually happening.
   This could come from a monitoring alert, a user report, or a manual
   check like reviewing logs.
2. **Contain** — Limit the damage. Short-term containment might mean
   isolating a device from the network; long-term containment might mean
   patching a vulnerability while keeping systems running.
3. **Eradicate** — Remove the root cause such as malware, a compromised account,
   a misconfiguration, etc. not just the visible symptoms.
4. **Recover** — Restore affected systems to normal operation, with
   monitoring in place to confirm the issue doesn't recur.
5. **Lessons learned** — Document what happened, what worked, and what
   should change (in tooling, process, or policy) to prevent a repeat.

## How this project fits in

- `helpdesk/ip_information.py` supports the **Identify** phase — quickly
  checking whether a login or connection is coming from an unexpected
  location.
- `helpdesk/password_checker.py` supports **prevention**, upstream of
  incident response — reducing the chance of credential-based incidents
  in the first place.
- Tools planned for `monitoring/` (log analyzer, SOC alert generator, IOC
  detector) are intended to support the **Identify** and **Contain**
  phases directly, by surfacing suspicious activity from logs.

## Worked example: Suspicious login alert

**Scenario:** A monitoring alert (or a user report) flags a login to a
company account from an unfamiliar location, outside normal business hours.

**1. Identify**
- Confirm the alert is legitimate, not a false positive (e.g. an employee
  traveling or using a VPN).
- Use IP lookup (`ip_information.py`) to check the geolocation and ISP
  of the login IP.
- Check whether MFA was used, and whether it was approved or denied.

**2. Contain**
- If the login looks unauthorized, force a password reset on the affected
  account and revoke active sessions/tokens.
- Temporarily disable the account if there's a strong indication of
  compromise, to prevent further access while investigating.

**3. Eradicate**
- Check for signs of further compromise: forwarding rules added to email,
  new OAuth app authorizations, changes to account recovery info.
- Remove or reverse anything unauthorized that's found.

**4. Recover**
- Restore the account to normal use with a new password (and MFA
  re-enrollment if needed).
- Monitor the account for a period afterward for any recurrence.

**5. Lessons learned**
- Was the alert timely? Would a tool in this project have caught it
  sooner?
- Should account lockout or conditional access policies be adjusted?
- Document the incident briefly, even informally, so the pattern is
  recognizable if it happens again.

## Note

This is a reference document for a portfolio project, not a formal IR plan
for a real organization. A production IR plan would include named
stakeholders, communication protocols, legal/compliance considerations, and
would be tested through tabletop exercises — not just written down.