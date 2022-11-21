FROM python:3.9-slim-bullseye
WORKDIR /app
ENV APP_PATH=services/bot
COPY . .
COPY $APP_PATH/requirements.txt /tmp/requirements.txt
RUN pip install -r $APP_PATH/requirements.txt
CMD ["python3", "services/bot/app.py"]