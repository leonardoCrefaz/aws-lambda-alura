import json
from log import log
import boto3

s3 = boto3.resource("s3")

def lambda_handler(event, context):

    Bucket = event["Records"][0]["s3"]["bucket"]["name"]
    Key = event["Records"][0]["s3"]["object"]["key"]

    log(f"Bucket: {Bucket}")
    log(f"Key: {Key}")

    getObjectResult = s3.Object(bucket_name=Bucket, key=Key)

    mega_byte = 1024 * 1024

    if (getObjectResult.content_length > 1 * mega_byte):
        log("Objeto muito grande")
        return "Objeto muito grande"

    print("Objeto de tamanho OK")
    return "Objeto de tamanho OK"