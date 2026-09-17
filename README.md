# BeastNet Wazuh Historical Case Study

## Project status notice

> **Project Status: Completed Historical Lab**
>
> BeastNet was an independent cybersecurity lab that I personally built and operated. The original virtual machines and supporting artifacts were later retired and are no longer available. This repository documents the architecture, implementation process, troubleshooting experience, investigation methodology, and reconstructed scripts based on the work I completed.

## Executive summary

I built BeastNet as an isolated Windows Active Directory security lab to develop practical endpoint-monitoring and security-operations skills. I configured the domain foundation, connected Windows endpoints to Wazuh, added Sysmon telemetry, and used Wazuh, PowerShell, and Windows Event Logs during controlled authentication-monitoring exercises.

The project gave me direct practice with endpoint visibility, alert validation, Windows authentication analysis, infrastructure troubleshooting, false-positive reasoning, and technical documentation. It represents independent lab experience and is separate from professional employment or production operations.

## What I built

I completed this progression in the BeastNet lab:

1. Built and operated the independent cybersecurity lab.
2. Created the `ad.beastnet.org` Active Directory domain.
3. Deployed and configured AD DS, DNS, and DHCP.
4. Domain-joined Windows systems.
5. Deployed Active Directory Certificate Services and configured trusted HTTPS access for the Wazuh dashboard through the BeastNet certificate authority.
6. Deployed Wazuh for centralized security monitoring.
7. Connected Windows endpoints to Wazuh with endpoint agents.
8. Deployed Sysmon to increase endpoint visibility.
9. Generated and analyzed controlled authentication activity.
10. Documented the implementation, troubleshooting lessons, investigation method, and limitations.

## Technical architecture

The historical data flow was Windows endpoint activity and logs, through Wazuh endpoint agents and the Wazuh manager/indexer, to the Wazuh dashboard and analyst workflow. AD DS, DNS, DHCP, and AD CS supplied identity, naming, connectivity, and certificate dependencies.

See the [historical architecture diagram](architecture/Architecture.md) and [implementation journey](architecture/Implementation_Journey.md).

## Security monitoring workflow

I validated endpoint telemetry by checking agent communication, event-channel configuration, time range and filtering, Windows logging, and the surrounding identity and network dependencies. I used Sysmon as additional endpoint context, then reviewed Wazuh results and PowerShell event queries before documenting facts, assessment, uncertainty, and next investigative steps.

## Authentication analysis

I used Wazuh and PowerShell to investigate relationships among:

- **Event ID 4624:** a successful account logon.
- **Event ID 4625:** a failed account logon.
- **Event ID 4740:** a user account was locked out.

Repeated failed logons are investigative leads requiring context, not confirmation of brute force or compromise. My analysis method was to identify the affected account and endpoint, review the time window, group failed attempts, examine source/workstation/logon type and failure details, search for lockouts, look for successful logons before or after the failures, correlate endpoint telemetry, consider benign causes such as user error or stale credentials, and document facts separately from assessment and recommended next steps.

The full [authentication analysis case study](reports/Authentication_Analysis_Case_Study.md) explains the workflow without inventing event totals, source addresses, timestamps, affected accounts, or attack conclusions.

## Troubleshooting and implementation challenges

I troubleshot Hyper-V networking, static addressing, DNS, DHCP, domain connectivity, certificate trust, Wazuh agent communication, Windows logging, firewall access, and Group Policy. These issues taught me that reliable endpoint monitoring depends on healthy identity, networking, time, logging, certificate, and agent foundations.

## Skills demonstrated

| Area | Demonstrated work |
| --- | --- |
| Endpoint protection | Wazuh agent enrollment and validation, Windows Security collection, Sysmon context |
| SOC analysis | Authentication correlation, timeline review, alert validation, false-positive reasoning |
| Windows security | Interpretation of Events 4624, 4625, and 4740 with logon context |
| Automation | PowerShell event retrieval and CSV export; standard-library Python aggregation |
| Operations | DNS, DHCP, domain connectivity, certificates, firewall, Group Policy, and logging dependencies |
| Communication | Technical documentation that separates facts, assessment, uncertainty, and next steps |

## Repository contents

- [`architecture/Architecture.md`](architecture/Architecture.md) - component flow and responsibilities.
- [`architecture/Implementation_Journey.md`](architecture/Implementation_Journey.md) - build sequence and troubleshooting.
- [`reports/Authentication_Analysis_Case_Study.md`](reports/Authentication_Analysis_Case_Study.md) - event-analysis method.
- [`reports/Lessons_Learned.md`](reports/Lessons_Learned.md) - operational takeaways.
- [`data/README.md`](data/README.md) - bounded authentication-event workflow dataset and verified Python output.

