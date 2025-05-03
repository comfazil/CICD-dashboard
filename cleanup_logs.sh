#!/bin/bash

PROJECT_DIR="/home/fazilk/Desktop/DevOps"
LOG_DIR="$PROJECT_DIR/logs"
MAX_DAYS=7
PROJECT_LOG="$PROJECT_DIR/project.log"
LOG_ANALYZER="$PROJECT_DIR/log_analyzer.py"

mkdir -p "$LOG_DIR"

echo "[INFO] Running log analysis..."
if [ -f "$LOG_ANALYZER" ]; then
	python3 "$LOG_ANALYZER" || {
	echo "[ERROR] Log analysis failed! Check for errors."
	exit 1
	}
else
	echo "[WARNING] log_analyzer.py not found. Skipping analysis."
fi

echo "[INFO] Cleaning up logs older than $MAX_DAYS days in $LOG_DIR"
find $LOG_DIR -type f -name "*.log" -mtime +$MAX_DAYS -delete

if [ -f "$PROJECT_LOG" ]; then
	echo "[INFO] Archiving project log..."
	gzip -c "$PROJECT_LOG" > "$PROJECT_LOG-$(date +%Y%m%d).gz"
	> "$PROJECT_LOG"
fi

echo "[SUCCESS] Log cleanup completed for project at $PROJECT_DIR"
