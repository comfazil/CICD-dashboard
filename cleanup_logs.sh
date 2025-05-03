#!/bin/bash

PROJECT_DIR="/home/fazilk/Desktop/DevOps"
LOG_DIR="$PROJECT_DIR/logs"
MAX_DAYS=7
PROJECT_LOG="$PROJECT_DIR/project.log"

echo "[INFO] Cleaning up logs older than $MAX_DAYS days in $LOG_DIR"
find $LOG_DIR -type f -name "*.log" -mtime +$MAX_DAYS -delete

if [ -f "$PROJECT_LOG" ]; then
	echo "[INFO] Archiving project log..."
	gzip -c "$PROJECT_LOG" > "$PROJECT_LOG-$(date +%Y%m%d).gz"
	> "$PROJECT_LOG"
fi

echo "[SUCCESS] Log cleanup completed for project at $PROJECT_DIR"
