# Evidence Collection and Live Memory Acquisition

## Overview

This lab introduces the principles and practices of digital forensic evidence collection and live memory acquisition in a Linux environment. Students will learn how to preserve volatile data, automate evidence gathering, analyze memory snapshots, and maintain proper chain-of-custody documentation throughout an investigation.

The lab combines Python automation with industry-standard forensic methodologies and tools such as Volatility 3 to simulate real-world incident response and forensic investigation workflows.

---

## Objectives

By completing this lab, students will learn how to:

- Perform live memory acquisition using forensic tools
- Implement automated evidence collection workflows with Python
- Analyze memory dumps using the Volatility framework
- Document chain of custody for digital evidence
- Apply incident response procedures for evidence preservation

---

## Prerequisites

Before beginning this lab, students should have:

- Basic Linux command line proficiency
- Understanding of operating system memory concepts
- Python programming fundamentals
- Familiarity with file systems and process management

---

## Lab Environment

Al Nafi provides pre-configured Linux cloud machines with all required tools installed.

### Included Components

- Ubuntu 22.04 LTS
- Python 3.10+
- Volatility 3 Framework
- Sample memory dumps
- Evidence files
- Pre-installed forensic utilities

---

# Project Structure

```text
forensic_lab/
│
├── memory_dumps/
├── evidence/
├── analysis/
├── scripts/
├── logs/
├── reports/
│
├── case_info.txt
│
└── scripts/
    ├── forensic_logger.py
    ├── memory_acquisition.py
    ├── evidence_collector.py
    ├── volatility_analyzer.py
    └── timeline_generator.py
```

---

# Task 1: Setting Up the Forensic Workspace

## Step 1.1: Verify Environment

```bash
python3 --version
vol.py --help | head -5
```

Create workspace:

```bash
mkdir -p ~/forensic_lab/{memory_dumps,evidence,analysis,scripts,logs,reports}
cd ~/forensic_lab
```

Initialize case documentation:

```bash
cat > case_info.txt << EOF
Case ID: LAB17-$(date +%Y%m%d)
Investigator: $(whoami)
Start Time: $(date)
Hostname: $(hostname)
EOF
```

---

## Step 1.2: Forensic Logger

### Purpose

The forensic logger provides:

- Chain of custody tracking
- Evidence acquisition logging
- Investigator activity auditing
- Timestamped forensic records

### Learning Outcomes

Students will:

- Configure forensic logging
- Record evidence collection actions
- Document investigator activities
- Maintain audit trails

### File

```text
scripts/forensic_logger.py
```

### Key Features

- File and console logging
- Evidence tracking
- SHA256 hash recording
- Timestamp preservation
- Chain-of-custody support

---

# Task 2: Live Memory Acquisition

## Purpose

Memory acquisition captures volatile system information before it is lost due to shutdown or reboot.

Collected information includes:

- Running processes
- Memory statistics
- System information
- Process command lines
- Memory utilization

---

## Step 2.1: Memory Acquisition Script

### File

```text
scripts/memory_acquisition.py
```

### Responsibilities

The script should:

#### Collect System Information

- Hostname
- Kernel version
- Architecture
- Memory statistics
- CPU information
- Boot time

#### Capture Process Information

- PID
- Process name
- Memory usage
- Command line arguments

#### Generate Memory Snapshot

- Save system state
- Store process information
- Create acquisition metadata

#### Verify Integrity

Calculate:

```text
SHA256 Hash
```

for every memory snapshot created.

---

## Expected Output

```text
memory_dumps/
├── memory_snapshot_20250715_120001.mem
├── memory_snapshot_20250715_120001.json
```

---

## Running Acquisition

```bash
python3 scripts/memory_acquisition.py
```

Verify output:

```bash
ls -lh memory_dumps/
sha256sum memory_dumps/*.mem
```

---

# Task 3: Automated Evidence Collection

## Purpose

Evidence collection automates gathering of forensic artifacts while maintaining integrity and documentation.

---

## Step 3.1: Evidence Collector

### File

```text
scripts/evidence_collector.py
```

---

### Evidence Categories

#### System Logs

Collect:

```text
/var/log/syslog
/var/log/auth.log
/var/log/kern.log
```

#### User Artifacts

Collect:

```text
~/.bash_history
~/.ssh/
```

#### Network Evidence

Collect:

```bash
ip addr show
ip route show
ss -tunap
```

#### File Timeline Data

Gather files modified within:

```text
Last 7 Days
```

---

### Evidence Integrity

Each collected artifact should include:

```json
{
  "filename": "auth.log",
  "size": 12345,
  "sha256": "HASH_VALUE",
  "collection_time": "TIMESTAMP"
}
```

---

## Manifest Generation

Generate:

```text
collection_manifest.json
```

containing:

- Case information
- Evidence summary
- Collection timestamps
- Hash values
- Investigator information

---

## Execute Collection

```bash
python3 scripts/evidence_collector.py
```

Review evidence:

```bash
CASE_DIR=$(ls -td ~/forensic_lab/evidence/case_* | head -1)

tree $CASE_DIR
```

View manifest:

```bash
cat $CASE_DIR/collection_manifest.json | python3 -m json.tool
```

---

# Task 4: Memory Analysis with Volatility

## Purpose

