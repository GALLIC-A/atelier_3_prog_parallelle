FROM python:3.10-slim
WORKDIR /app
COPY worker.py
COPY requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "worker.py"]