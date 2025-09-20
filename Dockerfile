

FROM python:3.13-slim-bookworm

WORKDIR /app

ENV PYTHONDONTWRITEBYTECOD=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]