Volatility is used to analyze memory dumps and recover forensic artifacts.

---

## Step 4.1: Volatility Analysis Script

### File

```text
scripts/volatility_analyzer.py
```

---

## Analysis Objectives

### Profile Identification

Identify:

- Operating System
- Version
- Architecture

---

### Process Enumeration

Recover:

- Running processes
- Hidden processes
- Suspicious processes

Example plugins:

```bash
windows.pslist
linux.pslist
```

---

### Network Analysis

Recover:

- Active connections
- Listening ports
- Remote endpoints

Example plugins:

```bash
windows.netstat
linux.netstat
```

---

### Command History Recovery

Recover:

- Bash history
- Command-line arguments
- Executed commands

---

### File Object Analysis

Identify:

- Open files
- Deleted files
- Suspicious file references

---

## Generated Outputs

```text
analysis/
├── volatility_report.json
├── volatility_report.txt
├── processes.json
├── network_connections.json
└── command_history.json
```

---

## Execute Analysis

```bash
MEMORY_DUMP=$(ls -t ~/forensic_lab/memory_dumps/*.mem | head -1)

python3 scripts/volatility_analyzer.py $MEMORY_DUMP
```

Review results:

```bash
ls -lh ~/forensic_lab/analysis/
```

---

# Task 5: Timeline Analysis

## Purpose

Timeline analysis reconstructs system activity chronologically from collected evidence.

---

## Step 5.1: Timeline Generator

### File

```text
scripts/timeline_generator.py
```

---

## Timeline Sources

### System Logs

- syslog
- auth.log
- kern.log

### Process Events

- Process creation
- Process termination

### File Events

- File creation
- File modification
- File deletion

---

## Timeline Workflow

### Parse Evidence

Extract:

```text
Timestamp
Event Type
Source
Description
```

### Merge Events

Combine:

- Log events
- File events
- Process events

### Sort Chronologically

Create a unified forensic timeline.

---

## Example Timeline Entry

```json
{
  "timestamp": "2025-07-15T12:15:32",
  "source": "auth.log",
  "event": "Failed SSH Login",
  "details": "User root from 10.0.0.5"
}
```

---

## Generated Reports

```text
analysis/
└── timeline_report.txt
```

---

## Execute Timeline Generation

```bash
EVIDENCE_DIR=$(ls -td ~/forensic_lab/evidence/case_* | head -1)

python3 scripts/timeline_generator.py $EVIDENCE_DIR
```

Review report:

```bash
cat ~/forensic_lab/analysis/timeline_report_*.txt | less
```

---

# Expected Outcomes

Upon successful completion of this lab, students should have:

✅ Memory snapshots with SHA256 verification

✅ Automated evidence collection workflows

✅ Complete chain-of-custody documentation

✅ Volatility-based memory analysis results

✅ Process and network forensic artifacts

✅ Timeline reconstruction of system events

✅ Incident investigation reports

---

# Verification Checklist

## Review Generated Files

```bash
cd ~/forensic_lab

find . -type f \
-name "*.json" \
-o -name "*.txt" \
-o -name "*.mem" | head -20
```

---

## Review Forensic Logs

```bash
tail -50 logs/forensic_activity_*.log
```

---

## Review Evidence Manifest

```bash
cat evidence/case_*/collection_manifest.json | python3 -m json.tool
```

---

# Troubleshooting Tips

## Issue: Permission Denied While Collecting Logs

### Solution

Some logs require elevated privileges:

```bash
sudo cp /var/log/auth.log .
```

or run:

```bash
sudo python3 scripts/evidence_collector.py
```

---

## Issue: Memory Snapshot Is Empty

### Solution

Verify:

```bash
pip3 install psutil
```

Check available disk space:

```bash
df -h
```

---

## Issue: Volatility Analysis Fails

### Solution

Verify installation:

```bash
vol.py --help
```

Check dump file:

```bash
file memory_dump.mem
```

Review script logs for errors.

---

## Issue: Timeline Report Contains No Events

### Solution

Verify:

```bash
tree evidence/
```

Ensure:

- Log files were collected
- Timeline data exists
- JSON files are valid

Validate JSON:

```bash
python3 -m json.tool file.json
```

---

# Skills Gained

After completing this lab, students will be able to:

### Digital Forensics

- Evidence preservation
- Chain of custody management
- Memory acquisition

### Incident Response

- Evidence collection
- Investigation workflows
- Documentation procedures

### Memory Analysis

- Volatility framework usage
- Process analysis
- Network artifact recovery

### Automation

- Python forensic scripting
- Evidence collection automation
- Timeline generation

---

# Conclusion

This lab provided practical experience in forensic evidence collection, memory acquisition, and memory analysis using Python and Volatility. Students developed automated workflows for collecting and preserving evidence, maintained proper chain-of-custody records, analyzed memory artifacts, and reconstructed system activity through timeline generation.

These skills are essential for digital forensic investigators, SOC analysts, incident responders, and cybersecurity professionals responsible for preserving and analyzing evidence during security investigations.

---

# Next Steps

- Explore advanced Volatility 3 plugins
- Practice with real-world memory images
- Study malware memory analysis techniques
- Learn forensic artifact triage methodologies
- Integrate forensic workflows with SIEM platforms
- Build automated incident response playbooks
