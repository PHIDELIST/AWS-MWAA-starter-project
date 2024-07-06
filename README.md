# AWS Managed Workflows for Apache Airflow(MWAA)

This starter project for AWS Managed Workflows for Apache Airflow (MWAA) is designed to streamline the setup and deployment process. 
It includes a CloudFormation template to automatically provision necessary AWS resources and deploy MWAA. Additionally, it leverages GitHub Actions for continuous integration and deployment (CI/CD). 
The GitHub Actions automate the process of deploying Directed Acyclic Graphs (DAGs) to Amazon S3 and deploying the AWS CloudFormation stack. 
The app also offers functionality to test MWAA workflows locally, ensuring a smooth transition before deploying to a production environment.

## Architecture

## Testing dags locally 
+ Add DAG code to the ```dags/``` folder.
+ Add Python dependencies to ```requirements/requirements.txt```
+ Build docker image
  ```./mwaa-local-env build-image```
+ Run Apache Airflow
  ```./mwaa-local-env start```
+ Accessing Airflow UI:
  
  Enter this url ```http://localhost:8080/``` in browser
  use ```admin``` as *username* and ```test``` as *password*
  ![image](https://github.com/PHIDELIST/AWS-MWAA-starter-project/assets/64526896/2d32a8d8-973b-4860-a111-f05f5a9d4bbd)

  


