###########
# BUILDER #
###########

# pull official base image
FROM python:3.10-alpine AS builder

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/app

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev diffutils

# pip
RUN --mount=type=cache,target=/root/.cache pip install --upgrade pip

# install dependencies
COPY ./requirements.txt .
#RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt
RUN --mount=type=cache,target=/root/.cache pip wheel --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

#########
# FINAL #
#########

# pull official base image
FROM python:3.10-alpine

RUN apk update && apk add libpq libstdc++ diffutils

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup -S app && adduser -S app -G app

# change to the app user
USER app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/backend
RUN mkdir -p $APP_HOME/static
WORKDIR $APP_HOME

# copy project
COPY --chown=app:app . $APP_HOME
#RUN find . -name "*.sh" | xargs chmod +x

# install dependencies
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
ENV PATH="${PATH}:/home/app/.local/bin/"
#RUN pip install --no-cache /wheels/*
RUN --mount=type=cache,target=/root/.cache pip install --upgrade pip
RUN --mount=type=cache,target=/root/.cache pip install /wheels/*
RUN --mount=type=cache,target=/root/.cache pip install gunicorn
