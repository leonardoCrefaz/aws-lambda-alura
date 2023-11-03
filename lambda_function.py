import json
from log import log

def lambda_handler(event, context):

    log(f"Event: {json.dumps(event)}")

    return {
        "statusCode": 200,
        "body": f"<html><body>Dados da requisicao {json.dumps(event)}</body></html>",
        "headers": {
            "content-type": "text/html",
        }
    }