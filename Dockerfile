FROM python:3.11-bookworm

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV PORT=8080 PYTHONUNBUFFERED=1

# run as non-root
RUN useradd -m appuser
USER appuser

EXPOSE 8080
CMD ["python", "main.py"]
