FROM python:3.7-alpine 
LABEL maintainer="quantacake"

ENV PYTHONUNBUFFERED 1 

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt 

# mkdir app 
RUN mkdir /app 
# change to root app dir
WORKDIR /app 
# copy local app into the root dir app of the container
COPY ./app /app 

# create user that will be used for running applications only (-D)
RUN adduser -D user 
# switch from root user to this user 
USER user 