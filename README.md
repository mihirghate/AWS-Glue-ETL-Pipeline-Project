# AWS-Glue-ETL-Pipeline-Project

## We have created an ETL Pipeline using AWS. Our ETL Pipeline involves Files extracting from S3, Triggering of Lambda function to trigger Glue Workflow, Resulting in creating a event in EventBridge to finally trigger a Email Notification with SNS Topic.

### ETL Pipeline -
<p align = "Center">
<img width="1460" height="616" alt="Screenshot 2025-12-06 164534" src="https://github.com/user-attachments/assets/82d09bdc-fc42-4d05-8d95-d9b7362616cd" />
</p>

### Amazon S3 - We have created one bucket with two folders -
#### Bucket --> mg-etl-pipeline
#### Folders --> extract/ & data-lake-target/
#### Extract folder is the Data Staging Area where CSV file is placed that is source file and Data Lake Target folder is target location where data is loaded after successful transformation.
<p align = "Center">
<img width="1723" height="627" alt="image" src="https://github.com/user-attachments/assets/bb0a727c-8ed9-4e43-816e-ebbeea1a8c95" />
</p>

### Lambda Function -
#### Lambda function is coded in Python. Lambda function gets triggered by S3 service. Once file is placed in source, Lambda gets triggered. Basic IAM role for Lambda execution is created during function creation. We need to add S3 access to Lambda function using role.
<p align = "Center">
<img width="1764" height="684" alt="image" src="https://github.com/user-attachments/assets/3aed959b-0d21-4907-bf3d-b8e8979e5916" />
<img width="1724" height="746" alt="image" src="https://github.com/user-attachments/assets/3cbbe3e9-4cf9-40d8-b5d9-84eda2bf68bc" />
</p>

### Glue Workflow -
Lambda function triggers Glue workflow which consists of below stages -
#### Extract - Data Source is Amazon S3 Extract folder
#### Transform - Using Drop Duplicate Transformation, Duplicate records are removed
### Load - Target data is ready in S3 Data Lake after transformation
Again, Lambda must have permission over Glue as well so the IAM role must be verified
<p align = "Center">
<img width="1320" height="567" alt="image" src="https://github.com/user-attachments/assets/e57403fc-cef0-4b10-9add-93a9c9ac57fe" />
<img width="1716" height="591" alt="image" src="https://github.com/user-attachments/assets/8b947b5d-4dbd-4320-977d-2422b1c2613a" />
</p>

For this Project, we have given full S3 Access and Glue access along with Lambda role. Only read access is enough for this project.
<p align = "Center">
<img width="1361" height="772" alt="image" src="https://github.com/user-attachments/assets/44b9ef22-3686-4bec-b7ff-7513346ed920" />
</p>

### EventBridge
#### We have created rule to track the event of completion of workflow in Glue that is on Job Status change. Once Job succeeds or fails, Event is triggered. This will trigger SNS Topic.
<p align = "Center">
<img width="1711" height="742" alt="image" src="https://github.com/user-attachments/assets/1c2df518-ec3c-47b6-8eda-d2704003d494" />
<img width="1722" height="785" alt="image" src="https://github.com/user-attachments/assets/f6a34072-eb01-4f80-a7d9-6aa6a3d64ebf" />
</p>

IAM Role needs to be created while creating rule in order to allow Glue to trigger event and send target invoke to email -
<p align = "Center">
<img width="1365" height="718" alt="image" src="https://github.com/user-attachments/assets/2eaa6496-0cd6-4edd-816a-e9432a5f577e" />
</p>

### SNS Email Notification
#### We have created a Standard SNS Topic and We have created an email subscription to get the notification for our Glue workflow status.
<p align = "Center">
<img width="2457" height="1223" alt="image" src="https://github.com/user-attachments/assets/66c35c6f-9fdb-4a15-9ed4-0667edcc9d57" />
<img width="1339" height="461" alt="image" src="https://github.com/user-attachments/assets/1e5f8692-b102-41d5-9b6a-156bf6c18f84" />
</p>

Data Lake Target file is generated once workflow is succeeded -
<p align = "Center">
<img width="1715" height="605" alt="image" src="https://github.com/user-attachments/assets/56c36f10-361c-4a9c-be4d-65b6fd0b9856" />
</p>
