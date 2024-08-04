# How to Run the Server Locally

1. Install Necessary Packages

Assuming Python is installed on your local machine, follow these steps:

```shell
source venv/bin/activate
(venv) pip install -r requirements.txt
```

2. (Optional) Set the Flask App Environment Variable

The `FLASK_APP` environment variable is already specified in the `.env` file. If you need to set it manually, use the following command:

```shell
(venv) export FLASK_APP=src
```

3. Prepare MongoDB
This application uses MongoDB. Follow these steps to set it up:
   1. Register and set up a MongoDB instance on [Mongodb Login](https://account.mongodb.com/account/login). 
   2. Obtain the connection string for MongoDB Compass to connect.
   3. Create a database named `english_study` if it does not already exist, and set up the default collection named `sentences`.
   4. Obtain the connection string for the Python project. The format should be:
   ```shell
   MONGO_URI=mongodb+srv://<your_username>:<your_password>@english.xxxxxx.mongodb.net/english_study?retryWrites=true&w=majority&appName=English
   ```
   5. Ensure the `<default_database_name>` is `english_study`.
   6. Run the following command to initialize the english_study database and the sentences collection:
   ```shell
   (venv) flask init-db
   ```
   

4. Run the Application
Start the Flask server with the following command:

```shell
(venv) flask run
```
The server should now be running.


# APIs
1. List al records:
```text
[GET] http://127.0.0.1:5000/sentence/list
```

2. Insert a new record
```text
[POST] http://127.0.0.1:5000/sentence/create
```


