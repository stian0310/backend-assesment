FROM python:3.10.7-bullseye

# Setting up Locales and Timezone
ENV LANG=es_CO.UTF-8 \
    LANGUAGE=es_CO.UTF-8 \
    LC_ALL=C \
    TZ=America/Bogota \
    DEBIAN_FRONTEND=noninteractive

RUN apt update \
    && apt install -y locales \
    && locale-gen es_CO.UTF-8 \
    && locale-gen en_US.utf8 \
    && update-locale

# Django
ARG DJANGO_ENV

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /code
WORKDIR /code

COPY requirements/base.txt /code/
COPY requirements/$DJANGO_ENV.txt /code/

RUN pip install --upgrade pip
RUN python -m pip install -r $DJANGO_ENV.txt

COPY . /code