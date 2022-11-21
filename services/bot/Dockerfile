FROM python:3.9-slim-bullseye
WORKDIR /app
ENV APP_PATH=services/bot
COPY . .
COPY $APP_PATH/requirements.txt /tmp/requirements.txt
RUN python3 -m pip install -r /tmp/requirements.txt


CMD ["python3", "services/bot/app.py"]