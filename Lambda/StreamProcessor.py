import json
import base64

def lambda_handler(event, context):

    processed_records = []

    for record in event['Records']:
        payload = base64.b64decode(record['kinesis']['data'])
        data = json.loads(payload)

        if data["price"] > 0:
            processed_records.append(data)

    print("Processed records:", processed_records)

    return {
        "statusCode": 200,
        "body": json.dumps("Processing complete")
    }
