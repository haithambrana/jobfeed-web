FROM python:3.12-slim

WORKDIR /app

COPY jobfeed /app/jobfeed
COPY jobfeed-web/app.py /app/app.py
COPY jobfeed-web/templates /app/templates
COPY jobfeed-web/data /app/data
COPY jobfeed-web/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

ENV JOBFEED_PATH=/app/jobfeed
EXPOSE 8001
CMD ["python", "app.py"]
