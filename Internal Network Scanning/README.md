# 🛡️ Internal Network Scanning 

<div align="center">

![Cybersecurity](https://img.shields.io/badge/Domain-Cybersecurity-red?style=for-the-badge&logo=shield&logoColor=white)
![Nmap](https://img.shields.io/badge/Tool-Nmap-4B8BBE?style=for-the-badge&logo=linux&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-✓-005571?style=for-the-badge&logo=elasticsearch&logoColor=white)
![Kibana](https://img.shields.io/badge/Kibana-✓-E8478B?style=for-the-badge&logo=kibana&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04_LTS-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

> **A comprehensive hands-on lab for mastering internal network vulnerability assessment, automation, and data visualization.**

</div>

---

## 🎯 Learning Objectives

By the end of this lab, you will be able to:

- 🔍 Understand the fundamentals of internal network scanning and its importance in cybersecurity
- 🗺️ Perform comprehensive internal network scans using **Nmap** with various scanning techniques
- 🐍 Create and execute **Python scripts** to automate vulnerability scanning processes
- 📊 Analyze scanning results using **Kibana** for effective data visualization and threat assessment
- 🚨 Identify common network vulnerabilities and security weaknesses in internal infrastructure
- ✅ Implement best practices for internal network reconnaissance and vulnerability assessment

---

## 📋 Prerequisites

Before starting this lab, ensure you have:

| Requirement | Description |
|---|---|
| 🌐 Networking Concepts | Basic understanding of IP addresses, ports, and protocols |
| 💻 Linux CLI | Familiarity with the Linux command-line interface |
| 🐍 Python Basics | Basic knowledge of Python programming |
| 🔐 Cybersecurity Fundamentals | Understanding of core security concepts |
| ✏️ Text Editors | Experience with text editors in Linux environment |

---

## 🖥️ Lab Environment Setup

![Al Nafi](https://img.shields.io/badge/Platform-Al_Nafi_Cloud-0078D7?style=flat-square&logo=cloud&logoColor=white)
![Single Machine](https://img.shields.io/badge/Setup-Single_Machine-green?style=flat-square)

> 💡 This lab runs entirely on a **single Linux-based cloud machine** provided by Al Nafi. Simply click **Start Lab** to access your pre-configured environment. No additional VM setup or configuration is required.

### 🔧 Pre-installed Tools

| Tool | Version | Purpose |
|---|---|---|
| ![Ubuntu](https://img.shields.io/badge/-Ubuntu-E95420?logo=ubuntu&logoColor=white) | 20.04 LTS | Operating System |
| ![Nmap](https://img.shields.io/badge/-Nmap-4B8BBE?logo=linux&logoColor=white) | Latest | Network Scanner |
| ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) | 3.8+ | Scripting & Automation |
| ![Elasticsearch](https://img.shields.io/badge/-Elasticsearch-005571?logo=elasticsearch&logoColor=white) | Latest | Data Indexing |
| ![Kibana](https://img.shields.io/badge/-Kibana-E8478B?logo=kibana&logoColor=white) | Latest | Data Visualization |
| 📦 Python Libraries | — | Required Dependencies |
| 🌐 Sample Services | — | Test Network Services |

---

## 📌 Task 1: Perform Internal Network Scans Using Nmap

![Nmap](https://img.shields.io/badge/Tool-Nmap-4B8BBE?style=flat-square&logo=linux&logoColor=white)
![Network Discovery](https://img.shields.io/badge/Type-Network_Discovery-orange?style=flat-square)

### 🔎 Subtask 1.1 — Basic Network Discovery

> Identify the network range and discover active hosts on the internal network.

---

#### 🪜 Step 1 — Check Your Network Configuration

```bash
ip addr show
```

---

#### 🪜 Step 2 — Identify Your Network Range

Look for the `inet` address in the output — typically something like `192.168.1.0/24` or `10.0.0.0/24`.

---

#### 🪜 Step 3 — Perform a Basic Ping Sweep

```bash
nmap -sn 192.168.1.0/24
```

> ⚠️ **Note:** Replace `192.168.1.0/24` with your actual network range identified in Step 2.

---

#### 🪜 Step 4 — Save Results to a File

```bash
nmap -sn 192.168.1.0/24 > network_discovery.txt
```

---

### 🔌 Subtask 1.2 — Port Scanning Techniques

> Perform various types of port scans to identify open services.

---

#### 🪜 Step 1 — Basic TCP SYN Scan

```bash
nmap -sS 192.168.1.1-254
```

---

#### 🪜 Step 2 — Service Version Detection Scan

```bash
nmap -sV -O 192.168.1.1-254
```

---

#### 🪜 Step 3 — UDP Service Scan

```bash
sudo nmap -sU --top-ports 100 192.168.1.1-254
```

---

#### 🪜 Step 4 — Aggressive Scan with Script Engine

```bash
nmap -A -T4 192.168.1.1-254
```

---

### 🐛 Subtask 1.3 — Targeted Vulnerability Scanning

![NSE](https://img.shields.io/badge/Feature-Nmap_Scripting_Engine-purple?style=flat-square)

> Use Nmap's scripting engine (NSE) to identify specific vulnerabilities.

---

#### 🪜 Step 1 — Update Nmap Script Database

```bash
sudo nmap --script-updatedb
```

---

#### 🪜 Step 2 — Scan for Common Vulnerabilities

```bash
nmap --script vuln 192.168.1.1-254
```

---

#### 🪜 Step 3 — Scan for SSH Vulnerabilities

```bash
nmap --script ssh-* 192.168.1.1-254 -p 22
```

---

#### 🪜 Step 4 — Create a Comprehensive Scan Report

```bash
nmap -A -T4 --script vuln -oA comprehensive_scan 192.168.1.1-254
```

> 📁 This creates three output files:
> - `comprehensive_scan.nmap`
> - `comprehensive_scan.xml`
> - `comprehensive_scan.gnmap`

---

## 🐍 Task 2: Create Python Script for Automated Vulnerability Scanning

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![Automation](https://img.shields.io/badge/Type-Automation-green?style=flat-square)

### 📦 Subtask 2.1 — Install Required Python Libraries

---

#### 🪜 Step 1 — Install Dependencies

```bash
pip3 install python-nmap requests beautifulsoup4 elasticsearch
```

---

#### 🪜 Step 2 — Verify Installation

```bash
python3 -c "import nmap; print('python-nmap installed successfully')"
```

---

### 💻 Subtask 2.2 — Create the Vulnerability Scanner Script

---

#### 🪜 Step 1 — Create the Script File

```bash
nano vulnerability_scanner.py
```

---

#### 🪜 Step 2 — Add the Vulnerability Scanner Code

```python
#!/usr/bin/env python3

import nmap
import json
import datetime
import subprocess
import re
import socket
from elasticsearch import Elasticsearch
import argparse
import sys

class VulnerabilityScanner:
    def __init__(self, target_range, output_file="scan_results.json"):
        self.target_range = target_range
        self.output_file = output_file
        self.nm = nmap.PortScanner()
        self.results = {
            "scan_info": {
                "timestamp": datetime.datetime.now().isoformat(),
                "target_range": target_range,
                "scanner_version": "1.0"
            },
            "hosts": []
        }
        
    def discover_hosts(self):
        """Discover active hosts in the network"""
        print(f"[+] Discovering hosts in range: {self.target_range}")
        try:
            self.nm.scan(hosts=self.target_range, arguments='-sn')
            active_hosts = []
            
            for host in self.nm.all_hosts():
                if self.nm[host].state() == 'up':
                    active_hosts.append(host)
                    print(f"[+] Found active host: {host}")
                    
            return active_hosts
        except Exception as e:
            print(f"[-] Error during host discovery: {e}")
            return []
    
    def port_scan(self, host):
        """Perform comprehensive port scan on a host"""
        print(f"[+] Scanning ports on {host}")
        try:
            self.nm.scan(host, arguments='-sV -sC -O -T4 --top-ports 1000')
            
            host_info = {
                "ip": host,
                "hostname": self.get_hostname(host),
                "state": self.nm[host].state(),
                "ports": [],
                "os_info": self.get_os_info(host),
                "vulnerabilities": []
            }
            
            for protocol in self.nm[host].all_protocols():
                ports = self.nm[host][protocol].keys()
                for port in ports:
                    port_info = self.nm[host][protocol][port]
                    host_info["ports"].append({
                        "port": port,
                        "protocol": protocol,
                        "state": port_info['state'],
                        "service": port_info.get('name', 'unknown'),
                        "version": port_info.get('version', 'unknown'),
                        "product": port_info.get('product', 'unknown')
                    })
            
            return host_info
            
        except Exception as e:
            print(f"[-] Error scanning {host}: {e}")
            return None
    
    def get_hostname(self, ip):
        """Get hostname for IP address"""
        try:
            return socket.gethostbyaddr(ip)[0]
        except:
            return "unknown"
    
    def get_os_info(self, host):
        """Extract OS information from scan results"""
        try:
            if 'osmatch' in self.nm[host]:
                os_matches = self.nm[host]['osmatch']
                if os_matches:
                    return {
                        "name": os_matches[0]['name'],
                        "accuracy": os_matches[0]['accuracy']
                    }
        except:
            pass
        return {"name": "unknown", "accuracy": "0"}
    
    def vulnerability_scan(self, host):
        """Perform vulnerability scanning using Nmap scripts"""
        print(f"[+] Running vulnerability scans on {host}")
        vulnerabilities = []
        
        try:
            vuln_scan = self.nm.scan(host, arguments='--script vuln')
            
            if host in vuln_scan['scan']:
                host_data = vuln_scan['scan'][host]
                if 'tcp' in host_data:
                    for port in host_data['tcp']:
                        port_data = host_data['tcp'][port]
                        if 'script' in port_data:
                            for script_name, script_output in port_data['script'].items():
                                if 'vuln' in script_name.lower() or 'cve' in script_output.lower():
                                    vulnerabilities.append({
                                        "port": port,
                                        "script": script_name,
                                        "output": script_output,
                                        "severity": self.assess_severity(script_output)
                                    })
                                    
        except Exception as e:
            print(f"[-] Error during vulnerability scan of {host}: {e}")
            
        return vulnerabilities
    
    def assess_severity(self, script_output):
        """Assess vulnerability severity based on script output"""
        output_lower = script_output.lower()
        
        if any(keyword in output_lower for keyword in ['critical', 'remote code execution', 'rce']):
            return "CRITICAL"
        elif any(keyword in output_lower for keyword in ['high', 'privilege escalation', 'authentication bypass']):
            return "HIGH"
        elif any(keyword in output_lower for keyword in ['medium', 'information disclosure', 'denial of service']):
            return "MEDIUM"
        else:
            return "LOW"
    
    def scan_network(self):
        """Main scanning function"""
        print("[+] Starting comprehensive network vulnerability scan")
        
        active_hosts = self.discover_hosts()
        
        if not active_hosts:
            print("[-] No active hosts found")
            return
        
        for host in active_hosts:
            print(f"\n[+] Scanning host: {host}")
            
            host_info = self.port_scan(host)
            if host_info:
                vulnerabilities = self.vulnerability_scan(host)
                host_info["vulnerabilities"] = vulnerabilities
                
                self.results["hosts"].append(host_info)
                
                print(f"[+] Host {host} scan complete:")
                print(f"    - Open ports: {len(host_info['ports'])}")
                print(f"    - Vulnerabilities found: {len(vulnerabilities)}")
        
        self.save_results()
        self.print_summary()
    
    def save_results(self):
        """Save scan results to JSON file"""
        try:
            with open(self.output_file, 'w') as f:
                json.dump(self.results, f, indent=2)
            print(f"[+] Results saved to {self.output_file}")
        except Exception as e:
            print(f"[-] Error saving results: {e}")
    
    def print_summary(self):
        """Print scan summary"""
        print("\n" + "="*50)
        print("SCAN SUMMARY")
        print("="*50)
        
        total_hosts = len(self.results["hosts"])
        total_ports = sum(len(host["ports"]) for host in self.results["hosts"])
        total_vulns = sum(len(host["vulnerabilities"]) for host in self.results["hosts"])
        
        print(f"Hosts scanned: {total_hosts}")
        print(f"Open ports found: {total_ports}")
        print(f"Vulnerabilities identified: {total_vulns}")
        
        severity_count = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0}
        for host in self.results["hosts"]:
            for vuln in host["vulnerabilities"]:
                severity_count[vuln["severity"]] += 1
        
        print("\nVulnerability Severity Breakdown:")
        for severity, count in severity_count.items():
            print(f"  {severity}: {count}")
    
    def send_to_elasticsearch(self, es_host="localhost", es_port=9200):
        """Send results to Elasticsearch for Kibana analysis"""
        try:
            es = Elasticsearch([{'host': es_host, 'port': es_port}])
            index_name = f"vulnerability-scan-{datetime.datetime.now().strftime('%Y-%m-%d')}"
            
            for host in self.results["hosts"]:
                doc = {
                    "timestamp": self.results["scan_info"]["timestamp"],
                    "host_ip": host["ip"],
                    "hostname": host["hostname"],
                    "os_info": host["os_info"],
                    "total_ports": len(host["ports"]),
                    "total_vulnerabilities": len(host["vulnerabilities"]),
                    "ports": host["ports"],
                    "vulnerabilities": host["vulnerabilities"]
                }
                
                es.index(index=index_name, body=doc)
            
            print(f"[+] Results sent to Elasticsearch index: {index_name}")
            
        except Exception as e:
            print(f"[-] Error sending to Elasticsearch: {e}")


def main():
    parser = argparse.ArgumentParser(description="Automated Vulnerability Scanner")
    parser.add_argument("target", help="Target IP range (e.g., 192.168.1.0/24)")
    parser.add_argument("-o", "--output", default="scan_results.json", help="Output file")
    parser.add_argument("--elasticsearch", action="store_true", help="Send results to Elasticsearch")
    
    args = parser.parse_args()
    
    if not re.match(r'^(\d{1,3}\.){3}\d{1,3}/\d{1,2}$', args.target):
        print("[-] Invalid target format. Use CIDR notation (e.g., 192.168.1.0/24)")
        sys.exit(1)
    
    scanner = VulnerabilityScanner(args.target, args.output)
    scanner.scan_network()
    
    if args.elasticsearch:
        scanner.send_to_elasticsearch()


if __name__ == "__main__":
    main()
```

---

#### 🪜 Step 3 — Make the Script Executable

```bash
chmod +x vulnerability_scanner.py
```

---

### 🧪 Subtask 2.3 — Test the Vulnerability Scanner

---

#### 🪜 Step 1 — Run the Scanner

```bash
python3 vulnerability_scanner.py 192.168.1.0/24 -o network_scan_results.json
```

---

#### 🪜 Step 2 — View Results

```bash
cat network_scan_results.json | python3 -m json.tool | head -50
```

---

#### 🪜 Step 3 — Create a Results Parser Script

```bash
nano parse_results.py
```

Add the following code:

```python
#!/usr/bin/env python3

import json
import sys

def parse_scan_results(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        
        print("VULNERABILITY SCAN REPORT")
        print("=" * 50)
        print(f"Scan Date: {data['scan_info']['timestamp']}")
        print(f"Target Range: {data['scan_info']['target_range']}")
        print(f"Total Hosts Scanned: {len(data['hosts'])}")
        print()
        
        for host in data['hosts']:
            print(f"Host: {host['ip']} ({host['hostname']})")
            print(f"  OS: {host['os_info']['name']}")
            print(f"  Open Ports: {len(host['ports'])}")
            print(f"  Vulnerabilities: {len(host['vulnerabilities'])}")
            
            if host['vulnerabilities']:
                print("  Critical Issues:")
                for vuln in host['vulnerabilities']:
                    if vuln['severity'] in ['CRITICAL', 'HIGH']:
                        print(f"    - Port {vuln['port']}: {vuln['script']}")
            print()
            
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 parse_results.py <results_file.json>")
        sys.exit(1)
    
    parse_scan_results(sys.argv[1])
```

---

#### 🪜 Step 4 — Make Parser Executable and Run It

```bash
chmod +x parse_results.py
python3 parse_results.py network_scan_results.json
```

---

## 📊 Task 3: Analyze Results with Kibana

![Elasticsearch](https://img.shields.io/badge/Elasticsearch-005571?style=flat-square&logo=elasticsearch&logoColor=white)
![Kibana](https://img.shields.io/badge/Kibana-E8478B?style=flat-square&logo=kibana&logoColor=white)

### ⚙️ Subtask 3.1 — Start Elasticsearch and Kibana Services

---

#### 🪜 Step 1 — Start Elasticsearch

```bash
sudo systemctl start elasticsearch
sudo systemctl enable elasticsearch
```

---

#### 🪜 Step 2 — Verify Elasticsearch is Running

```bash
curl -X GET "localhost:9200/"
```

---

#### 🪜 Step 3 — Start Kibana

```bash
sudo systemctl start kibana
sudo systemctl enable kibana
```

---

#### 🪜 Step 4 — Check Kibana Status

```bash
sudo systemctl status kibana
```

> ⏳ **Note:** Kibana may take a few minutes to fully start up.

---

### 🗂️ Subtask 3.2 — Configure Kibana for Vulnerability Data

---

#### 🪜 Step 1 — Access Kibana Web Interface

Open a web browser and navigate to:

```
http://localhost:5601
```

---

#### 🪜 Step 2 — Send Scan Results to Elasticsearch

```bash
python3 vulnerability_scanner.py 192.168.1.0/24 --elasticsearch
```

---

#### 🪜 Step 3 — Navigate to Index Patterns

In Kibana, go to **Management → Stack Management → Index Patterns**.

---

#### 🪜 Step 4 — Create Index Pattern

Click **Create index pattern** and enter:

```
vulnerability-scan-*
```

---

#### 🪜 Step 5 — Set Time Field

Select `timestamp` as the time field and click **Create index pattern**.

---

### 📈 Subtask 3.3 — Create Vulnerability Dashboards

---

#### 🪜 Step 1 — Explore Data in Discover

Navigate to **Analytics → Discover** and select your vulnerability index pattern.

---

#### 🪜 Step 2 — Go to Visualize Library

Navigate to **Analytics → Visualize Library**.

---

#### 🪜 Step 3 — Create a Pie Chart (Severity Distribution)

```
➤ Click "Create visualization"
➤ Select "Pie"
➤ Choose your index pattern
➤ In Buckets → Add "Split slices"
   ├── Aggregation: Terms
   └── Field: vulnerabilities.severity.keyword
```

---

#### 🪜 Step 4 — Create a Bar Chart (Ports by Host)

```
➤ Create new visualization
➤ Select "Vertical Bar"
➤ Y-axis: Count
➤ X-axis: Terms aggregation on host_ip.keyword
```

---

#### 🪜 Step 5 — Create a Data Table

```
➤ Create new visualization
➤ Select "Data Table"
➤ Add metrics and buckets as needed
```

---

### 🖥️ Subtask 3.4 — Build a Comprehensive Dashboard

---

#### 🪜 Step 1 — Go to Dashboard

Navigate to **Analytics → Dashboard**.

---

#### 🪜 Step 2 — Create Dashboard

Click **Create dashboard**.

---

#### 🪜 Step 3 — Add Visualizations

Click **Add** and select your saved visualizations.

---

#### 🪜 Step 4 — Arrange & Save

Arrange the visualizations and save the dashboard as:

> **"Network Vulnerability Assessment"**

---

### 🔍 Subtask 3.5 — Create Advanced Queries and Filters

![KQL](https://img.shields.io/badge/Query_Language-KQL-E8478B?style=flat-square&logo=kibana&logoColor=white)

---

#### 🪜 Step 1 — Filter by Severity

```kql
vulnerabilities.severity: "CRITICAL" OR vulnerabilities.severity: "HIGH"
```

---

#### 🪜 Step 2 — Find Hosts with Specific Open Ports

```kql
ports.port: 22 OR ports.port: 80 OR ports.port: 443
```

---

#### 🪜 Step 3 — Search for Specific Services

```kql
ports.service: "ssh" OR ports.service: "http"
```

---

#### 🪜 Step 4 — Save Useful Queries

Save queries you'll reuse for future assessments via the **Save** option in the Discover tab.

---

## 🛠️ Troubleshooting Tips

### ⚠️ Common Issues and Solutions

| ❌ Issue | ✅ Solution |
|---|---|
| **Nmap permission denied** | Run with `sudo` when root privileges are required |
| **Python libraries not found** | Verify correct Python/pip version with `python3 --version` and `pip3 --version` |
| **Elasticsearch connection refused** | Check status: `sudo systemctl status elasticsearch` |
| **Kibana not accessible** | Edit config: `sudo nano /etc/kibana/kibana.yml` — set `server.host` to `"0.0.0.0"` |
| **No vulnerabilities found** | Update scripts with `sudo nmap --script-updatedb` and try different targets |

---

### ⚡ Performance Optimization

**For Large Networks:**

```bash
# Use faster timing template
nmap -T4   # or -T5 for even faster

# Limit port range for speed
nmap --top-ports 100

# Host discovery first, then port scan
nmap -sn 192.168.1.0/24
```

**For Better Results:**
- 🕐 Run scans during off-peak hours
- 🔀 Use different scan techniques for different services
- 🔧 Combine multiple scanning tools for comprehensive coverage

---

## 🏁 Conclusion

### ✅ What You've Accomplished

| Achievement | Description |
|---|---|
| 🗺️ **Network Scanning Mastery** | Used Nmap effectively for network discovery, port scanning, and vulnerability detection |
| 🤖 **Automated Assessment** | Built a Python script that automates vulnerability scanning — efficient and repeatable |
| 📊 **Data Visualization** | Configured Kibana to transform raw scan results into actionable intelligence |

---

### 🌍 Why This Matters

Internal network scanning is a critical component of a comprehensive cybersecurity strategy. Regular internal vulnerability assessments help organizations:

- 🔓 **Identify Security Gaps** — Discover unpatched systems, misconfigured services, and unnecessary open ports
- 🚧 **Prevent Lateral Movement** — Limit an attacker's ability to move through the network after initial compromise
- 📜 **Ensure Compliance** — Meet regulatory requirements for regular security assessments
- 🎯 **Prioritize Resources** — Focus security efforts on the most critical vulnerabilities

---

### 🚀 Real-World Career Applications

| 👤 Role | 💼 How This Lab Applies |
|---|---|
| 🔎 **Security Analyst** | Regular vulnerability assessments and threat hunting |
| 🧪 **Penetration Tester** | Internal network reconnaissance and vulnerability exploitation |
| 🏛️ **Cyber Defense Architect** | Designing comprehensive security monitoring and assessment programs |
| 🚨 **Incident Responder** | Understanding network topology and potential attack vectors |

---

<div align="center">

![Cybersecurity](https://img.shields.io/badge/Stay_Ethical-Hack_Responsibly-red?style=for-the-badge&logo=shield&logoColor=white)
![Al Nafi](https://img.shields.io/badge/Powered_By-Al_Nafi-0078D7?style=for-the-badge)

*Built with ❤️ for the next generation of cybersecurity professionals*

</div>
