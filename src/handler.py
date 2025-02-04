import json
def handler(event, context):
    # Log the event argument for debugging and for use in local development.
    print(json.dumps(event))

    # Return a response to the event caller.
    response = {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }