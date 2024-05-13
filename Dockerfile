FROM python:3.10.12

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --upgrade pip

COPY . /app/

RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 9000

CMD ["python", "manage.py", "runserver", "0.0.0.0:9000", "--insecure"]
