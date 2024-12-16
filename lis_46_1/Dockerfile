FROM python:3.12-slim
WORKDIR /app/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY echo.py .
ENTRYPOINT ["python", "echo.py"]
