import boto3
import os

def lambda_handler(event, context):
    # Initialize Glue client
    glue_client = boto3.client('glue')

    glue_job_name = "S3-Glue-S3-ETL"

    try:
        response = glue_client.start_job_run(JobName=glue_job_name)

        print(f"Triggered Glue job: {glue_job_name}")
        print(f"Job Run ID: {response['JobRunId']}")

        return {
            "statusCode": 200,
            "body": f"Glue job {glue_job_name} started successfully with JobRunId {response['JobRunId']}"
        }

    except Exception as e:
        print(f"Error triggering Glue job: {str(e)}")
        return {
            "statusCode": 500,
            "body": f"Failed to start Glue job {glue_job_name}: {str(e)}"
        }