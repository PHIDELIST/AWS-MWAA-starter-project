# AWS Managed Workflows for Apache Airflow(MWAA)

This starter project for AWS Managed Workflows for Apache Airflow (MWAA) is designed to streamline the setup and deployment process. 
It includes a CloudFormation template to automatically provision necessary AWS resources and deploy MWAA. Additionally, it leverages GitHub Actions for continuous integration and deployment (CI/CD). 
The GitHub Actions automate the process of deploying Directed Acyclic Graphs (DAGs) to Amazon S3 and deploying the AWS CloudFormation stack. 
The app also offers functionality to test MWAA workflows locally, ensuring a smooth transition before deploying to a production environment.



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
  
## Deploying MWAA to AWS 
+ Fork or clone the project and deploy it to your Github account
+ Add aws region, secrete key and aws access key in the github repo secretes
+ Got to the Actions tab then run ```Deploy AWS MWAA job```
  ![image](https://github.com/user-attachments/assets/9a430b76-f163-4261-b66a-6c6a14fdfae7)
+ This will deploy all necessary resources required to create AWS MWAA plus AWS MWAA its self

## Working with dags
+ Dags are placed the ```/dags``` folder
+ For AWS MWAA dags are sorted in aws s3 bucket
+ Add or update your dags in ```/dags``` folder the push your code to github
+ Proceed to Actions then run ```Deploy DAGS to S3 job```
  ![image](https://github.com/user-attachments/assets/55b712ab-e201-4b44-8502-b309d5668706)

## Accessing AWS MWAA UI
+ Wait for AWS MWAA environment to finish creating then open the AIflow UI link:
  ![image](https://github.com/user-attachments/assets/5e320050-d1f5-46d9-ab78-bd2a65c69139)
+ Then link will open airflow UI console with your dags loaded
  ![image](https://github.com/user-attachments/assets/00e70662-e75c-48fe-9115-4ed899def83b)

+ To clean the resources from your AWS account, go to AWS cloudformation stacks and delete mwaa-environment-public-network stack
  ![image](https://github.com/user-attachments/assets/46c090a0-b06e-446e-b47e-2559242d1ac7)


