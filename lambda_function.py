import json
from log import log

def lambda_handler(event, context):

    log(f"Log de execução após github actions. Event: {json.dumps(event)}")

    return {
        'statusCode': 200,
        'body': json.dumps(event),
    }