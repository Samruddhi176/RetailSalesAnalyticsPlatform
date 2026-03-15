import json
import base64
import boto3
from datetime import datetime

s3 = boto3.client("s3")
BUCKET = "retail-data-lake"

def lambda_handler(event, context):

    records = []

    for record in event['Records']:

        payload = base64.b64decode(record['kinesis']['data'])
        data = json.loads(payload)

        data["ingestion_time"] = datetime.utcnow().isoformat()

        records.append(data)

    s3.put_object(
        Bucket=BUCKET,
        Key=f"raw/transactions_{datetime.utcnow().timestamp()}.json",
        Body=json.dumps(records)
    )

    return {
        "statusCode": 200,
        "body": "Processed successfully"
    }
