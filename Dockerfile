FROM python:3.8.12-slim-buster
# YOUR COMMANDS HERE
# ....
# ....
RUN pip install --upgrade pip
RUN pip install awscli
COPY . .
RUN pip install -r requirements.txt
CMD ["python3", "worker.py"]