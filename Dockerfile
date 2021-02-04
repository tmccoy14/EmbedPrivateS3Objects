FROM python:3.7.4-slim-buster

# set working directory to app
WORKDIR /app

# copy all project contents to directory app
COPY . /app

# expose application port
EXPOSE 5000

# pip install/upgrade pip
RUN pip install --upgrade pip

# pip install/upgrade pip
RUN pip install -r requirements.txt

# set entry point as python command
ENTRYPOINT [ "python" ]

# start up flask app
CMD [ "app.py" ]
