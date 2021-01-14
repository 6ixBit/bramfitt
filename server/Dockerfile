FROM python:3.8-alpine 

WORKDIR /app
COPY . .

RUN source venv/bin/activate
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]