# AWS-Glue-ETL-Pipeline-Project

##We have created an ETL Pipeline using AWS. Our ETL Pipeline involves Files extracting from S3, Triggering of Lambda function to trigger Glue Workflow, Resulting in creating a event in EventBridge to finally trigger a Email Notification with SNS Topic.

### ETL Pipeline -
<p align = "Center">
<img width="1460" height="616" alt="Screenshot 2025-12-06 164534" src="https://github.com/user-attachments/assets/82d09bdc-fc42-4d05-8d95-d9b7362616cd" />
</p>

### Amazon S3 - We have created one bucket with two folders -
#### Bucket --> mg-etl-pipelin
#### Folders --> extract/ and data-lake-target/
#### Extract folder is the Data Staging Area where CSV file is placed that is source file and Data Lake Target folder is target location where data is loaded after successful transformation.

