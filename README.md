# AI-Powered CI/CD Dashboard

## Day 1: Set up git and github repo.
## Day 2: Wrote bash and python scripts. Pushed them to github repo.
Stored token into local machine at ~/.get-credentials.
We can automate this script to run daily at midnight by using
[
crontab -e
0 0 * * * /home/fazilk/Desktop/DevOps/cleanup_logs.sh
]
Executed log analyzer python script via log cleanup bash script.

## 📅 Day 3: Git Hooks Implementation
✅ Completed
Pre-commit Hook (.git/hooks/pre-commit)

Blocks commits when errors >5
Shows severity breakdown (CRITICAL/WARNING)
Enhanced log_analyzer.py

Added severity classification
Improved output formatting

## Day 4: 
Added git branches (dev, feature, stage)
Restructured the project

## Day 5:
Wrote a script (fetcher.py) to fetch fake CI/CD metrics from MockAPI
Integrated it with log_analyzer.py
Enhanced `log_analyzer.py` to show:  
   - Failed pipeline count  
   - Average duration  

## Day 6:
Dockerization
Built image and a container from that image.
Executed successfully.
Current project structure :
![image](https://github.com/user-attachments/assets/fe4840a8-2663-4199-a213-43503fa8bc40)



