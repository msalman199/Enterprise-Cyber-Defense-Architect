# 🛡️ IDS/IPS Configuration (Snort & Suricata)

<div align="center">

# 🚨 Intrusion Detection & Prevention Systems

### 🔍 Hands-On Security Monitoring with Snort, Suricata, Elastic Stack, and Python

![Linux](https://img.shields.io/badge/Linux-Ubuntu%2022.04-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Snort](https://img.shields.io/badge/Snort-IDS%2FIPS-red?style=for-the-badge)
![Suricata](https://img.shields.io/badge/Suricata-Network%20Security-orange?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-Automation-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-Analytics-005571?style=for-the-badge&logo=elasticsearch&logoColor=white)
![Kibana](https://img.shields.io/badge/Kibana-Visualization-005571?style=for-the-badge&logo=kibana&logoColor=white)
![Logstash](https://img.shields.io/badge/Logstash-Data%20Pipeline-005571?style=for-the-badge)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Detection-green?style=for-the-badge)

</div>

---

# 📖 Project Overview

This project provides practical experience in deploying, configuring, and managing **Intrusion Detection and Prevention Systems (IDS/IPS)** using two of the industry's most popular open-source security platforms:

- 🚨 Snort 3
- 🚨 Suricata

Students learn how to:

- Install enterprise-grade IDS solutions
- Create custom detection rules
- Generate attack traffic for testing
- Analyze security events
- Visualize alerts using the Elastic Stack
- Compare IDS performance and detection capabilities

This lab simulates real-world Security Operations Center (SOC) workflows and provides hands-on exposure to network threat detection technologies.

---

# 🎯 Learning Objectives

By completing this lab, students will be able to:

### 🛡️ IDS/IPS Deployment

- Install Snort 3
- Install Suricata
- Configure detection engines
- Manage IDS rule sets

### 🔍 Threat Detection

- Detect network scans
- Identify web attacks
- Monitor suspicious traffic
- Analyze security events

### 🐍 Python Security Automation

- Generate detection rules automatically
- Manage IDS signatures
- Create attack simulations
- Automate reporting

### 📊 Security Analytics

- Configure Elasticsearch
- Configure Logstash
- Configure Kibana
- Visualize security alerts

### ⚡ Performance Analysis

- Compare Snort and Suricata
- Measure resource consumption
- Evaluate detection effectiveness
- Analyze operational efficiency

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| 🛡️ Snort 3 | Intrusion Detection & Prevention |
| 🚨 Suricata | Network Threat Detection |
| 🐍 Python | Security Automation |
| 📊 Elasticsearch | Security Data Storage |
| 📈 Kibana | Alert Visualization |
| 🔄 Logstash | Log Processing |
| 🖥️ Ubuntu 22.04 LTS | Operating System |
| 🌐 Nmap | Network Scanning |
| 🔍 Regular Expressions | Signature Development |
| 📁 JSON | Reporting & Analytics |

---

# 📋 Prerequisites

Before starting this project, students should have:

### 🌐 Networking Knowledge

- TCP/IP Fundamentals
- Common Network Protocols
- Packet Flow Concepts
- Network Security Basics

### 🖥️ Linux Skills

- Linux Command Line
- File Permissions
- Service Management
- Package Installation

### 🐍 Programming Skills

- Python Basics
- Functions
- Classes
- File Handling
- JSON Processing

### 🔐 Security Knowledge

- IDS/IPS Concepts
- Security Monitoring
- Threat Detection Fundamentals
- Network Security Operations

---

# 🏗️ Project Architecture

```text
                    ┌───────────────────────┐
                    │   Network Traffic     │
                    └──────────┬────────────┘
                               │
                               ▼
          ┌─────────────────────────────────────┐
          │      Snort & Suricata IDS/IPS       │
          └───────────────┬─────────────────────┘
                          │
            ┌─────────────┴─────────────┐
            ▼                           ▼
     Detection Rules             Security Alerts
            │                           │
            ▼                           ▼
      Python Scripts              Log Collection
                                        │
                                        ▼
                            ┌───────────────────┐
                            │     Logstash      │
                            └─────────┬─────────┘
                                      │
                                      ▼
                            ┌───────────────────┐
                            │ Elasticsearch     │
                            └─────────┬─────────┘
                                      │
                                      ▼
                            ┌───────────────────┐
                            │      Kibana       │
                            └───────────────────┘
```

---

# 🚀 Lab Tasks

---

# 🛡️ Task 1 – Install & Configure IDS Platforms

## 🎯 Purpose

Deploy and configure Snort and Suricata in a production-style environment.

### 🔹 Activities

✅ Install dependencies

✅ Install Snort 3

✅ Install Suricata

✅ Configure IDS directories

✅ Create logging infrastructure

✅ Configure rule management

### 🔹 Skills Learned

- IDS Installation
- Service Configuration
- Rule Management
- Security Monitoring Setup

---

# 🐍 Task 2 – Custom Rule Development with Python

## 🎯 Purpose

Automate IDS rule creation and management.

### 🔹 Detection Categories

### 🚨 Web Attack Detection

- SQL Injection
- Cross-Site Scripting (XSS)
- Directory Traversal

### 🚨 Network Scanning

- Port Scanning
- Ping Sweeps

### 🚨 Malware Detection

- Encoded PowerShell Commands
- Suspicious File Downloads

### 🔹 Python Components

```text
SnortRuleGenerator
│
├── Web Attack Rules
├── Network Scan Rules
├── Malware Rules
└── Rule Export Functions
```

### 🔹 Skills Learned

- Signature Development
- Threat Detection Logic
- Python Automation
- Rule Management

---

# 📜 Task 3 – Rule Management System

## 🎯 Purpose

Validate, analyze, and manage IDS signatures.

### 🔹 Features

✅ Rule Loading

✅ Rule Validation

✅ SID Extraction

✅ Statistics Generation

✅ JSON Reporting

### 🔹 Analysis Metrics

- Total Rules
- Protocol Distribution
- Action Types
- Rule Categories
- Validation Results

---

# 📊 Task 4 – Elastic Stack Integration

## 🎯 Purpose

Centralize and visualize security alerts.

### Components

#### 🔍 Elasticsearch

Stores IDS events and alerts.

#### 🔄 Logstash

Processes Snort and Suricata logs.

#### 📈 Kibana

Visualizes security analytics.

---

# 🔹 Security Dashboard Features

### 📊 Alert Trends

Track alert volume over time.

### 🚨 Top Alert Types

Identify most common threats.

### 🌍 Source IP Distribution

Visualize attacker activity.

### 🌐 Protocol Analysis

Analyze protocol usage.

---

# 🚨 Task 5 – Attack Traffic Generation

## 🎯 Purpose

Generate realistic attack traffic for IDS testing.

### Attack Simulations

#### 🔥 SQL Injection

```text
?id=1' OR '1'='1
```

#### 🔥 Cross-Site Scripting

```html
<script>alert(1)</script>
```

#### 🔥 Directory Traversal

```text
../../../../etc/passwd
```

#### 🔥 Port Scanning

```text
Nmap SYN Scan
```

#### 🔥 ICMP Sweeps

```text
Multiple Ping Requests
```

### Skills Learned

- IDS Validation
- Attack Simulation
- Detection Testing
- Alert Verification

---

# ⚡ Task 6 – Performance Comparison

## 🎯 Purpose

Compare Snort and Suricata performance.

### Evaluation Metrics

| Metric | Description |
|----------|------------|
| CPU Usage | Resource Consumption |
| Memory Usage | RAM Utilization |
| Alert Count | Detection Volume |
| Detection Rate | Threat Coverage |
| Processing Speed | Traffic Analysis Performance |

---

# 📈 Comparison Goals

### 🛡️ Snort

- Signature-Based Detection
- Flexible Rule Language
- Lightweight Operation

### 🚨 Suricata

- Multi-Threaded Architecture
- High-Speed Processing
- Advanced Protocol Detection

---

# 📂 Suggested Project Structure

```text
ids-ips-lab/
│
├── rules/
│   ├── local.rules
│   ├── custom.rules
│   └── generated.rules
│
├── python/
│   ├── rule_generator.py
│   ├── rule_manager.py
│   ├── traffic_generator.py
│   └── ids_comparator.py
│
├── configs/
│   ├── snort.lua
│   ├── suricata.yaml
│   └── logstash.conf
│
├── reports/
│   ├── rule_report.json
│   ├── detection_report.json
│   └── performance_report.json
│
├── logs/
│   ├── snort/
│   └── suricata/
│
└── README.md
```

---

# 📑 Expected Outcomes

After completing this lab, students will have:

✅ Fully Operational Snort IDS

✅ Fully Operational Suricata IDS

✅ Custom Detection Signatures

✅ Automated Rule Generation Scripts

✅ Centralized Security Monitoring

✅ Kibana Dashboards

✅ Threat Detection Capabilities

✅ Performance Benchmark Reports

---

# 🎓 Skills Gained

### 🛡️ IDS/IPS Deployment

### 🔍 Signature Development

### 🐍 Python Security Automation

### 📊 Security Analytics

### 🚨 Threat Detection

### 📈 Log Visualization

### 🌐 Network Security Monitoring

### ⚡ Performance Evaluation

### 🔐 Security Operations

---

# 🛠️ Troubleshooting Guide

---

## ❌ Snort Won't Start

### Verify Configuration

```bash
snort -c /usr/local/etc/snort/snort.lua -T
```

### Check Interface

```bash
ip link show
```

### Verify Rule Files

```bash
ls -la /usr/local/etc/snort/rules
```

---

## ❌ Elasticsearch Connection Failed

### Check Status

```bash
sudo systemctl status elasticsearch
```

### Verify Port

```bash
netstat -tlnp | grep 9200
```

### Review Logs

```bash
sudo tail -f /var/log/elasticsearch/ids-lab.log
```

---

## ❌ No Alerts Generated

### Verify IDS Status

```bash
ps aux | grep snort
```

### Confirm Rules Loaded

```bash
snort -c snort.lua --rule-to-text
```

### Check Log Permissions

```bash
ls -la /var/log/snort
```

---

## ❌ Kibana Not Accessible

### Verify Service

```bash
sudo systemctl status kibana
```

### Check Port

```bash
netstat -tlnp | grep 5601
```

### Allow Startup Time

```text
Kibana may require 2–3 minutes to initialize.
```

---

# 🌟 Real-World Applications

This project directly supports careers in:

- 🛡️ SOC Analyst
- 🚨 Threat Hunter
- 🔍 Incident Responder
- 🌐 Security Engineer
- 📈 Security Monitoring Specialist
- 🕵️ Cybersecurity Analyst
- 🔐 Network Security Administrator

---

# 🏆 Key Takeaways

### 🔥 Detection Requires Tuning

IDS solutions must balance detection accuracy with false positives.

### 🔥 Custom Rules Improve Visibility

Organizations can detect unique threats through custom signatures.

### 🔥 Centralized Monitoring Matters

Elastic Stack enhances visibility and incident investigation.

### 🔥 Performance Impacts Security

Resource consumption influences IDS deployment strategy.

### 🔥 Automation Improves Efficiency

Python scripting streamlines security operations.

---

# 🎯 Conclusion

The **IDS/IPS Configuration Lab (Snort & Suricata)** provides comprehensive experience in deploying, managing, and optimizing modern intrusion detection systems.

Students gain practical skills in:

✔️ IDS Installation

✔️ Threat Detection

✔️ Signature Development

✔️ Python Security Automation

✔️ Elastic Stack Integration

✔️ Alert Analysis

✔️ Security Monitoring

✔️ Performance Benchmarking

These capabilities are essential for modern Security Operations Centers (SOC), threat detection teams, and cybersecurity professionals responsible for protecting enterprise environments.

---

<div align="center">

## 🛡️ Detect Threats • 🚨 Monitor Attacks • 📊 Analyze Alerts • 🔐 Secure Networks

### ⭐ IDS/IPS Configuration Lab – Snort & Suricata ⭐

If you found this project useful, consider giving it a ⭐ on GitHub.

</div>
