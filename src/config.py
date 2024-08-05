import os
import json
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from dotenv import load_dotenv


class Config:
    def __init__(self):
        if os.environ.get('FLASK_ENV') == 'local':
            # local
            env_file = '.env.local'
            load_dotenv(env_file)
            self.mongo_uri = os.environ.get('MONGO_URI')
        else:
            # prod
            env_file = '.env.prod'
            load_dotenv(env_file)
            self.region_name = os.environ.get('AWS_REGION')
            self.aws_secret_name = os.environ.get('AWS_SECRET_NAME')
            self.mongo_uri = self.get_secret().get('MONGO_URI')

    def get_secret(self):
        session = boto3.Session(profile_name='english-study-app-manager')
        client = session.client(
            'secretsmanager',
            region_name=self.region_name
        )

        try:
            get_secret_value_response = client.get_secret_value(SecretId=self.aws_secret_name)
            secret = get_secret_value_response['SecretString']
            return json.loads(secret)
        except (NoCredentialsError, PartialCredentialsError, Exception) as e:
            print(f"Error retrieving secret: {e}")
            return None

config = Config()

