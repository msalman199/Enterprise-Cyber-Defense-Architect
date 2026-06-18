#!/usr/bin/env python3
"""
Test Sample Generator
Creates harmless test files for analysis practice
"""

import os
import zipfile
from pathlib import Path

class TestSampleGenerator:
    def __init__(self, output_dir="./test_samples"):
        """Initialize generator"""
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
    
    def create_suspicious_script(self):
        """Create a PowerShell test script"""
        script = '''# Harmless test script
Write-Host "Test analysis sample"
Get-Process | Select-Object -First 5
$env:TEMP
'''
        filepath = self.output_dir / "test_script.ps1"
        # TODO: Write script to file
        # TODO: Return filepath
        pass
    
    def create_network_sample(self):
        """Create Python script that makes network requests"""
        script = '''#!/usr/bin/env python3
import socket
import time

# Harmless network test
try:
    socket.gethostbyname("example.com")
    print("Network test completed")
except:
    pass
'''
        filepath = self.output_dir / "network_test.py"
        # TODO: Write script to file
        # TODO: Make executable
        # TODO: Return filepath
        pass
    
    def create_document_sample(self):
        """Create a test document"""
        filepath = self.output_dir / "test_doc.zip"
        # TODO: Create simple ZIP file
        # TODO: Add text content
        # TODO: Return filepath
        pass

def main():
    # TODO: Create generator instance
    # TODO: Generate all test samples
    # TODO: Print created files
    pass

if __name__ == '__main__':
    main()
