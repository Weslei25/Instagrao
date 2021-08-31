# coding=utf-8

import boto3
try:

    dynamodb = boto3.resource("dynamodb")

    def extractMetadata(event, context):
        print("Hello World")

    def getMetadata(event, context):
        print("Hello World")
except Exception as error:
    print(error)