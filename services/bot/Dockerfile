FROM python:3.9-slim-bullseye
WORKDIR /app
ENV APP_PATH=services/bot
COPY . .
RUN pip3 freeze > services/bot/requirements.txt
RUN pip3 install -r $APP_PATH/requirements.txt


CMD ["python3", "services/bot/app.py"]