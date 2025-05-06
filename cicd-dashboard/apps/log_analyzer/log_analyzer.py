#!/usr/bin/env python3
import os
import sys
from datetime import datetime

# Add parent directory to sys.path to fix import error
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from metrics.fetcher import fetch_metrics

#LOG_FILE = os.path.expanduser("/home/fazilk/Desktop/DevOps/cicd-dashboard/apps/log_analyzer/logs/project.log")

def get_log_path():
    """Determine the correct log file location with fallbacks"""
    # Priority 1: Environment variable
    if 'LOG_FILE' in os.environ:
        return os.environ['LOG_FILE']
    
    # 2. Sibling 'logs' folder (../logs/project.log) #this path is being used
    script_dir = os.path.dirname(__file__)
    sibling_logs_path = os.path.join(script_dir, '../logs/project.log')  # <-- Key change
    if os.path.exists(sibling_logs_path):
        return os.path.abspath(sibling_logs_path)  # Convert to absolute path
    
    # Priority 3: Development location
    dev_path = os.path.join(os.path.dirname(__file__), '../../../logs/project.log')
    if os.path.exists(dev_path):
        return dev_path
    
    # Priority 4: Last resort - current directory
    return 'project.log'


def analyze_logs():
    log_file = get_log_path()
    if not os.path.exists(log_file):
        print(f"[ERROR] Log file not found at: {log_file}")
        print("Searched in:")
        print(f"- Environment LOG_FILE: {os.environ.get('LOG_FILE', 'Not set')}")
        print(f"- Docker default path: /app/logs/project.log")
        print(f"- Local logs path: {os.path.join(os.path.dirname(__file__), 'logs/project.log')}")
        print(f"- Project root path: {os.path.join(os.path.dirname(__file__), '../../../logs/project.log')}")
        print(f"- Current directory: project.log")
        return

    with open(log_file, "r") as f:
        logs = f.readlines()

    error_count = sum("error" in line.lower() for line in logs)
    print(f"Log Analysis Report ({datetime.now()}):")
    print(f"- Total entries: {len(logs)}")
    print(f"- Errors detected: {error_count}")

    #Categorizing errors
    severity = {
        "CRITICAL" : sum("critical" in line.lower() for line in logs),
        "WARNING" : sum("warning" in line.lower() for line in logs),
        "INFO": sum("info" in line.lower() for line in logs),
        "FATAL": sum("fatal" in line.lower() for line in logs)
        }
    
    print(f"\nSeverity Breakdown:")
    
    for level, count in severity.items():
        print(f"- {level}: {count}")
         
    #cicd-metrics
    pipelines = fetch_metrics()
    failed_pipelines = sum(1 for p in pipelines if p["status"] == "failed")

    print(f"\nCI/CD Metrics:")
    print(f"- Failed pipelines: {failed_pipelines}/{len(pipelines)}")
    print(f"- Avg duration: {sum(float(p['duration_sec']) for p in pipelines)/len(pipelines):.1f}s")

if __name__ == "__main__":
    analyze_logs()
