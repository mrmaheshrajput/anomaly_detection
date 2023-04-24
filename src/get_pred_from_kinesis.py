"""Python Lambda Handler function."""
import base64
import json
import random

from transformers import pipeline

sent_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def lambda_handler(event, context) -> json:
    """Lambda handler function."""
    outputs = []

    for record in event["records"]:
        payload = base64.b64decode(record["data"])
        text = payload.decode("utf-8")

        split_inputs = text.split("\t")
        review_body = split_inputs[2]
        
        predictions = sent_pipeline(review_body)
        inputs = [{"features": [review_body]}]

        for pred, input_data in zip(predictions, inputs):
            review_id = random.randint(0, 1000)

            # review_id, star_rating, review_body
            output_data = "{}\t{}\t{}".format(
                split_inputs[0], 0 if pred["label] == "NEGATIVE" else 1, input_data["features"]
            )
            output_data_encoded = output_data.encode("utf-8")
            output_record = {
                "recordId": record["recordId"],
                "result": "Ok",
                "data": base64.b64encode(output_data_encoded).decode("utf-8"),
            }
            outputs.append(output_record)

    return {"records": outputs}