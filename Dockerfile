FROM python:3.8.12-slim-buster
# YOUR COMMANDS HERE
# ....
# ....
COPY . .
RUN pip install -r requirements.txt
CMD ["python3", "bot.py" , "worker.py"]