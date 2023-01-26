FROM python:3.10-slim

# set the working directory
WORKDIR /code

# Set initial env's
ENV FLASK_APP=api
ENV FLASK_RUN_HOST=0.0.0.0
ENV APP_SETTINGS=config.ProductionConfig
ENV FLASK_DEBUG=0

# install dependencies
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 5000
COPY . .

# start the server
CMD ["python", "manage.py", "run"]
