import json
import os
import uuid
from datetime import datetime, timezone

import boto3

TABLE_NAME = os.environ.get("TABLE_NAME", "serverless-items")
table = boto3.resource("dynamodb").Table(TABLE_NAME)


def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body),
    }


def lambda_handler(event, context):
    method = event.get("requestContext", {}).get("http", {}).get("method", "GET")
    path = event.get("rawPath", "/")

    if method == "GET" and path == "/health":
        return response(200, {"status": "healthy"})

    if method == "POST" and path == "/items":
        body = json.loads(event.get("body") or "{}")
        item_id = str(uuid.uuid4())
        item = {
            "id": item_id,
            "name": body.get("name", "unnamed"),
            "created_at": datetime.now(timezone.utc).isoformat(),
        }
        table.put_item(Item=item)
        return response(201, item)

    if method == "GET" and path.startswith("/items/"):
        item_id = path.split("/")[-1]
        result = table.get_item(Key={"id": item_id})
        item = result.get("Item")
        if not item:
            return response(404, {"error": "item not found"})
        return response(200, item)

    return response(404, {"error": "route not found"})
