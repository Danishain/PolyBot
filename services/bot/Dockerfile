FROM python:3.9-slim-bullseye
WORKDIR /app
ENV APP_PATH=services/bot
COPY . .
RUN python3 -m venv tutorial-env-m pip install --upgrade pip
RUN pip install -r $APP_PATH/requirements.txt

CMD ["python3", "services/bot/app.py"]