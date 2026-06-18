# 🧪 Cuckoo Sandbox Analysis 

![Cuckoo](https://img.shields.io/badge/Tool-Cuckoo%20Sandbox-blue)
![Linux](https://img.shields.io/badge/OS-Ubuntu%2020.04-orange)
![Python](https://img.shields.io/badge/Language-Python%203.x-yellow)
![Focus](https://img.shields.io/badge/Focus-Dynamic%20Malware%20Analysis-critical)
![Level](https://img.shields.io/badge/Difficulty-Advanced-red)

---

# 🎯 Objectives

By the end of this lab, students will be able to:

🚀 Install and configure **Cuckoo Sandbox** for automated malware analysis  
🐍 Build Python automation scripts for sample submission & report retrieval  
🔎 Extract and analyze Indicators of Compromise (IoCs) from sandbox reports  
🧠 Interpret dynamic malware behavior for threat hunting  
📦 Implement batch analysis workflows for multiple samples  

---

# 📌 Prerequisites

Before starting, students should have:

🐧 Linux command-line basics  
🐍 Python programming fundamentals  
🦠 Malware analysis understanding  
📊 Familiarity with JSON data structures  

---

# 🖥️ Lab Environment

⚙️ **Al Nafi Cloud Machine**

You will get:

🧰 Ubuntu 20.04 (8GB RAM / 50GB Storage)  
🧪 Preconfigured analysis environment  
🖥️ VirtualBox + networking tools  
📡 Packet capture utilities  

👉 Click **Start Lab** to begin

---

# 🧩 Task 1: Install & Configure Cuckoo Sandbox

---

## ⚙️ Step 1.1: System Setup

```bash
# 🔄 Update system
sudo apt update && sudo apt upgrade -y

# 📦 Install dependencies
sudo apt install -y python3 python3-pip python3-venv mongodb postgresql
sudo apt install -y tcpdump libffi-dev libssl-dev libjpeg-dev
sudo apt install -y virtualbox-6.1

# 👤 Create cuckoo user
sudo adduser cuckoo --disabled-password --gecos ""
sudo usermod -a -G vboxusers,pcap cuckoo
🧪 Step 1.2: Cuckoo Environment Setup
sudo su - cuckoo

python3 -m venv cuckoo-env
source cuckoo-env/bin/activate

pip install --upgrade pip
pip install cuckoo

cuckoo init
🗄️ Step 1.3: PostgreSQL Configuration
sudo -u postgres createuser cuckoo
sudo -u postgres createdb cuckoo -O cuckoo
sudo -u postgres psql -c "ALTER USER cuckoo PASSWORD 'cuckoo123';"

Update config:

[database]
connection = postgresql://cuckoo:cuckoo123@localhost:5432/cuckoo
🌐 Step 1.4: Network Setup
# 📡 Packet capture permissions
sudo setcap cap_net_raw,cap_net_admin=eip /usr/sbin/tcpdump

# 🌐 VirtualBox network
sudo VBoxManage hostonlyif create
sudo VBoxManage hostonlyif ipconfig vboxnet0 --ip 192.168.56.1 --netmask 255.255.255.0
⚙️ Step 1.5: Cuckoo Configuration
[resultserver]
ip = 192.168.56.1
port = 2042

[processing]
analysis_timeout = 300
🧩 Task 2: Automation Scripts
🐍 Step 2.1: Sample Submission Script
cat > ~/cuckoo_submit.py << 'EOF'
#!/usr/bin/env python3
import os
import requests
import argparse

class CuckooSubmitter:
    def __init__(self, host="127.0.0.1", port=8090):
        self.base = f"http://{host}:{port}"

    def submit_file(self, file_path):
        if not os.path.exists(file_path):
            return None

        url = f"{self.base}/tasks/create/file"
        with open(file_path, "rb") as f:
            files = {"file": f}
            r = requests.post(url, files=files)

        if r.ok:
            return r.json().get("task_id")
        return None

    def submit_url(self, url):
        endpoint = f"{self.base}/tasks/create/url"
        r = requests.post(endpoint, data={"url": url})
        return r.json().get("task_id")

    def get_task_status(self, task_id):
        url = f"{self.base}/tasks/view/{task_id}"
        r = requests.get(url)
        return r.json().get("task", {}).get("status")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    parser.add_argument("--url")
    args = parser.parse_args()

    cuckoo = CuckooSubmitter()

    if args.file:
        print("Task ID:", cuckoo.submit_file(args.file))
    elif args.url:
        print("Task ID:", cuckoo.submit_url(args.url))

if __name__ == "__main__":
    main()
EOF
📊 Step 2.2: Report Analyzer
cat > ~/cuckoo_analyzer.py << 'EOF'
#!/usr/bin/env python3
import requests
import json
import time

class CuckooAnalyzer:
    def __init__(self, host="127.0.0.1", port=8090):
        self.base = f"http://{host}:{port}"

    def wait_for_completion(self, task_id):
        while True:
            r = requests.get(f"{self.base}/tasks/view/{task_id}")
            status = r.json()["task"]["status"]
            if status == "reported":
                return True
            time.sleep(30)

    def get_report(self, task_id):
        url = f"{self.base}/tasks/report/{task_id}"
        return requests.get(url).json()

    def extract_network_iocs(self, report):
        return {
            "ips": list(set(
                [c.get("dst") for c in report.get("network", {}).get("tcp", [])]
            )),
            "domains": report.get("network", {}).get("dns", [])
        }

    def extract_file_iocs(self, report):
        return {
            "md5": report.get("target", {}).get("file", {}).get("md5"),
            "sha256": report.get("target", {}).get("file", {}).get("sha256"),
            "dropped": report.get("dropped", [])
        }

def main():
    import sys
    task_id = sys.argv[1]

    analyzer = CuckooAnalyzer()
    report = analyzer.get_report(task_id)

    iocs = {
        "network": analyzer.extract_network_iocs(report),
        "files": analyzer.extract_file_iocs(report)
    }

    print(json.dumps(iocs, indent=4))

if __name__ == "__main__":
    main()
EOF
📦 Step 2.3: Batch Analyzer
cat > ~/batch_analyzer.py << 'EOF'
#!/usr/bin/env python3
import os
import glob
import requests

class BatchAnalyzer:
    def scan_directory(self, directory):
        return glob.glob(directory + "/**/*.exe", recursive=True)

    def submit_batch(self, files):
        tasks = []
        for f in files:
            r = requests.post(
                "http://127.0.0.1:8090/tasks/create/file",
                files={"file": open(f, "rb")}
            )
            tasks.append((f, r.json().get("task_id")))
        return tasks

def main():
    import sys
    folder = sys.argv[1]
    analyzer = BatchAnalyzer()

    files = analyzer.scan_directory(folder)
    tasks = analyzer.submit_batch(files)

    print("Submitted Tasks:")
    for t in tasks:
        print(t)

if __name__ == "__main__":
    main()
EOF
🧪 Step 2.4: Test Sample Generator
cat > ~/generate_test_samples.py << 'EOF'
#!/usr/bin/env python3
from pathlib import Path

out = Path("./test_samples")
out.mkdir(exist_ok=True)

(out/"test_script.ps1").write_text(
    "Write-Host 'Test malware analysis sample'"
)

(out/"network_test.py").write_text(
    "import socket\nsocket.gethostbyname('example.com')"
)

print("Samples generated:", list(out.iterdir()))
EOF
🧩 Task 3: Analysis Execution
🚀 Start Cuckoo Services
# 🧠 Daemon
cuckoo -d

# 🌐 Web UI
cuckoo web runserver 0.0.0.0:8080
📤 Submit Sample
python3 cuckoo_submit.py --file ./test_samples/test_script.ps1
📊 Analyze Report
python3 cuckoo_analyzer.py 1 | python3 -m json.tool
📦 Batch Processing
python3 batch_analyzer.py ./test_samples
📊 Expected Outcomes

✔ Fully working Cuckoo Sandbox environment
✔ Automated malware submission system
✔ Dynamic IoC extraction pipeline
✔ Batch analysis automation
✔ Structured JSON threat intelligence output

⚠️ Troubleshooting

❌ Cuckoo not starting → check PostgreSQL service
❌ No task created → verify API endpoint (port 8090)
❌ No network traffic → check VirtualBox host-only network
❌ Timeout errors → increase analysis timeout

🏁 Conclusion

You learned:

🧪 Dynamic malware analysis using Cuckoo Sandbox
🤖 Automation of malware submission pipelines
🔎 IoC extraction from runtime behavior
📊 Batch processing for large-scale analysis

🚀 Next Steps
Integrate with SIEM (Splunk / ELK)
Add YARA-based detection in pipeline
Extend with memory forensics (Volatility)
Build full threat intelligence platform
