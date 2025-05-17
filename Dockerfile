FROM python:3.13-alpine
COPY app/ app/
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD python -m app