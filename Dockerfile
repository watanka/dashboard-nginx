FROM python:3.11
COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN chmod +x run.sh

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]