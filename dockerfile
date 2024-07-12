FROM python:3.7
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# RUN python -m venv venv
# RUN source venv/bin/activate

CMD ["python", "app.py"]
