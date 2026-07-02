import logging
from pathlib import Path
from datetime import datetime

import boto3
from botocore.exceptions import ClientError, NoCredentialsError

# -------------------------------------------------------
# Configuration
# -------------------------------------------------------

BUCKET_NAME = "earthpulse-etl-921570400808"

LOCAL_FILE = Path("sample_data") / "earthquake_raw_data.json"

# Timestamped filename
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

S3_OBJECT_KEY = f"raw/earthquake_{timestamp}.json"

# -------------------------------------------------------
# Logging
# -------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# -------------------------------------------------------
# AWS Client
# -------------------------------------------------------

s3_client = boto3.client("s3")


def upload_file():

    if not LOCAL_FILE.exists():
        logger.error(f"File not found: {LOCAL_FILE}")
        return False

    try:

        logger.info("Uploading file to Amazon S3...")

        s3_client.upload_file(
            str(LOCAL_FILE),
            BUCKET_NAME,
            S3_OBJECT_KEY
        )

        logger.info("=" * 50)
        logger.info("Upload Successful")
        logger.info(f"Bucket : {BUCKET_NAME}")
        logger.info(f"Object : {S3_OBJECT_KEY}")
        logger.info("=" * 50)

        logger.info("Lambda Triggered Automatically")

        return True

    except NoCredentialsError:

        logger.error("AWS credentials not configured.")
        return False

    except ClientError as e:

        logger.error(f"AWS Error : {e}")
        return False

    except Exception as e:

        logger.exception(e)
        return False


if __name__ == "__main__":
    upload_file()