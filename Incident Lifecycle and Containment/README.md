
# 🚨 Incident Lifecycle & Containment 

<div align="center">

# 🛡️ Digital Forensics & Incident Response (DFIR) with Automated Containment

### 🔍 Detection • 🚧 Containment • 🧹 Eradication • 🔄 Recovery

![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04%20LTS-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Metasploit](https://img.shields.io/badge/Metasploit-Framework-red?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-Automation-3776AB?style=for-the-badge&logo=python&logoColor=white)
![DFIR](https://img.shields.io/badge/DFIR-Incident%20Response-darkred?style=for-the-badge)
![SOC](https://img.shields.io/badge/SOC-Operations-green?style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-Security-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Automation](https://img.shields.io/badge/Automation-Response-blue?style=for-the-badge)

</div>

---

# 📖 Project Overview

This lab provides hands-on experience with the complete **Incident Response Lifecycle** used by modern Security Operations Centers (SOC) and Digital Forensics & Incident Response (DFIR) teams.

Students will simulate a controlled security incident, develop automated detection and containment tools, perform incident handling activities, and document response actions according to industry best practices.

The project focuses on:

- 🔍 Security Incident Detection
- 🚧 Automated Containment
- 🧹 Threat Eradication
- 🔄 Service Recovery
- 📑 Incident Documentation
- 🤖 Security Automation
- 🛡️ DFIR Methodologies
- ⚡ Response Acceleration

By completing this lab, students gain practical experience responding to incidents in a structured and repeatable manner.

---

# 🎯 Learning Objectives

After completing this lab, students will be able to:

### 🔍 Incident Detection

- Identify Indicators of Compromise (IOCs)
- Monitor suspicious processes
- Detect malicious network activity
- Generate incident reports

### 🚧 Incident Containment

- Isolate malicious processes
- Block suspicious communications
- Quarantine malicious files
- Preserve forensic evidence

### 🧹 Threat Eradication

- Remove malware artifacts
- Eliminate persistence mechanisms
- Reset compromised configurations
- Secure affected assets

### 🔄 Recovery Operations

- Restore normal services
- Verify system integrity
- Confirm remediation success
- Resume business operations

### 📑 Incident Documentation

- Create incident reports
- Document actions taken
- Record timelines
- Produce lessons learned

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| 🛡️ Metasploit Framework | Security Incident Simulation |
| 🐍 Python 3.8+ | Detection & Automation |
| 🐧 Ubuntu 20.04 LTS | Incident Response Platform |
| 📑 JSON | Incident Reporting |
| 🔍 Psutil | Process & Network Monitoring |
| 🌐 Apache2 | Test Web Service |
| 📂 VSFTPD | Test FTP Service |
| 🔥 IPTables | Network Containment |
| 🧪 DFIR Practices | Incident Handling |

---

# 📋 Prerequisites

Before beginning this lab, students should have:

### 🖥️ Linux Fundamentals

- Command Line Usage
- File Management
- Service Administration
- Process Monitoring

### 🌐 Security Knowledge

- Network Fundamentals
- Attack Vectors
- Malware Concepts
- Security Monitoring

### 🐍 Python Programming

- Classes
- Functions
- File Handling
- JSON Processing

### 🛡️ Incident Response Concepts

- Detection
- Containment
- Eradication
- Recovery

---

# 🏗️ Incident Response Architecture

```text
                ┌────────────────────┐
                │ Security Incident  │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Detection Phase    │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Containment Phase  │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Eradication Phase  │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Recovery Phase     │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Lessons Learned    │
                └────────────────────┘
```

---

# 🚀 Lab Tasks

---

# 🔥 Task 1 – Simulate a Security Incident

## 🎯 Purpose

Create a controlled security incident for detection and response testing.

---

## 🖥️ Vulnerable Environment Setup

Deploy test services:

### FTP Service

```text
VSFTPD
User: ftpuser
Password: password123
```

### Web Service

```text
Apache2 Web Server
```

---

## 🛡️ Metasploit Framework Initialization

### Components

- PostgreSQL Database
- Metasploit Framework
- Payload Generation
- Session Management

### Skills Learned

✅ Metasploit Configuration

✅ Security Testing

✅ Attack Simulation

---

## 🔎 Reconnaissance Activities

Perform:

### Port Discovery

```text
FTP (21)
SSH (22)
HTTP (80)
HTTPS (443)
```

### Service Enumeration

```text
FTP Version Detection
```

### Skills Learned

✅ Vulnerability Discovery

✅ Enumeration Techniques

✅ Reconnaissance Methodology

---

## ⚠️ Controlled Incident Simulation

Generate a simulated compromise using:

```text
Reverse Connection Payload
```

Monitor:

- Active Sessions
- Network Activity
- System Processes

---

## 📑 Initial Incident Documentation

Record:

### Key Evidence

- Timestamp
- Attack Vector
- Services Affected
- Indicators of Compromise

### Skills Learned

✅ Evidence Collection

✅ Incident Documentation

---

# 🔍 Task 2 – Build Incident Detection Framework

## 🎯 Purpose

Develop automated detection capabilities using Python.

---

# 🐍 Incident Detector Features

### Process Monitoring

Detect suspicious processes such as:

```text
meterpreter
payload
nc
netcat
```

Monitor:

- PID
- Process Name
- Command Line
- Creation Time

---

### Network Monitoring

Monitor suspicious ports:

```text
4444
5555
6666
1234
```

Capture:

- Local Address
- Remote Address
- Connection State
- Associated Process

---

# 📊 Detection Workflow

```text
Running Processes
        │
        ▼
Process Analysis
        │
        ▼
Network Analysis
        │
        ▼
IOC Detection
        │
        ▼
Incident Report
```

---

### Incident Report Contents

```json
{
  "timestamp": "",
  "processes": [],
  "connections": [],
  "status": ""
}
```

---

### Skills Learned

✅ IOC Identification

✅ Process Analysis

✅ Network Monitoring

✅ Automated Reporting

---

# 🚧 Task 3 – Develop Automated Containment System

## 🎯 Purpose

Automate response actions to reduce incident impact.

---

# ⚡ Containment Actions

### Process Termination

Actions:

```text
Graceful Termination
Force Kill if Necessary
```

Targets:

- Malicious Payloads
- Suspicious Sessions

---

### Network Isolation

Block suspicious communications using:

```text
iptables
```

Actions:

```text
Drop Outbound Traffic
Block Malicious IPs
```

---

### File Quarantine

Move suspicious files into:

```text
/tmp/quarantine
```

Actions:

```text
Rename Files
Remove Execution Permissions
Preserve Evidence
```

---

### System Snapshot Creation

Collect:

```text
Running Processes
Network Connections
System Logs
```

Purpose:

- Forensics
- Evidence Preservation
- Timeline Reconstruction

---

# 🧠 Containment Workflow

```text
Incident Report
        │
        ▼
Create Snapshot
        │
        ▼
Kill Processes
        │
        ▼
Block Connections
        │
        ▼
Quarantine Files
        │
        ▼
Containment Report
```

---

### Skills Learned

✅ Incident Containment

✅ Process Isolation

✅ Network Defense

✅ Forensic Preservation

---

# 🧹 Task 4 – Execute Eradication Phase

## 🎯 Purpose

Completely remove malicious artifacts.

---

# 🔥 Eradication Activities

### Remove Payload Files

Examples:

```text
test_payload
payload
```

---

### Reset Firewall Rules

Restore normal network operations.

---

### Remove Remaining Processes

Terminate:

```text
meterpreter
```

---

### Verification

Confirm:

- No malicious files
- No suspicious processes
- No unauthorized connections

---

### Skills Learned

✅ Malware Removal

✅ Environment Cleanup

✅ Threat Elimination

---

# 🔄 Task 5 – Recovery Phase

## 🎯 Purpose

Restore normal business operations safely.

---

# 🛠️ Recovery Activities

### Service Restoration

Restart:

```text
SSH
Apache2
```

---

### Health Validation

Verify:

- Services Running
- Network Connectivity
- System Stability

---

### Post-Recovery Scan

Run:

```text
Incident Detector
```

Expected Result:

```text
No Incidents Found
```

---

### Skills Learned

✅ Service Recovery

✅ Validation Procedures

✅ Operational Restoration

---

# 📑 Task 6 – DFIR Documentation

## 🎯 Purpose

Create professional incident response reports.

---

# 📋 Incident Report Structure

## 1️⃣ Detection

Document:

- Detection Time
- IOC List
- Detection Method

---

## 2️⃣ Containment

Document:

- Actions Taken
- Systems Affected
- Time to Contain

---

## 3️⃣ Eradication

Document:

- Files Removed
- Threats Eliminated
- Security Fixes

---

## 4️⃣ Recovery

Document:

- Services Restored
- Validation Results
- Recovery Duration

---

## 5️⃣ Lessons Learned

Document:

- Root Cause
- Recommendations
- Follow-Up Actions

---

### Skills Learned

✅ DFIR Documentation

✅ Reporting Standards

✅ Incident Communication

---

# 📊 DFIR Lifecycle Diagram

```text
Detection
    │
    ▼
Containment
    │
    ▼
Eradication
    │
    ▼
Recovery
    │
    ▼
Lessons Learned
```

---

# 📂 Suggested Project Structure

```text
incident-response-lab/
│
├── scripts/
│   ├── incident_detector.py
│   └── containment_automation.py
│
├── logs/
│   ├── incident_detection.log
│   ├── containment_actions.log
│   └── system_snapshots/
│
├── reports/
│   ├── incident_report.json
│   ├── containment_report.json
│   └── final_report.txt
│
├── quarantine/
│   └── isolated_files/
│
└── README.md
```

---

# 📈 Expected Outcomes

After completing this lab, students will have:

✅ Simulated a Security Incident

✅ Used Metasploit Framework

✅ Built Detection Automation

✅ Developed Containment Scripts

✅ Executed Complete Incident Lifecycle

✅ Preserved Forensic Evidence

✅ Produced DFIR Documentation

✅ Practiced Security Operations Workflows

---

# 🎓 Skills Gained

### 🔍 Threat Detection

### 🚧 Incident Containment

### 🧹 Malware Eradication

### 🔄 Recovery Operations

### 🐍 Python Security Automation

### 📑 Incident Documentation

### 🛡️ DFIR Methodologies

### ⚡ Security Operations

---

# 🛠️ Troubleshooting Guide

---

## ❌ Metasploit Payload Doesn't Execute

### Verify Permissions

```bash
ls -l /tmp/test_payload
```

### Ensure Executable Bit

```bash
chmod +x /tmp/test_payload
```

### Verify Listener

Check Metasploit handler is active.

---

## ❌ Python Cannot Import psutil

### Install Dependency

```bash
pip3 install --user psutil
```

### Verify Installation

```bash
python3 -c "import psutil"
```

---

## ❌ Permission Denied During Containment

### Run with Elevated Privileges

```bash
sudo python3 containment_automation.py
```

---

## ❌ No Incident Detected

### Verify Payload Running

```bash
ps aux | grep payload
```

### Verify Active Session

Check Metasploit session status.

---

# 🌟 Real-World Applications

This project directly supports careers such as:

- 🛡️ SOC Analyst
- 🚨 Incident Responder
- 🔍 DFIR Analyst
- 🐍 Security Automation Engineer
- 🔥 Threat Hunter
- 🔐 Blue Team Specialist
- 🏢 Security Operations Engineer

---

# 🏆 Key Takeaways

### 🔥 Incident Response Is Structured

Every response follows:

```text
Detection → Containment → Eradication → Recovery
```

---

### 🔥 Automation Accelerates Response

Faster response reduces damage.

---

### 🔥 Evidence Preservation Matters

Snapshots support forensic investigations.

---

### 🔥 Documentation Is Essential

Accurate reports improve future responses.

---

### 🔥 Verification Ensures Success

Recovery must be validated before closure.

---

# 🎯 Conclusion

The **Incident Lifecycle & Containment Lab** provides practical experience implementing a complete incident response workflow using DFIR methodologies, Python automation, and controlled security incident simulation.

Students learn how to:

✔️ Detect Security Incidents

✔️ Identify Indicators of Compromise

✔️ Automate Containment

✔️ Preserve Evidence

✔️ Eradicate Threats

✔️ Recover Systems

✔️ Create Professional Incident Reports

✔️ Follow Industry DFIR Best Practices

These skills are essential for SOC analysts, incident responders, DFIR investigators, and cybersecurity professionals responsible for managing security incidents in modern enterprise environments.

---

<div align="center">

## 🛡️ Detect • 🚧 Contain • 🧹 Eradicate • 🔄 Recover

### ⭐ Incident Lifecycle & Containment Lab ⭐

Strengthen DFIR Skills • Automate Response • Improve Security Operations

</div>
````
