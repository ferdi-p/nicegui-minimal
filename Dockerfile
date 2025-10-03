FROM python:3.11-bookworm

# create the user first so we can chown later
RUN useradd -m appuser

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# make the project readable/enterable by appuser (and anyone)
RUN chown -R appuser:appuser /app && chmod -R a+rX /app

USER appuser
ENV PORT=8080 PYTHONUNBUFFERED=1

EXPOSE 8080
CMD ["python", "main.py"]
