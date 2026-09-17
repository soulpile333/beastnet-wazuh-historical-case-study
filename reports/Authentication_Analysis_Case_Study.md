# Authentication analysis case study

## Scenario practiced

I generated controlled authentication activity within the authorized independent lab to practice detection and analysis. This was a learning exercise, not a confirmed incident.

## Investigation workflow

1. Identify Event ID 4625 failed logons.
2. Group failures by target account, source, endpoint, and time window.
3. Review logon type, failure reason, status, and substatus.
4. Search for Event ID 4740 account lockouts involving the same account.
5. Search for Event ID 4624 successful logons before or after the failure sequence.
6. Pivot into Sysmon and endpoint telemetry where relevant.
7. Consider user error, stale service authentication, scheduled tasks, mapped drives, and other stored authentication state.
8. Record observed facts, analyst assessment, confidence, benign alternatives, and next pivots separately.

## Interpretation

Repeated failed logons are an investigative lead, not automatic proof of brute force. A defensible assessment depends on pattern, source ownership, account privilege, asset criticality, successful follow-on activity, endpoint context, and benign explanations. Event 4740 confirms a lockout, but stale credentials can cause lockouts too. Event 4624 requires review of logon type, user, host, source, and timing.

## Example analyst output shape

| Section | Question |
| --- | --- |
| Observed facts | What event IDs, accounts, hosts, sources, and times are actually present? |
| Assessment | What hypotheses fit the available context, and how confident is the analyst? |
| Benign alternatives | Could user error, a scheduled task, mapped drive, or stale credential explain it? |
| Next pivots | Which endpoint, identity, or network records should be checked next? |
| Limitations | What data is missing or unavailable for verification? |

Specific event counts, timestamps, source addresses, dashboards, and reports are not included because the original supporting artifacts are no longer retained.
