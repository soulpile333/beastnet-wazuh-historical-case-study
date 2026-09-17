# Authentication-event workflow dataset

This dataset recreates the structure and authentication-event workflow I analyzed in BeastNet because the original Wazuh CSV export was not retained.

The bounded CSV contains five non-sensitive workflow records for the Windows Security events used in this project:

- `4624` — successful account logon
- `4625` — failed account logon
- `4740` — account lockout

The values are limited to a lab endpoint label, UTC timestamps, event IDs, readable descriptions, record identifiers, and a short message. The file contains no credentials, addresses, personal identities, or operational network data.

## Verified Python workflow

Command:

```text
python ".\scripts\Summarize-AuthenticationEvents.py" ".\data\authentication-events.csv"
```

Verified output:

```text
Total events: 5
4624 (Successful logon): 2
4625 (Failed logon): 2
4740 (Account lockout): 1
Note: Counts are investigative leads and require contextual validation of the account, source, host, time, and logon context.
```

The counts demonstrate the utility's CSV parsing and event-label translation. They are not incident findings and require analyst context.
