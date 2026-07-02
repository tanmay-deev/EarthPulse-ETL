import subprocess
import sys

print("=" * 60)
print("EarthPulse ETL Pipeline")
print("=" * 60)

print("\nStep 1: Extracting Earthquake Data...\n")

result = subprocess.run(
    [sys.executable, "scripts/extract_earthquake_data.py"]
)

if result.returncode != 0:
    print("Extraction failed.")
    sys.exit(1)

print("\nExtraction Completed Successfully.\n")

print("-" * 60)

print("\nStep 2: Uploading to Amazon S3...\n")

result = subprocess.run(
    [sys.executable, "scripts/upload_to_s3.py"]
)

if result.returncode != 0:
    print("Upload failed.")
    sys.exit(1)

print("\nUpload Completed Successfully.")

print("-" * 60)

print("\nETL Pipeline Finished Successfully.")
print("Amazon S3 has triggered AWS Lambda automatically.")
print("Check DynamoDB and CloudWatch Logs in AWS Console.")
print("=" * 60)