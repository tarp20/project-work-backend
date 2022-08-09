FROM python:3.10-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY src/ /code/

ENTRYPOINT ["python3", "src/manage.py", "runserver", "0.0.0.0:8000"]
