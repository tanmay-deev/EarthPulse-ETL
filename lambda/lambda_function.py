import json
import os
import logging
from decimal import Decimal
from datetime import datetime, UTC

import boto3

# Logging Configuration

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# AWS Clients
s3_client = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")

TABLE_NAME = os.environ["DYNAMODB_TABLE"]
table = dynamodb.Table(TABLE_NAME)

# Helper Functions

def calculate_risk_level(magnitude):
    """
    Determine earthquake risk level.
    """
    if magnitude >= 5:
        return "High"
    elif magnitude >= 3:
        return "Medium"
    return "Low"


def convert_timestamp(timestamp_ms):
    """
    Convert Unix milliseconds into readable UTC format.
    """
    return datetime.fromtimestamp(
        timestamp_ms / 1000,
        UTC
    ).strftime("%Y-%m-%d %H:%M:%S UTC")

# Lambda Handler

def lambda_handler(event, context):

    inserted_records = 0
    rejected_records = 0

    try:

        bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
        object_key = event["Records"][0]["s3"]["object"]["key"]

        logger.info(f"Bucket : {bucket_name}")
        logger.info(f"Object : {object_key}")


        response = s3_client.get_object(
            Bucket=bucket_name,
            Key=object_key
        )

        raw_json = json.loads(
            response["Body"].read().decode("utf-8")
        )

        earthquakes = raw_json.get("features", [])

        logger.info(f"Total Records Found : {len(earthquakes)}")


        for earthquake in earthquakes:

            try:

                properties = earthquake.get("properties", {})
                geometry = earthquake.get("geometry", {})

                magnitude = properties.get("mag")
                place = properties.get("place")

                if magnitude is None:
                    rejected_records += 1
                    continue

                if place is None:
                    rejected_records += 1
                    continue

                coordinates = geometry.get(
                    "coordinates",
                    [0, 0, 0]
                )

                longitude = coordinates[0]
                latitude = coordinates[1]
                depth = coordinates[2]

                item = {

                    "record_id": earthquake["id"],

                    "place": place.strip().title(),

                    "magnitude": Decimal(str(magnitude)),

                    "event_time": convert_timestamp(
                        properties["time"]
                    ),

                    "status": properties.get(
                        "status",
                        "unknown"
                    ),

                    "tsunami": int(
                        properties.get(
                            "tsunami",
                            0
                        )
                    ),

                    "latitude": Decimal(str(latitude)),

                    "longitude": Decimal(str(longitude)),

                    "depth": Decimal(str(depth)),

                    "significance": int(
                        properties.get(
                            "sig",
                            0
                        )
                    ),

                    "risk_level": calculate_risk_level(
                        magnitude
                    )

                }

                table.put_item(Item=item)

                inserted_records += 1

            except Exception as record_error:

                rejected_records += 1

                logger.error(
                    f"Record skipped : {record_error}"
                )


        logger.info("=" * 50)
        logger.info("ETL SUMMARY")
        logger.info("=" * 50)
        logger.info(f"Total Records   : {len(earthquakes)}")
        logger.info(f"Inserted Records: {inserted_records}")
        logger.info(f"Rejected Records: {rejected_records}")
        logger.info("=" * 50)

        return {
            "statusCode": 200,
            "body": json.dumps(
                {
                    "message": "ETL Completed Successfully",
                    "total_records": len(earthquakes),
                    "inserted_records": inserted_records,
                    "rejected_records": rejected_records,
                }
            ),
        }

    except Exception as e:

        logger.exception("ETL Pipeline Failed")

        return {
            "statusCode": 500,
            "body": json.dumps(
                {
                    "error": str(e)
                }
            ),
        }