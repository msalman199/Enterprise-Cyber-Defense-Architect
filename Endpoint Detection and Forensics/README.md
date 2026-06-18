# 🖥️ Endpoint Detection and Forensics

<div align="center">

# 🔍 Endpoint Detection & Digital Forensics 

### 🚨 Automated Endpoint Monitoring • Memory Analysis • Threat Correlation • Incident Reporting

![Linux](https://img.shields.io/badge/Linux-Ubuntu%2020.04-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Velociraptor](https://img.shields.io/badge/Velociraptor-Endpoint%20Monitoring-2E8B57?style=for-the-badge)
![Forensics](https://img.shields.io/badge/Digital-Forensics-blue?style=for-the-badge)
![Incident Response](https://img.shields.io/badge/Incident-Response-red?style=for-the-badge)
![Security](https://img.shields.io/badge/Cyber-Security-black?style=for-the-badge)

</div>

---

# 📖 Project Overview

This project provides hands-on experience with **Endpoint Detection and Response (EDR)** and **Digital Forensics** using industry-standard tools and custom Python automation.

Students will deploy **Velociraptor** for endpoint monitoring, collect forensic artifacts, analyze system memory and processes, correlate evidence from multiple sources, and generate comprehensive incident response reports.

The lab simulates real-world endpoint investigations performed by:

- 🔍 Security Analysts
- 🛡️ SOC Analysts
- 🚨 Incident Responders
- 🧠 Threat Hunters
- 📁 Digital Forensics Investigators

---

# 🎯 Objectives

By completing this lab, students will learn how to:

✅ Install and configure Velociraptor for endpoint monitoring

✅ Develop Python-based endpoint data collection tools

✅ Perform memory and process forensics analysis

✅ Correlate endpoint telemetry with forensic evidence

✅ Identify suspicious system activity

✅ Generate professional incident response reports

✅ Build an automated forensic investigation workflow

---

# 🏗️ Lab Architecture

```text
┌──────────────────────────┐
│     Endpoint System      │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│      Velociraptor        │
│ Endpoint Monitoring Agent│
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ Endpoint Data Collector  │
│     Python Script        │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ Memory Forensics Engine  │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ Correlation Framework    │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ Incident Response Report │
└──────────────────────────┘
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| 🐍 Python 3.8+ | Automation & Analysis |
| 🖥️ Ubuntu Linux | Investigation Platform |
| 🔍 Velociraptor | Endpoint Monitoring |
| 📁 JSON | Data Storage |
| ⚙️ Psutil | System Information Collection |
| 📡 Netstat / SS | Network Analysis |
| 📜 Bash Utilities | Log & System Analysis |
| 🧠 Digital Forensics Techniques | Threat Investigation |

---

# 📂 Project Structure

```text
endpoint-forensics-lab/
│
├── endpoint_collector.py
├── memory_analyzer.py
├── forensics_correlator.py
│
├── endpoint_data/
│   ├── system_info.json
│   ├── processes.json
│   ├── file_hashes.json
│   └── collection_summary.json
│
├── memory_analysis/
│   ├── process_tree.txt
│   ├── network_connections.txt
│   ├── filesystem_artifacts.json
│   ├── timeline.json
│   └── analysis_summary.json
│
├── correlation_results/
│   ├── risk_assessment.json
│   ├── incident_report.json
│   └── incident_report.txt
│
├── final_report/
│   └── executive_summary.txt
│
├── logs/
├── artifacts/
│
└── README.md
```

---

# 🚀 Task 1 – Velociraptor Deployment

## 🔹 Install Velociraptor

Download and prepare the endpoint monitoring platform.

### Key Activities

✔ Create working directory

✔ Download Velociraptor binary

✔ Configure executable permissions

✔ Create system symlink

---

## 🔹 Generate Configuration Files

Generate:

- Server configuration
- Client configuration
- Artifact storage directories

---

## 🔹 Start Monitoring Services

Launch:

- Velociraptor Frontend
- Velociraptor Client

Verify processes are running successfully.

---

# 🖥️ Task 2 – Endpoint Data Collection

## 🔹 Endpoint Collector Development

Students complete the implementation of:

### System Information Collection

Collect:

- Hostname
- Kernel Version
- Architecture
- Uptime
- Logged Users
- Network Connections

---

### Process Enumeration

Collect:

- PID
- Process Name
- Username
- Command Line
- Creation Time

---

### File Integrity Monitoring

Generate SHA256 hashes for:

```text
/bin
/usr/bin
```

Collect:

- File path
- File size
- Modification time
- SHA256 hash

---

### Log Collection

Acquire:

```text
/var/log/auth.log
/var/log/syslog
```

Collect:

- Recent authentication events
- System activity logs
- Security-related messages

---

## 🔹 Data Collection Workflow

```text
System Information
        │
        ▼
Process Enumeration
        │
        ▼
File Hash Analysis
        │
        ▼
Log Collection
        │
        ▼
JSON Evidence Storage
```

---

# 🧠 Task 3 – Memory Forensics Analysis

## 🔹 Process Analysis

Investigate running processes and identify:

- Suspicious binaries
- Reverse shells
- Netcat activity
- Malicious execution paths

Examples:

```text
nc
netcat
wget
curl
/tmp/
```

---

## 🔹 Network Analysis

Analyze:

- Listening Ports
- Established Connections
- Suspicious Services

Flag unusual ports such as:

```text
4444
1234
31337
5555
```

---

## 🔹 File System Forensics

Investigate:

### Temporary Directories

```text
/tmp
/var/tmp
```

### Hidden Files

```text
.*
```

### Bash History

Review suspicious commands including:

```text
wget
curl
nc
chmod +x
bash -i
```

---

## 🔹 Timeline Generation

Build a timeline from:

- Authentication Logs
- System Logs
- Process Creation Events
- Network Activity

---

# 🔗 Task 4 – Correlation Analysis

## 🔹 Endpoint Correlation

Combine:

- Process Data
- File Artifacts
- Network Activity
- System Logs

---

## 🔹 Process Correlation

Identify:

✅ Unknown Processes

✅ Temporary Executables

✅ Suspicious Parent/Child Relationships

✅ Unauthorized User Activity

---

## 🔹 Network Correlation

Analyze:

- External Connections
- Unusual Ports
- Unknown IP Addresses
- Potential Command & Control Activity

---

## 🔹 File Correlation

Detect:

- Modified System Files
- Malware Locations
- Persistence Mechanisms
- Hidden Artifacts

---

# 📊 Risk Assessment Engine

Generate risk score based on findings.

### Example Model

| Score | Risk Level |
|---------|------------|
| 0-25 | 🟢 LOW |
| 26-50 | 🟡 MEDIUM |
| 51-75 | 🟠 HIGH |
| 76-100 | 🔴 CRITICAL |

---

# 📑 Incident Response Report

The system automatically generates:

### Executive Summary

```text
Overview of investigation
```

### Indicators of Compromise (IOCs)

```text
Suspicious Processes
Suspicious Files
Suspicious IPs
```

### Timeline of Events

```text
Chronological attack reconstruction
```

### Risk Assessment

```text
Overall Risk Score
```

### Remediation Guidance

```text
Recommended response actions
```

---

# 🔍 Example Investigation Workflow

```text
Velociraptor Monitoring
           │
           ▼
Endpoint Collection
           │
           ▼
Memory Analysis
           │
           ▼
Artifact Correlation
           │
           ▼
Risk Assessment
           │
           ▼
Incident Report
```

---

# 🎓 Learning Outcomes

After completing this lab, students will be able to:

✅ Deploy Velociraptor for endpoint visibility

✅ Collect forensic evidence automatically

✅ Investigate processes and network activity

✅ Perform memory-based threat hunting

✅ Correlate multiple evidence sources

✅ Build incident response reports

✅ Conduct endpoint forensic investigations

✅ Apply DFIR methodologies in real-world scenarios

---

# 🛡️ Security Skills Developed

### Endpoint Security

- Endpoint Detection & Response (EDR)
- Host Monitoring
- Threat Detection

### Digital Forensics

- Artifact Collection
- Timeline Analysis
- Evidence Preservation

### Incident Response

- Threat Investigation
- IOC Identification
- Risk Assessment

### Python Security Automation

- System Enumeration
- Log Analysis
- Automated Reporting

---

# 📈 Expected Outcomes

By the end of this project you will have:

✔ Functional Velociraptor deployment

✔ Automated endpoint collection framework

✔ Memory forensics analysis system

✔ Correlation engine for investigations

✔ Risk assessment methodology

✔ Professional incident response reports

✔ Practical DFIR experience

---

# 🚀 Future Enhancements

### Advanced Endpoint Detection

- YARA Rule Integration
- Sigma Rule Matching
- Threat Intelligence Feeds

### Memory Forensics

- Volatility Framework Integration
- Memory Dump Analysis
- Malware Detection

### SIEM Integration

- ELK Stack
- Wazuh
- Splunk

### Automated Threat Hunting

- Behavioral Analytics
- Machine Learning Detection
- Automated IOC Enrichment

---

# 🏆 Conclusion

This lab provides a complete introduction to **Endpoint Detection and Digital Forensics** using **Velociraptor**, **Python automation**, and **forensic correlation techniques**.

Students gain practical experience in collecting evidence, analyzing suspicious activity, correlating multiple data sources, and producing professional incident response reports.

These skills form the foundation of modern:

🔍 Digital Forensics

🚨 Incident Response

🛡️ Security Operations

🧠 Threat Hunting

and Endpoint Security Monitoring.

---

<div align="center">

### 🔐 Investigate • Correlate • Detect • Respond 🔐

**Endpoint Detection & Forensics Lab**

⭐ Building Practical DFIR Skills Through Hands-On Investigation ⭐

</div>
