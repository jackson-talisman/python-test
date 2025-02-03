import json


def hello(event, context):
    body = {
        "message": "Go Serverless v4.0! Your function executed successfully!"
    }

    ## Attempting to trigger CFN deployment

    return {"statusCode": 200, "body": json.dumps(body)}