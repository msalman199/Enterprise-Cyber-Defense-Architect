# 🕵️ Social Engineering and Reconnaissance 

<div align="center">

![Cybersecurity](https://img.shields.io/badge/Domain-Cybersecurity-red?style=for-the-badge&logo=shield&logoColor=white)
![Gobuster](https://img.shields.io/badge/Tool-Gobuster-4B8BBE?style=for-the-badge&logo=linux&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-005571?style=for-the-badge&logo=elasticsearch&logoColor=white)
![Kibana](https://img.shields.io/badge/Kibana-E8478B?style=for-the-badge&logo=kibana&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04_LTS-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

> **A comprehensive hands-on lab for mastering DNS enumeration, phishing awareness simulation, social engineering assessment, and reconnaissance data analysis.**

</div>

---

> ⚖️ **Ethics Warning:** All activities must be performed **only in authorized, controlled environments**. Unauthorized reconnaissance is **illegal**.

---

## 🎯 Learning Objectives

By the end of this lab, you will be able to:

- 🔍 Perform **DNS enumeration** and directory discovery using **Gobuster**
- 🐍 Create **Python scripts** for phishing awareness simulations
- 📊 Analyze reconnaissance data using **Elasticsearch** and **Kibana**
- 🧠 Identify **social engineering** attack vectors and indicators
- ✅ Implement ethical reconnaissance techniques in controlled environments

---

## 📋 Prerequisites

Before starting this lab, ensure you have:

| Requirement | Description |
|---|---|
| 💻 Linux CLI | Basic Linux command line proficiency |
| 🐍 Python Basics | Fundamental Python programming skills |
| 🌐 Networking | Understanding of DNS, HTTP/HTTPS concepts |
| ⚖️ Cybersecurity Ethics | Knowledge of legal and ethical boundaries |
| 🖥️ Web Technologies | Familiarity with web technologies |

---

## 🖥️ Lab Environment Setup

![Al Nafi](https://img.shields.io/badge/Platform-Al_Nafi_Cloud-0078D7?style=flat-square&logo=cloud&logoColor=white)
![Single Machine](https://img.shields.io/badge/Setup-Single_Machine-green?style=flat-square)

> 💡 Click **Start Lab** to access your pre-configured **Ubuntu 20.04** environment — no additional setup required.

### 🔧 Pre-installed Tools

| Tool | Purpose |
|---|---|
| ![Gobuster](https://img.shields.io/badge/-Gobuster-4B8BBE?logo=linux&logoColor=white) | Directory and DNS enumeration |
| ![Python](https://img.shields.io/badge/-Python_3.8+-3776AB?logo=python&logoColor=white) | Scripting with required libraries |
| ![Elasticsearch](https://img.shields.io/badge/-Elasticsearch-005571?logo=elasticsearch&logoColor=white) | Reconnaissance data indexing |
| ![Kibana](https://img.shields.io/badge/-Kibana-E8478B?logo=kibana&logoColor=white) | Data visualization and dashboards |
| ![Apache](https://img.shields.io/badge/-Apache2-D22128?logo=apache&logoColor=white) | Web server for testing |

---

## 📌 Task 1: DNS and Directory Enumeration with Gobuster

![Gobuster](https://img.shields.io/badge/Tool-Gobuster-4B8BBE?style=flat-square&logo=linux&logoColor=white)
![Apache](https://img.shields.io/badge/Server-Apache2-D22128?style=flat-square&logo=apache&logoColor=white)
![Enumeration](https://img.shields.io/badge/Phase-Enumeration-blue?style=flat-square)

### 🏗️ Step 1 — Setup Test Environment

Create a local web environment for safe testing:

```bash
# Create test directories
sudo mkdir -p /var/www/html/testsite/{admin,backup,config,api}

# Create test files
echo "<h1>Main Page</h1>" | sudo tee /var/www/html/testsite/index.html
echo "<h1>Admin Panel</h1>" | sudo tee /var/www/html/testsite/admin/index.html
echo "<h1>Backup Area</h1>" | sudo tee /var/www/html/testsite/backup/index.html

# Start Apache
sudo systemctl start apache2
sudo systemctl enable apache2
```

---

### 📋 Step 2 — Create Custom Wordlists

Generate wordlists for enumeration:

```bash
# Create directory wordlist
cat > /tmp/dir-wordlist.txt << EOF
admin
backup
config
api
test
dev
uploads
private
secure
dashboard
login
EOF

# Create subdomain wordlist
cat > /tmp/subdomain-wordlist.txt << EOF
www
mail
ftp
admin
dev
test
api
staging
EOF
```

---

### 🔍 Step 3 — Perform Directory Enumeration

Execute Gobuster scans:

```bash
# Basic directory scan
gobuster dir -u http://localhost/testsite -w /tmp/dir-wordlist.txt

# Scan with file extensions
gobuster dir -u http://localhost/testsite -w /tmp/dir-wordlist.txt -x php,html,txt,js

# Advanced scan with status codes
gobuster dir -u http://localhost/testsite -w /usr/share/wordlists/dirb/common.txt -s "200,204,301,302,307,401,403" -x php,html
```

---

### 📊 Step 4 — Analyze Results

Document your findings:

```bash
# Save results to file
gobuster dir -u http://localhost/testsite -w /tmp/dir-wordlist.txt -o /tmp/gobuster-results.txt

# Review discovered paths
cat /tmp/gobuster-results.txt

# Identify sensitive directories (admin, backup, config)
grep -E "(admin|backup|config)" /tmp/gobuster-results.txt
```

> 📝 **Expected Output:** List of discovered directories with HTTP status codes. Identify which paths represent security risks.

---

## 🎣 Task 2: Phishing Awareness Simulation Script

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![Phishing](https://img.shields.io/badge/Topic-Phishing_Awareness-orange?style=flat-square)
![OWASP](https://img.shields.io/badge/OWASP-Social_Engineering-black?style=flat-square&logo=owasp&logoColor=white)

### 📄 Step 1 — Create Phishing Simulator Template

Save as `/tmp/phishing_simulator.py`:

```python
#!/usr/bin/env python3
"""
Phishing Awareness Simulation Tool
Educational purposes only - simulates phishing campaigns for training
"""

import json
import datetime
import logging

class PhishingSimulator:
    def __init__(self):
        """Initialize the phishing simulator"""
        self.setup_logging()
        self.templates = {}
        self.results = []
    
    def setup_logging(self):
        """Configure logging for simulation tracking"""
        # TODO: Setup logging to file and console
        # TODO: Use INFO level for general messages
        pass
    
    def create_email_templates(self):
        """
        Create phishing email templates for awareness training
        
        Returns:
            dict: Dictionary of email templates with subjects and bodies
        """
        # TODO: Create at least 3 different phishing templates
        # TODO: Include urgent_security, prize_notification, software_update
        # TODO: Each template should have 'subject' and 'body' keys
        # TODO: Mark clearly as SIMULATION in each template
        pass
    
    def analyze_phishing_indicators(self, template_content):
        """
        Analyze email content for phishing indicators
        
        Args:
            template_content: String containing email subject and body
        
        Returns:
            list: List of identified phishing indicators
        """
        indicators = []
        
        # TODO: Check for urgency words (urgent, immediate, critical)
        # TODO: Check for reward/prize mentions (won, prize, free)
        # TODO: Check for action requests (click, download, verify)
        # TODO: Append found indicators to list
        
        return indicators
    
    def calculate_risk_level(self, indicators):
        """
        Calculate risk level based on number of indicators
        
        Args:
            indicators: List of phishing indicators
        
        Returns:
            str: Risk level (HIGH, MEDIUM, LOW)
        """
        # TODO: Return HIGH if 4+ indicators
        # TODO: Return MEDIUM if 2-3 indicators
        # TODO: Return LOW if 0-1 indicators
        pass
    
    def simulate_campaign(self, target_list):
        """
        Simulate phishing campaign without sending actual emails
        
        Args:
            target_list: List of target email addresses
        
        Returns:
            list: Campaign results with analysis
        """
        # TODO: Loop through templates and targets
        # TODO: Analyze each template for indicators
        # TODO: Create result dictionary with timestamp, target, indicators, risk
        # TODO: Return list of all results
        pass
    
    def generate_report(self, results):
        """
        Generate awareness training report
        
        Args:
            results: List of simulation results
        
        Returns:
            dict: Comprehensive report with recommendations
        """
        # TODO: Calculate summary statistics
        # TODO: Count high/medium/low risk templates
        # TODO: Add security recommendations
        # TODO: Save report to JSON file
        pass

def main():
    # TODO: Initialize simulator
    # TODO: Create test target list
    # TODO: Run simulation campaign
    # TODO: Generate and display report
    pass

if __name__ == "__main__":
    main()
```

---

### 🛠️ Step 2 — Implement Core Functions

Complete the template by implementing:

```
➤ Email Templates    — Create 3 realistic phishing scenarios
➤ Indicator Analysis — Detect urgency, rewards, and action requests
➤ Risk Calculation   — Classify templates by risk level (HIGH / MEDIUM / LOW)
➤ Report Generation  — Output JSON report with all findings
```

---

### ▶️ Step 3 — Execute and Analyze

Run your completed script:

```bash
# Make executable
chmod +x /tmp/phishing_simulator.py

# Execute simulation
python3 /tmp/phishing_simulator.py

# Review results
cat /tmp/phishing_report.json | python3 -m json.tool
```

> 📝 **Expected Output:** JSON report showing simulated campaigns, phishing indicators detected, risk levels, and security recommendations.

---

## 🧠 Task 3: Social Engineering Assessment Tool

![SE Assessment](https://img.shields.io/badge/Topic-Social_Engineering-red?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![Risk Scoring](https://img.shields.io/badge/Feature-Risk_Scoring-orange?style=flat-square)

### 📄 Step 1 — Create Assessment Framework

Save as `/tmp/se_assessment.py`:

```python
#!/usr/bin/env python3
"""
Social Engineering Assessment Tool
Evaluates organizational vulnerability to social engineering attacks
"""

import json
import datetime

class SEAssessment:
    def __init__(self):
        """Initialize assessment tool"""
        self.scenarios = {}
        self.results = []
    
    def create_scenarios(self):
        """
        Create social engineering attack scenarios
        
        Returns:
            dict: Dictionary of SE scenarios with details
        """
        # TODO: Create scenarios for:
        # - phone_pretexting (IT support impersonation)
        # - email_spoofing (fake executive emails)
        # - physical_tailgating (unauthorized building access)
        # - usb_baiting (malicious USB drops)
        
        # TODO: Each scenario should include:
        # - name, description, tactics, risk_factors, mitigation
        pass
    
    def assess_vulnerability(self, scenario_id, responses):
        """
        Assess vulnerability level for a scenario
        
        Args:
            scenario_id: Identifier for the scenario
            responses: User responses to assessment questions
        
        Returns:
            int: Vulnerability score (1-10)
        """
        # TODO: Analyze user responses
        # TODO: Calculate vulnerability score
        # TODO: Consider scenario-specific risk factors
        pass
    
    def generate_recommendations(self, assessment_results):
        """
        Generate training recommendations based on assessment
        
        Args:
            assessment_results: List of scenario assessment results
        
        Returns:
            list: Prioritized training recommendations
        """
        # TODO: Identify high-risk scenarios (score >= 7)
        # TODO: Identify medium-risk scenarios (score 4-6)
        # TODO: Create recommendations with priority, focus areas, timeline
        pass
    
    def run_assessment(self, user_id):
        """
        Execute complete assessment for a user
        
        Args:
            user_id: Identifier for the user being assessed
        
        Returns:
            dict: Complete assessment report
        """
        # TODO: Loop through all scenarios
        # TODO: Collect responses (simulate for testing)
        # TODO: Calculate vulnerability scores
        # TODO: Generate recommendations
        # TODO: Create and save comprehensive report
        pass

def main():
    # TODO: Initialize assessment tool
    # TODO: Run assessment for test users
    # TODO: Display summary results
    pass

if __name__ == "__main__":
    main()
```

---

### 🛠️ Step 2 — Implement Assessment Logic

Complete the assessment tool with:

```
➤ Scenario Creation      — Define 4 SE attack scenarios
➤ Vulnerability Scoring  — Implement scoring algorithm (1–10)
➤ Recommendations        — Generate prioritized training plans
➤ Reporting              — Save detailed JSON reports
```

---

### ▶️ Step 3 — Run Assessment

Execute the assessment:

```bash
chmod +x /tmp/se_assessment.py
python3 /tmp/se_assessment.py

# Review assessment results
ls -l /tmp/se_assessment_*.json
cat /tmp/se_assessment_employee_001.json | python3 -m json.tool
```

---

## 📊 Task 4: Reconnaissance Data Analysis with Kibana

![Elasticsearch](https://img.shields.io/badge/Elasticsearch-005571?style=flat-square&logo=elasticsearch&logoColor=white)
![Kibana](https://img.shields.io/badge/Kibana-E8478B?style=flat-square&logo=kibana&logoColor=white)
![KQL](https://img.shields.io/badge/Query_Language-KQL-E8478B?style=flat-square)

### ⚙️ Step 1 — Setup Elasticsearch and Kibana

Configure the ELK stack:

```bash
# Start Elasticsearch
sudo systemctl start elasticsearch
sudo systemctl enable elasticsearch

# Start Kibana
sudo systemctl start kibana
sudo systemctl enable kibana

# Wait for services
sleep 30

# Verify Elasticsearch
curl -X GET "localhost:9200/"

# Kibana will be available at http://localhost:5601
```

---

### 🔧 Step 2 — Generate Reconnaissance Data

Save as `/tmp/recon_data_gen.py`:

```python
#!/usr/bin/env python3
"""
Reconnaissance Data Generator
Creates sample data for Kibana analysis
"""

import json
import datetime
import random
from elasticsearch import Elasticsearch

class ReconDataGenerator:
    def __init__(self):
        """Initialize data generator and connect to Elasticsearch"""
        # TODO: Connect to Elasticsearch on localhost:9200
        # TODO: Verify connection with ping()
        pass
    
    def generate_port_scan_data(self, num_records=50):
        """
        Generate port scan reconnaissance data
        
        Args:
            num_records: Number of records to generate
        
        Returns:
            list: Port scan event records
        """
        # TODO: Generate records with:
        # - timestamp, event_type, source_ip, target_ip
        # - target_port, protocol, scan_type, status
        # - tool_used, severity
        pass
    
    def generate_dns_enum_data(self, num_records=30):
        """
        Generate DNS enumeration data
        
        Args:
            num_records: Number of records to generate
        
        Returns:
            list: DNS enumeration event records
        """
        # TODO: Generate records with:
        # - timestamp, event_type, query_domain, query_type
        # - response_code, tool_used, success
        pass
    
    def generate_web_recon_data(self, num_records=40):
        """
        Generate web reconnaissance data
        
        Args:
            num_records: Number of records to generate
        
        Returns:
            list: Web reconnaissance event records
        """
        # TODO: Generate records with:
        # - timestamp, event_type, target_url, http_method
        # - status_code, user_agent, tool_used
        pass
    
    def index_data(self, index_name, data):
        """
        Index data into Elasticsearch
        
        Args:
            index_name: Name of the Elasticsearch index
            data: List of records to index
        """
        # TODO: Loop through data records
        # TODO: Index each record using es.index()
        # TODO: Handle errors appropriately
        pass
    
    def generate_all_data(self):
        """Generate and index all reconnaissance data types"""
        # TODO: Generate port scan data
        # TODO: Generate DNS enumeration data
        # TODO: Generate web reconnaissance data
        # TODO: Index all data into Elasticsearch
        pass

def main():
    # TODO: Initialize generator
    # TODO: Generate all data types
    # TODO: Confirm data indexed successfully
    pass

if __name__ == "__main__":
    main()
```

---

### 📡 Step 3 — Index Data and Create Visualizations

Generate and visualize data:

```bash
# Install Python Elasticsearch client
pip3 install elasticsearch

# Run data generator
python3 /tmp/recon_data_gen.py

# Verify data in Elasticsearch
curl -X GET "localhost:9200/_cat/indices?v"
curl -X GET "localhost:9200/recon-data/_count"
```

---

### 🖥️ Step 4 — Analyze in Kibana

Access Kibana and create visualizations:

```
➤ Open Kibana:
   └── Navigate to http://localhost:5601

➤ Create Index Pattern:
   └── Management → Index Patterns → Create pattern for recon-data*

➤ Explore Data:
   └── Discover → View reconnaissance events

➤ Create Visualizations:
   ├── Bar chart   — Event types distribution
   ├── Line chart  — Events over time
   ├── Pie chart   — Severity levels
   └── Data table  — Top targeted IPs

➤ Build Dashboard:
   └── Combine visualizations into security dashboard
```

**Analysis Tasks:**

```
➤ Identify most common reconnaissance techniques
➤ Detect patterns in timing and targeting
➤ Correlate different reconnaissance activities
➤ Assess overall security posture
```

---

## 🏁 Expected Outcomes

Upon completing this lab, you should have:

| ✅ Outcome | Description |
|---|---|
| 🔍 **Gobuster Enumeration** | Successfully enumerated directories with scan results |
| 🎣 **Phishing Simulator** | Functional phishing awareness simulation tool |
| 🧠 **SE Assessment Tool** | Social engineering vulnerability assessment capabilities |
| 📊 **Kibana Dashboard** | Generated and analyzed reconnaissance data with visualizations |
| 🛡️ **Detection Knowledge** | Understanding of reconnaissance techniques and detection methods |

### 📦 Deliverables

| File | Description |
|---|---|
| `/tmp/gobuster-results.txt` | Gobuster scan results showing discovered paths |
| `/tmp/phishing_report.json` | Phishing simulation report in JSON format |
| `/tmp/se_assessment_*.json` | Social engineering assessment reports |
| Kibana Dashboard | Reconnaissance visualization dashboard |

---

## 🛠️ Troubleshooting Tips

### ⚠️ Common Issues and Solutions

| ❌ Issue | ✅ Solution |
|---|---|
| **Gobuster wordlists missing** | Run `sudo apt install wordlists` or use custom lists from the lab |
| **Gobuster connection refused** | Verify Apache is running: `sudo systemctl status apache2` |
| **Python import errors** | Install missing libraries: `pip3 install <library>` |
| **Permission denied on scripts** | Make executable: `chmod +x script.py` |
| **Elasticsearch not starting** | Check logs: `/var/log/elasticsearch/` |
| **Kibana not starting** | Check logs: `/var/log/kibana/` |
| **Index not appearing in Kibana** | Wait 30–60 seconds after data generation before refreshing |

---

## 📖 Conclusion

### ✅ What You've Accomplished

| Achievement | Description |
|---|---|
| 🔍 **Systematic Enumeration** | Performed directory discovery using industry-standard Gobuster tool |
| 🎣 **Phishing Simulation** | Simulated social engineering attacks for awareness training |
| 📊 **Enterprise Data Analysis** | Analyzed security data using Elasticsearch and Kibana |
| 🧠 **Human Layer Assessment** | Identified vulnerabilities in both technical and human security layers |

---

### 🔑 Key Takeaways

| 💡 Principle | Details |
|---|---|
| 🗺️ **Recon is the Foundation** | Reconnaissance is the first and most critical phase of any security assessment |
| 🧠 **Human Psychology** | Social engineering exploits human psychology, not just technology |
| 📊 **Data Reveals Patterns** | Analysis uncovers patterns that are invisible when looking at individual events |
| ⚖️ **Ethics are Paramount** | Authorization and ethical boundaries are non-negotiable in all activities |

---

### 🚀 Next Steps

- 🧪 Practice on authorized platforms like **HackTheBox** or **TryHackMe**
- 🔧 Expand scripts to handle more complex scenarios
- 📚 Learn advanced Kibana query languages (**KQL**)
- 📖 Study real-world social engineering case studies

---

> ⚠️ **Remember:** Use these skills **only** for authorized security testing and educational purposes. Unauthorized reconnaissance and social engineering are **illegal and unethical**.

---

<div align="center">

![HackTheBox](https://img.shields.io/badge/Practice-HackTheBox-9FEF00?style=for-the-badge&logo=hackthebox&logoColor=black)
![TryHackMe](https://img.shields.io/badge/Practice-TryHackMe-212C42?style=for-the-badge&logo=tryhackme&logoColor=white)
![Ethical Hacking](https://img.shields.io/badge/Stay_Ethical-Hack_Responsibly-red?style=for-the-badge&logo=shield&logoColor=white)
![Al Nafi](https://img.shields.io/badge/Powered_By-Al_Nafi-0078D7?style=for-the-badge)

*Built with ❤️ for the next generation of cybersecurity professionals*

</div>
