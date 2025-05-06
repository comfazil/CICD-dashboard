# stage one: build
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


#copy installed packages and scripts
COPY log_analyzer.py .
COPY metrics/ ./metrics/

ENV PATH=/root/.local/bin:$PATH \
    LOG_FILE=/app/logs/project.log

RUN mkdir -p /app/logs

CMD ["python","log_analyzer.py"]
