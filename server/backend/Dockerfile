FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /backend

COPY ./requirements.txt /backend/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /backend

CMD [ "uvicorn", "api.server:app", "--reload", "--workers", "1", "--host", "0.0.0.0", "--port", "80" ]
