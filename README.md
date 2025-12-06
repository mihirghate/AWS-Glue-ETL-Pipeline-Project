# AWS-Glue-ETL-Pipeline-Project

## We have created an ETL Pipeline using AWS. Our ETL Pipeline involves Files extracting from S3, Triggering of Lambda function to trigger Glue Workflow, Resulting in creating a event in EventBridge to finally trigger a Email Notification with SNS Topic.

### ETL Pipeline -
<p align = "Center">
<img width="1460" height="616" alt="Screenshot 2025-12-06 164534" src="https://github.com/user-attachments/assets/82d09bdc-fc42-4d05-8d95-d9b7362616cd" />
</p>

### Amazon S3 - We have created one bucket with two folders -
#### Bucket --> mg-etl-pipeline
#### Folders --> extract/ and data-lake-target/
#### Extract folder is the Data Staging Area where CSV file is placed that is source file and Data Lake Target folder is target location where data is loaded after successful transformation.

### Lambda Function -
#### Lambda function is coded in Python. Lambda function gets triggered by S3 service. Once file is placed in source, Lambda gets triggered. Basic IAM role for Lambda execution is created during function creation. We need to add S3 access to Lambda function using role.

### Glue Workflow -
#### Lambda function triggers Glue workflow which consists of below stages -
#### Extract - Data Source is Amazon S3 Extract folder
#### Transform - Using Drop Duplicate Transformation, Duplicate records are removed
### Load - Target data is ready in S3 Data Lake after transformation

Lambda must have permission over Glue as well so the IAM role must be verified

### EventBridge
#### We have created rule to track the event of completion of workflow in Glue that is on Job Status change. Once Job succeeds or fails, Event is triggered

### SNS Email Notification