## Reconstructed scripts

Both files are labeled: **Reconstructed portfolio example based on the historical BeastNet workflow. This is not an original retained artifact.**

- [`Get-BeastNetAuthenticationEvents.ps1`](scripts/Get-BeastNetAuthenticationEvents.ps1) retrieves selected Windows Security events and writes a potentially sensitive CSV.
- [`Summarize-AuthenticationEvents.py`](scripts/Summarize-AuthenticationEvents.py) counts event IDs in an authorized CSV export using Python standard-library modules only.

The scripts do not recreate historical outputs. Run them only on authorized systems and data.

## Use the Scripts

- [`Get-BeastNetAuthenticationEvents.ps1`](scripts/Get-BeastNetAuthenticationEvents.ps1) - collects selected Windows Security events from an authorized system.
- [`Summarize-AuthenticationEvents.py`](scripts/Summarize-AuthenticationEvents.py) - summarizes event IDs from a CSV.
- [`authentication-events.csv`](data/authentication-events.csv) - bounded workflow dataset.
- [`data/README.md`](data/README.md) - dataset details and verified output.

Run the Python utility with:

```text
python ".\scripts\Summarize-AuthenticationEvents.py" ".\data\authentication-events.csv"
```

The utility translates `4624` to **Successful logon**, `4625` to **Failed logon**, and `4740` to **Account lockout**. Counts are investigative leads requiring account, source, host, time, and logon context.

Use the PowerShell utility only on systems you own or are explicitly authorized to administer.

## Run on a Windows PC

The PowerShell collector is not limited to BeastNet. It can query the Windows Security log on the current computer or another Windows computer that the user is authorized to administer.

### 1. Open PowerShell as Administrator

Open Windows PowerShell and select Run as administrator. Elevated permissions may be required to access the Windows Security log.

### 2. Navigate to the repository

Replace the placeholder path with the actual location where the repository is saved:

	cd "C:\path\to\beastnet-wazuh-historical-case-study"

### 3. Find the current computer name

Run:

	$env:COMPUTERNAME

This environment variable returns the hostname of the current Windows computer.

Example output:

	LAB-WKS01

### 4. Run the collector

To query the current computer, run:

	& ".\scripts\Get-BeastNetAuthenticationEvents.ps1" -ComputerName $env:COMPUTERNAME

A specific authorized computer name can also be supplied:

	& ".\scripts\Get-BeastNetAuthenticationEvents.ps1" -ComputerName "LAB-WKS01"

- Replace `C:\path\to\beastnet-wazuh-historical-case-study` with the actual location where the repository is saved.
- Replace `LAB-WKS01` with the name of the authorized Windows computer being checked.
- The relative path `.\scripts\Get-BeastNetAuthenticationEvents.ps1` works after navigating to the repository root.
- Run PowerShell as Administrator if access to the Windows Security log is denied.
- Only query computers that the user owns or is explicitly authorized to administer.

### 5. Locate the exported CSV

After the query completes, the script displays the full location of the exported `AuthenticationEvents.csv` file.

Example output:

	Events exported to C:\Windows\System32\AuthenticationEvents.csv

Follow the complete path displayed by the script to locate the export. The export is not necessarily saved in the repository or Documents folder.

### 6. Analyze the exported CSV

Replace the placeholder below with the full CSV path displayed by the PowerShell collector:

	python ".\scripts\Summarize-AuthenticationEvents.py" "C:\path\to\AuthenticationEvents.csv"

To analyze the reviewed dataset included with the repository:

	python ".\scripts\Summarize-AuthenticationEvents.py" ".\data\authentication-events.csv"

The first command analyzes an authorized event export created by the PowerShell collector. The second command analyzes `authentication-events.csv` from the repository's `data` folder. A real authentication export must not replace `data\authentication-events.csv`.

Authentication exports may contain account names, device names, domains, IP addresses, logon details, and other sensitive information. Real organizational authentication exports must not be committed to a public repository.

Windows Security event IDs:

- **4624:** Successful logon
- **4625:** Failed logon
- **4740:** Account lockout

Event counts are investigative leads. Review the account, computer, source, timestamp, logon type, failure reason, and surrounding authentication activity before determining why the events occurred.

## Evidence status

The original virtual machines, Wazuh dashboard, screenshots, logs, reports, and event exports are no longer retained. This repository therefore contains the historical technical narrative and reconstructed workflow, not original telemetry or a current dashboard demonstration.

## Ethical use and privacy

Use the scripts only on systems and data you are authorized to access. 
