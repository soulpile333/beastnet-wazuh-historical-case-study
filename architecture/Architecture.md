# Historical architecture

This diagram shows the components I connected in the completed independent lab and their historical data flow.

```mermaid
flowchart TD
    A[Windows endpoint activity] --> B[Windows Security logs]
    A --> C[Sysmon telemetry]
    B --> D[Wazuh endpoint agent]
    C --> D
    D --> E[Wazuh manager and indexer]
    E --> F[Wazuh dashboard]
    F --> G[Analyst validation, correlation, reporting, and remediation]
    H[AD DS, DNS, DHCP, and AD CS] -. identity and infrastructure dependencies .-> A
    H -. agent and dashboard name resolution .-> D
    H -. certificate trust and domain services .-> F
```

## Components and responsibilities

| Component | Role in the historical lab |
| --- | --- |
| AD DS | Domain identity and authentication |
| DNS and DHCP | Name resolution, addressing, and connectivity dependencies |
| AD CS | Certificate services used for trusted HTTPS access |
| Windows endpoints | Sources of Security log and Sysmon telemetry |
| Wazuh agent | Endpoint collection and forwarding |
| Wazuh manager/indexer/dashboard | Central monitoring, search, and analyst review |
| Sysmon | Additional process, network, file, registry, and DNS context |

The original VMs, dashboard state, screenshots, and event exports are no longer retained due to needing storage space for future labs.
