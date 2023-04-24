"""Python Lambda SNS notifier"""

import base64
import os

import boto3

SNS_TOPIC_ARN = os.environ["SNS_TOPIC_ARN"]

sns = boto3.client("sns")

print("Loading function")

def lambda_handler(event, context):
    output = []
    success = 0
    failure = 0
    highest_score = 0

    print(f"event: {event}")
    r = event["records"]
    print(f"records: {r}")
    print(f"type_records: {type(r)}")

    for record in event["records"]:
        try:
            # Uncomment the below line to publish the decoded data to the SNS topic.
            payload = base64.b64decode(record["data"])
            print(f"payload: {payload}")
            text = payload.decode("utf-8")
            print(f"text: {text}")
            score = float(text)
            if (score != 0) and (score > highest_score):
                highest_score = score
                print(f"New highest_score: {highest_score}")
                # sns.publish(
                #     TopicArn=SNS_TOPIC_ARN, 
                #     Message='New anomaly score: {}'.format(text), 
                #     Subject='New Reviews Anomaly Score Detected'
                # )
                output.append({"recordId": record["recordId"], "result": "Ok"})
                success += 1
        except Exception as e:
            print(e)
            output.append({"recordId": record["recordId"], "result": "DeliveryFailed"})
            failure += 1
    if highest_score != 0:
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=f"New anomaly score: {str(highest_score)}",
            Subject="New Reviews Anomaly Score Detected",
        )
    print(
        f"Successfully delivered {success} records, failed to deliver {failure} records"
    )
    return {"records": output}