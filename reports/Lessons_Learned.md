# Lessons learned

- Wazuh visibility depends on healthy agents, reliable DNS and routing, correct event channels, synchronized time, and endpoint logging.
- Sysmon adds useful endpoint context but still requires analyst interpretation.
- Event ID 4625 means a logon failed; it does not confirm an attacker or brute-force activity.
- Event ID 4740 confirms a lockout, but stale credentials can cause lockouts too.
- Event ID 4624 should be reviewed with logon type, user, host, source, and surrounding activity.
- Missing dashboard results can be caused by filtering, time range, agent connectivity, or collection configuration.
- A strong report separates facts from assessment and records benign explanations, investigative pivots, remediation, and uncertainty.
