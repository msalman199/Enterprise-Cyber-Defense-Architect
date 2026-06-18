# 🛡️ SIEM Setup with ELK Stack & Wazuh 

<div align="center">

# 🚨 Security Information and Event Management (SIEM)

### 📊 Hands-On Security Monitoring with ELK Stack, Wazuh & Python Automation

![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04%20LTS-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-Search%20Engine-005571?style=for-the-badge&logo=elasticsearch&logoColor=white)
![Logstash](https://img.shields.io/badge/Logstash-Log%20Processing-005571?style=for-the-badge)
![Kibana](https://img.shields.io/badge/Kibana-Security%20Analytics-005571?style=for-the-badge&logo=kibana&logoColor=white)
![Wazuh](https://img.shields.io/badge/Wazuh-HIDS%20Platform-0268B4?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-Automation-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-Log%20Data-black?style=for-the-badge)
![SIEM](https://img.shields.io/badge/SIEM-Security%20Monitoring-green?style=for-the-badge)

</div>

---

# 📖 Project Overview

This project provides practical experience in building a complete **Security Information and Event Management (SIEM)** solution using the **ELK Stack (Elasticsearch, Logstash, Kibana)** integrated with **Wazuh** for advanced host-based monitoring.

Students will learn how to:

- 🛡️ Deploy the ELK Stack
- 📊 Centralize security logs
- 🚨 Monitor security events
- 🔍 Detect suspicious activities
- 🐍 Automate log processing with Python
- 📈 Create security dashboards
- ⚡ Analyze threats using SIEM technologies

The lab simulates a real-world SOC (Security Operations Center) environment where logs from multiple sources are collected, analyzed, and visualized.

---

# 🎯 Learning Objectives

By the end of this lab, students will be able to:

### 🛡️ ELK Stack Deployment

- Install Elasticsearch
- Install Logstash
- Install Kibana
- Configure ELK services

### 🚨 Security Monitoring

- Deploy Wazuh Manager
- Configure host monitoring
- Collect security logs
- Monitor authentication events

### 🐍 Python Automation

- Build log aggregation tools
- Parse Linux logs
- Index events into Elasticsearch
- Generate security reports

### 📊 Data Visualization

- Create Kibana dashboards
- Build security visualizations
- Monitor attack trends
- Analyze authentication activity

### 🔍 Threat Detection

- Detect failed SSH attempts
- Identify brute-force attacks
- Investigate suspicious activity
- Monitor system events

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| 🔍 Elasticsearch | Log Storage & Search |
| 🔄 Logstash | Data Processing Pipeline |
| 📊 Kibana | Security Visualization |
| 🛡️ Wazuh | Host Intrusion Detection |
| 📁 Filebeat | Log Forwarding |
| 🐍 Python | Automation & Analysis |
| 🖥️ Ubuntu 20.04 LTS | Operating System |
| 📄 JSON | Structured Log Format |
| 🔐 Linux Authentication Logs | Security Monitoring |

---

# 📋 Prerequisites

Before starting this lab, students should have:

### 🖥️ Linux Skills

- Command Line Navigation
- Service Management
- Package Installation
- File Permissions

### 🌐 Security Knowledge

- Security Monitoring Concepts
- Authentication Systems
- Log Management
- Threat Detection

### 🐍 Programming Skills

- Python Basics
- Functions
- Classes
- JSON Processing

### 📊 Data Knowledge

- Log Formats
- Event Analysis
- Structured Data
- Basic Elasticsearch Concepts

---

# 🏗️ SIEM Architecture

```text
                    ┌────────────────────┐
                    │ Linux System Logs  │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │       Wazuh        │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │      Filebeat      │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │      Logstash      │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │   Elasticsearch    │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │       Kibana       │
                    └────────────────────┘
```

---

# 🚀 Lab Tasks

---

# 🛠️ Task 1 – Install & Configure ELK Stack

## 🎯 Purpose

Deploy a fully functional ELK Stack environment.

### 🔹 Components Installed

### 🔍 Elasticsearch

Stores and indexes security events.

### 🔄 Logstash

Processes incoming logs.

### 📊 Kibana

Visualizes security data.

---

### 🔹 Configuration Activities

✅ Configure Elasticsearch Cluster

✅ Configure Kibana Interface

✅ Create Logstash Pipelines

✅ Enable Services

✅ Validate Connectivity

---

### Skills Learned

- ELK Deployment
- Service Configuration
- Pipeline Development
- Log Processing

---

# 🛡️ Task 2 – Integrate Wazuh

## 🎯 Purpose

Add host-based intrusion detection and security monitoring.

### 🔹 Wazuh Features

### 🔐 Authentication Monitoring

Monitor:

```text
/var/log/auth.log
```

### 🖥️ System Activity Monitoring

Monitor:

```text
/var/log/syslog
```

### 🚨 Security Alert Generation

Generate:

- Authentication Alerts
- Privilege Escalation Alerts
- System Integrity Events

---

### 🔹 Filebeat Integration

Forward Wazuh alerts to Logstash.

```text
Wazuh
   │
   ▼
Filebeat
   │
   ▼
Logstash
   │
   ▼
Elasticsearch
```

---

### Skills Learned

✅ HIDS Deployment

✅ Log Collection

✅ Security Monitoring

✅ Event Forwarding

---

# 🐍 Task 3 – Develop Python Log Aggregation System

## 🎯 Purpose

Automate log collection, parsing, and indexing.

---

# 🔹 Log Aggregator Features

### 📄 Authentication Log Parsing

Extract:

- Timestamp
- Username
- IP Address
- Event Type

### 🖥️ Syslog Parsing

Extract:

- Process Name
- PID
- Message Content

### 📊 Elasticsearch Indexing

Store logs in:

```text
siem-logs-YYYY.MM.DD
```

### 🚨 Security Reporting

Generate reports for:

- Failed SSH Attempts
- Brute Force Activity
- Top Attacking IPs

---

# 🔹 Python Components

```text
SIEMLogAggregator
│
├── Elasticsearch Connectivity
├── Auth Log Parser
├── Syslog Parser
├── Log Indexing
├── Report Generation
└── Automation Engine
```

---

### Skills Learned

✅ Log Parsing

✅ Elasticsearch APIs

✅ Security Analytics

✅ Python Automation

---

# ⏰ Task 4 – Automated Scheduling

## 🎯 Purpose

Run security monitoring automatically.

### Features

### 🔄 Scheduled Execution

Run every:

```text
5 Minutes
```

### 📊 Continuous Monitoring

Process new events automatically.

### 🚨 Automated Reporting

Generate ongoing security reports.

---

### Skills Learned

- Task Scheduling
- Continuous Monitoring
- Automation Workflows
- Security Operations

---

# 📊 Task 5 – Build Kibana Dashboards

## 🎯 Purpose

Visualize security events and monitor threats.

---

# 📈 Dashboard 1 – Failed SSH Attempts

### Visualization

Line Chart

Metrics:

```text
Count of Events
```

Filter:

```text
event_type: ssh_failed
```

Purpose:

- Monitor brute-force attempts
- Identify attack spikes

---

# 🌍 Dashboard 2 – Top Attacking IPs

### Visualization

Data Table

Metrics:

```text
Count by IP Address
```

Purpose:

- Identify attackers
- Track malicious sources

---

# 🥧 Dashboard 3 – Authentication Event Distribution

### Visualization

Pie Chart

Categories:

```text
ssh_success
ssh_failed
sudo_command
```

Purpose:

- Analyze authentication trends
- Understand system activity

---

# 📋 Security Dashboard Components

```text
┌────────────────────┐
│ Failed SSH Events  │
└────────────────────┘

┌────────────────────┐
│ Top Attacking IPs  │
└────────────────────┘

┌────────────────────┐
│ Event Distribution │
└────────────────────┘
```

---

# 📂 Suggested Project Structure

```text
siem-elk-lab/
│
├── elasticsearch/
│   └── elasticsearch.yml
│
├── logstash/
│   └── siem-pipeline.conf
│
├── kibana/
│   └── kibana.yml
│
├── wazuh/
│   └── ossec.conf
│
├── scripts/
│   ├── log_aggregator.py
│   ├── scheduler.py
│   └── report_generator.py
│
├── reports/
│   ├── security_report.json
│   ├── ssh_analysis.json
│   └── threat_summary.json
│
├── dashboards/
│   └── security_dashboard.json
│
└── README.md
```

---

# 📑 Expected Outcomes

After completing this lab, students will have:

✅ Fully Functional Elasticsearch Cluster

✅ Operational Logstash Pipeline

✅ Running Kibana Dashboard

✅ Integrated Wazuh Monitoring

✅ Automated Log Processing

✅ Python-Based Log Analysis

✅ Security Reporting Capability

✅ Centralized Log Management

---

# 🎓 Skills Gained

### 🛡️ SIEM Administration

### 🔍 Security Monitoring

### 📊 Log Analysis

### 🐍 Python Automation

### 📈 Dashboard Development

### 🚨 Threat Detection

### 🔄 Event Correlation

### 🔐 Security Operations

### 🌐 SOC Workflows

---

# 🛠️ Troubleshooting Guide

---

## ❌ Elasticsearch Won't Start

### Verify Memory Allocation

```bash
sudo nano /etc/elasticsearch/jvm.options
```

Check:

```text
-Xms2g
-Xmx2g
```

### Verify Disk Space

```bash
df -h
```

### Review Logs

```bash
sudo journalctl -u elasticsearch -n 50
```

---

## ❌ Logstash Not Processing Logs

### Verify Service

```bash
sudo systemctl status logstash
```

### Check Pipeline

```bash
sudo cat /etc/logstash/conf.d/siem-pipeline.conf
```

### Review Logs

```bash
sudo journalctl -u logstash -n 50
```

---

## ❌ Wazuh Not Sending Alerts

### Check Services

```bash
sudo systemctl status wazuh-manager
sudo systemctl status wazuh-agent
```

### Verify Log Files

```bash
ls -la /var/ossec/logs/alerts/
```

---

## ❌ Kibana Displays No Data

### Verify Indexes

```bash
curl localhost:9200/_cat/indices?v
```

### Check Time Filter

Expand dashboard range:

```text
Last 7 Days
```

### Verify Index Pattern

```text
siem-logs-*
```

---

## ❌ Python Script Errors

### Activate Virtual Environment

```bash
source siem-env/bin/activate
```

### Verify Elasticsearch

```bash
curl localhost:9200
```

### Check Dependencies

```bash
pip list
```

---

# 🌟 Real-World Applications

This project directly supports careers such as:

- 🛡️ SOC Analyst
- 🚨 Security Analyst
- 🔍 Threat Hunter
- 📊 SIEM Engineer
- 🔐 Security Engineer
- 🖥️ System Security Administrator
- 🌐 Cyber Defense Analyst

---

# 🏆 Key Takeaways

### 🔥 ELK Stack Centralizes Security Data

Provides scalable log collection and analysis.

### 🔥 Wazuh Adds Host-Based Detection

Enhances visibility into endpoint activity.

### 🔥 Automation Improves Efficiency

Python reduces manual analysis efforts.

### 🔥 Dashboards Improve Visibility

Visual analytics reveal patterns quickly.

### 🔥 SIEM Enables Threat Detection

Correlated events provide actionable security insights.

---

# 🎯 Conclusion

The **SIEM Setup with ELK Stack & Wazuh Lab** provides hands-on experience building a modern Security Information and Event Management platform.

Students learn how to:

✔️ Deploy Elasticsearch

✔️ Configure Logstash Pipelines

✔️ Build Kibana Dashboards

✔️ Integrate Wazuh Monitoring

✔️ Automate Log Processing

✔️ Analyze Security Events

✔️ Generate Threat Reports

✔️ Operate SIEM Infrastructure

These capabilities are essential for modern Security Operations Centers (SOC), cyber defense teams, and security engineers responsible for monitoring and protecting enterprise environments.

---

<div align="center">

## 🛡️ Collect Logs • 🔍 Detect Threats • 📊 Visualize Events • 🚨 Secure Systems

### ⭐ SIEM Setup with ELK Stack & Wazuh Lab ⭐

Build Visibility • Automate Analysis • Strengthen Security Operations

</div>
