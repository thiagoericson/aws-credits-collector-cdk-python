import json

def handler(event, context):
    """
    Handler para a função Lambda do Web App.
    Responde às requisições HTTP enviadas pelo API Gateway.
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
