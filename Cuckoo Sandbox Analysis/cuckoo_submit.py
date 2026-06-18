#!/usr/bin/env python3
"""
Cuckoo Sample Submission Script
Students: Complete the TODO sections to implement functionality
"""

import os
import sys
import json
import requests
import argparse

class CuckooSubmitter:
    def __init__(self, host="127.0.0.1", port=8090):
        """Initialize Cuckoo API connection"""
        self.base_url = f"http://{host}:{port}"
        self.session = requests.Session()
    
    def submit_file(self, file_path, options=None):
        """
        Submit a file for analysis
        
        Args:
            file_path: Path to the file to analyze
            options: Dictionary of analysis options
        
        Returns:
            Task ID if successful, None otherwise
        """
        # TODO: Check if file exists
        # TODO: Prepare the API endpoint URL
        # TODO: Open file and prepare multipart form data
        # TODO: Send POST request to Cuckoo API
        # TODO: Parse response and extract task_id
        # TODO: Return task_id or None on failure
        pass
    
    def submit_url(self, url, options=None):
        """
        Submit a URL for analysis
        
        Args:
            url: URL to analyze
            options: Dictionary of analysis options
        
        Returns:
            Task ID if successful, None otherwise
        """
        # TODO: Prepare API endpoint
        # TODO: Create data payload with URL
        # TODO: Send POST request
        # TODO: Return task_id from response
        pass
    
    def get_task_status(self, task_id):
        """
        Get the current status of a task
        
        Args:
            task_id: The task ID to check
        
        Returns:
            Status string or None
        """
        # TODO: Construct status check URL
        # TODO: Send GET request
        # TODO: Parse and return status
        pass

def main():
    parser = argparse.ArgumentParser(description='Submit samples to Cuckoo')
    parser.add_argument('--file', help='File to analyze')
    parser.add_argument('--url', help='URL to analyze')
    
    args = parser.parse_args()
    
    # TODO: Create CuckooSubmitter instance
    # TODO: Submit file or URL based on arguments
    # TODO: Print task ID

if __name__ == '__main__':
    main()
