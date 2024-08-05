# How to Run the Server Locally

1. Install Necessary Packages

   Assuming Python is installed on your local machine, follow these steps:
   
   ```shell
   python3 -m venv venv  # Create a virtual environment
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   (venv) pip install -r requirements.txt
   ```
   

2. Set the Flask App Environment Variable
 
   ```shell
   (venv) export FLASK_APP=src
   (venv) export FLASK_ENV=local
   ```

3. Prepare MongoDB 
   1. Install and Start MongoDB:
      1. Ensure that MongoDB is installed on your system. Start the MongoDB service to enable the application to connect to it.
   2. Create Database and Collection:
      1. Create a database named `english_study` if it does not already exist. 
      2. Set up the default collection named `sentences` within the `english_study` database.
   3. Initialize the Database:
      1. Run the following command to initialize the `english_study` database and the `sentences` collection:
      ```shell
      (venv) flask init-db
      ```

4. Run the Application

   Start the Flask server with the following command:

   ```shell
   (venv) flask run
   ```

   The server should now be running.


# How to deploy it to AWS with MongoDB Atlas

The project decides to use AWS ElasticBeanstalk, AWS secret manager, AWS gateway, Circle CI and Mongo Atlas.

## Prepare Mongodb

This application uses MongoDB. Follow these steps to set it up:

   1. Register and set up a MongoDB instance on [Mongodb Login](https://account.mongodb.com/account/login). 
   2. Add current IP address (local) to the network access list, and later the ElasticBeanstalk's IP address need to be added as well.
   3. Obtain the connection string for MongoDB Compass to connect.
   4. Create a database named `english_study` if it does not already exist, and set up the default collection named `sentences`.
   5. Obtain the connection string for the Python project. The format should be:
   ```shell
   MONGO_URI=mongodb+srv://<your_username>:<your_password>@english.xxxxxx.mongodb.net/english_study?retryWrites=true&w=majority&appName=english_study
   ```
   5. Ensure the `<default_database_name>` is `english_study`.
   6. Fill in the `.env` file.
   7. Run the following command to initialize the english_study database and the sentences collection:
   ```shell
   (venv) flask init-db
   ```

## Configuration AWS

### Create AWS user

1. Need to create an AWS account and a root user first.
2. Create an IAM user `english-study-app-manager` from the root user perspective.
3. Grant all permissions listed:
   1. AdministratorAccess-AWSElasticBeanstalk
   2. AmazonAPIGatewayAdministrator 
   3. IAMFullAccess 
   4. AmazonS3FullAccess 
   5. CloudWatchFullAccess
   6. CloudWatchFullAccessV2
   7. SecretsManagerReadWrite
4. Generate Credentials for this user.

### AWS CLI

1. Install the AWS CLI.
2. Add the profile to the CLI:
   ```shell
   aws configure --profile english-study-app-manager
   ```
3. Decide to use AWS CLI to set up all necessary resources, later for executing AWS CLIs under this user, just need to specify `--profile english-study-app-manager` at end of each command.

## AWS Secret Manager

1. Store Mongodb credential in AWS Secret Manager
   ```shell
   aws secretsmanager create-secret --name EnglishStudyApp --secret-string '{"MONGO_URI":"your_MONGODB_uri"}' --profile english-study-app-manager
   ```
   
## AWS Elastic Beanstalk

1. Install Elastic Beanstalk
   ```shell
   brew install aws-elasticbeanstalk
   ```
2. 


## Prepare `.env`

Create a copy of the `.env.prod.example` file and name it `.env.prod`. Fill in the necessary fields in the `.env.prod` file.

# APIs

1. List al records:

   ```text
   [GET] http://127.0.0.1:5000/sentence/list
   ```

2. Insert a new record

   ```text
   [POST] http://127.0.0.1:5000/sentence/create
   ```
   
# Troubleshooting

## No module named 'markupsafe'

The error "No module named 'markupsafe'" persisting despite the package being installed could be due to a number of issues, including environment misconfiguration or conflicts. Here are some steps to troubleshoot and resolve this issue:

1. Verify Virtual Environment Activation

   ```shell
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. Check Installed Packages

   ```shell
   (venv) pip list
   ```
   Ensure MarkupSafe appears in the list of installed packages.

3. Check Python Version

   ```shell
   (venv) which python  # On Unix-like systems
   (venv) where python  # On Windows
   ```
   
4. Reinstall MarkupSafe

   ```shell
   (venv) pip uninstall markupsafe
   (venv) pip install markupsafe
   ```
   
5. Check for Virtual Environment Conflicts

   ```shell
   (venv) deactivate
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   
6. Review and Clean requirements.txt

   ```shell
   (venv) rm requirements.txt
   (venv) pip freeze > requirements.txt
   (venv) pip install -r requirements.txt
   ```
   
7. Run Flask again

## Failed to start MongoDB on macOS

Try to use the following command:
   ```shell
   sudo brew services start mongodb-community@7.0
   ```
