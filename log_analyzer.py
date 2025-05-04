#!/usr/bin/env python3
import os
from datetime import datetime

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
		"WARNING" : sum("warning" in line.lower() for line in logs)
		}
    print(f"\nSeverity Breakdown:")
    for level, count in severity.items():
	print(f"- {level}: {count}")

if __name__ == "__main__":
    analyze_logs()
