import json
import time
import boto3
import botocore
from loguru import logger
from utils import search_download_youtube_video
from botocore.exceptions import ClientError
import subprocess
import os


def process_msg(msg):
    search_download_youtube_video(msg)

    # TODO upload the downloaded video to your S3 bucket

    # Creating Session With Boto3.
    session = boto3.Session(
        aws_access_key_id='AKIAVEHYNQDCSCKZADHQ',
        aws_secret_access_key='UeEdShSfYYzf5W/zvM9RbAZdt5QyJWrt5VT/1Ey1'
    )

    # Creating S3 Resource From the Session.
    s3 = session.resource('s3')
    test = msg
    # result = s3.Bucket('danishain-polybot-aws-ex1').upload_file(f'C:/Users/דניאל/PycharmProjects/PolyBot/{msg}','/youtube')
    result = s3.Bucket('danishain-polybot-aws-ex1').upload_file( f"C:/Users/דניאל/PycharmProjects/PolyBot/{msg}",'/youtube')

def main():
    while True:
        try:
            messages = queue.receive_messages(
                MessageAttributeNames=['All'],
                MaxNumberOfMessages=1,
                WaitTimeSeconds=10
            )
            for msg in messages:
                logger.info(f'processing message {msg}')
                process_msg(msg.body)

                # delete message from the queue after is was handled
                response = queue.delete_messages(Entries=[{
                    'Id': msg.message_id,
                    'ReceiptHandle': msg.receipt_handle
                }])
                if 'Successful' in response:
                    logger.info(f'msg {msg} has been handled successfully')

        except botocore.exceptions.ClientError as err:
            logger.exception(f"Couldn't receive messages {err}")
            time.sleep(10)


if __name__ == '__main__':
    with open('config.json') as f:
        config = json.load(f)

    sqs = boto3.resource('sqs', region_name=config.get('aws_region'))
    queue = sqs.get_queue_by_name(QueueName=config.get('bot_to_worker_queue_name'))

    main()
