FROM python:3.9-slim-bullseye
WORKDIR /app
ENV APP_PATH=services/bot
COPY . .
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r $APP_PATH/requirements.txt

CMD ["python3", "services/bot/app.py"]