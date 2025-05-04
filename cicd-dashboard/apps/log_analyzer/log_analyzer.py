#!/usr/bin/env python3
import os
import sys
from datetime import datetime

# Add parent directory to sys.path to fix import error
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from metrics.fetcher import fetch_metrics

LOG_FILE = os.path.expanduser("/home/fazilk/Desktop/DevOps/project.log")

def analyze_logs():
    if not os.path.exists(LOG_FILE):
        print("[ERROR] Log file not found")
        return

    with open(LOG_FILE, "r") as f:
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
