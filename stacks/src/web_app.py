import json

def handler(event, context):
    """
    Handler for the Web App Lambda function.
    Responds to HTTP requests sent by API Gateway.    
    """
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message": "Hello World from AWS Lambda Web App!",
            "status": "success"
        })
    }
