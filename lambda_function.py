import json
from log import log

def lambda_handler(event, context):

    log(f"Event: {json.dumps(event)}")
    log(f"Context: {context.invoked_function_arn}")

    return {
        "statusCode": 200,
        "body": f"<html><body>Dados da requisicao {json.dumps(event)}</body></html>",
        "headers": {
            "content-type": "text/html",
        }
    }