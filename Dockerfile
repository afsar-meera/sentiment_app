FROM python:3.9

WORKDIR /app

COPY requirment.txt .
RUN pip install --no-cache-dir -r requirment.txt

COPY . .

EXPOSE 5007

CMD ["python", "main.py"]