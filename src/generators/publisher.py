""" Publishes generated events to AWS SNS"""

import json
import os
import random
from typing import Any

import boto3

from .demand_signal_generator import generate_demand_signal
from .inventory_movement_generator import generate_inventory_movement
from .production_order_generator import generate_production_order
from .supplier_delivery_generator import generate_supplier_delivery


def get_sns_client():
    AWS_ENDPOINT_URL = os.getenv("AWS_ENDPOINT_URL", "http://localhost:4566")
    AWS_REGION_NAME = os.getenv("AWS_REGION_NAME", "us-east-1")

    return boto3.client("sns", region_name=AWS_REGION_NAME, endpoint_url=AWS_ENDPOINT_URL)

def publish_event(
    event: dict[str, Any],
    topic_arn: str,
    sns_client: Any | None = None
) -> str:

    if sns_client is None:
        sns_client = get_sns_client()

    event_type = event.get("event_type", "unknown")
    plant_code = event.get("plant_code", "unknown")
    source_system = event.get("source_system", "unknown")

    message_attributes = {
        "event_type": {
            "DataType": "String",
            "StringValue": event_type},
        "plant_code": {
            "DataType": "String",
            "StringValue": plant_code},
        "source_system": {
            "DataType": "String",
            "StringValue": source_system}
    }

    response = sns_client.publish(
        TopicArn = topic_arn,
        Message = json.dumps(event),
        Subject = f"Event: {event_type}",
        MessageAttributes = message_attributes
    )

    return response.get("MessageId", "")

def generate_and_publish(
    n_events: int,
    topic_arn: str,
    sns_client: Any | None = None,
    event_mix: dict[str, float] | None = None
) -> list[str]:

    if sns_client is None:
        sns_client = get_sns_client()

    if event_mix is None:
        event_mix = {
            "production_order": 0.25,
            "inventory_movement": 0.40,
            "supplier_delivery": 0.20,
            "demand_signal": 0.15,
        }
    types = list(event_mix.keys())
    weights = list(event_mix.values())

    message_ids = []
    for n in range(n_events):
        evt = random.choices(types, weights=weights)[0]
        if evt == "production_order":
            event = generate_production_order()
        elif evt == "inventory_movement":
            event = generate_inventory_movement()
        elif evt == "supplier_delivery":
            event = generate_supplier_delivery()
        else:
            event = generate_demand_signal()

        mid = publish_event(event=event,topic_arn=topic_arn,sns_client=sns_client)
        message_ids.append(mid)

    return message_ids

if __name__ == "__main__":
    TOPIC_ARN = os.environ.get("SNS_TOPIC_ARN","arn:aws:sns:us-east-1:000000000000:mrp-dev-events")
    print(f"Publishing test events to: {TOPIC_ARN}")
    messages = generate_and_publish(5,TOPIC_ARN)
    print(messages)

    
