FROM python:3.11

COPY . .

RUN python3 -m pip install -r requirements.txt

# uvicorn exchange.main:main --reload --host 0.0.0.0 --port 8000
CMD ["uvicorn", "main:main", "--reload", "--host", "0.0.0.0", "--port", "8000"]