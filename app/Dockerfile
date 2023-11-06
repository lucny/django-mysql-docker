# pull official base image
FROM python:3.11-bullseye

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# Install mysqlclient debian package dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
   libmariadb-dev-compat gcc                   `: MySQL client` \
&& rm -rf /var/lib/apt/lists/*

# Install mysqlclient python package
RUN pip install --no-cache-dir mysqlclient

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]