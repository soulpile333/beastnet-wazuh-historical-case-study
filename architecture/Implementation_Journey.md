# Implementation journey

This is the implementation sequence I completed in the independent BeastNet lab.

## 1. Establish the Windows domain foundation

I built the Windows domain lab around `ad.beastnet.org`, including AD DS, DNS, DHCP, domain authentication, and domain-joined endpoints. These services established the identity, naming, and connectivity dependencies required for endpoint monitoring.

## 2. Add certificate-backed access

I deployed Active Directory Certificate Services and used a trusted certificate issued through the BeastNet certificate authority for Wazuh dashboard HTTPS access. I troubleshot service naming, DNS resolution, certificate trust, and secure administrative access.

## 3. Deploy centralized monitoring

I deployed Wazuh as the central endpoint-monitoring platform and connected Windows endpoint agents. I validated agent communication and event arrival, then troubleshot connectivity, event-channel, time-range, and configuration issues.

## 4. Add endpoint context with Sysmon

I deployed Sysmon to increase visibility into process creation, command lines, network connections, files, registry activity, and DNS queries. I used Sysmon data as investigation context rather than a complete verdict.

## 5. Practice authentication analysis

I used Wazuh and PowerShell to review successful logons (4624), failed logons (4625), and account lockouts (4740). I correlated accounts, hosts, source information, timestamps, logon type, failure details, and surrounding endpoint activity during controlled learning exercises.

## 6. Troubleshoot the visibility chain

I troubleshot Hyper-V networking, static addressing, DNS, DHCP, domain connectivity, certificates, Wazuh agents, Windows logging, firewall access, and Group Policy. The central lesson was that endpoint visibility depends on reliable identity, networking, time, logging, and agent infrastructure.
