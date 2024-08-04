# How to Run the Server Locally

1. Install Necessary Packages

   Assuming Python is installed on your local machine, follow these steps:
   
   ```shell
   python3 -m venv venv  # Create a virtual environment
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   (venv) pip install -r requirements.txt
   ```
   
2. Prepare `.env`
   
   Create a copy of the `.env.example` file and name it `.env`. Fill in the necessary fields in the `.env` file.


4. (Optional) Set the Flask App Environment Variable

   The `FLASK_APP` environment variable is already specified in the `.env` file. If you need to set it manually, use the following command:
   
   ```shell
   (venv) export FLASK_APP=src
   ```

5. Prepare MongoDB

   This application uses MongoDB. Follow these steps to set it up:

   1. Register and set up a MongoDB instance on [Mongodb Login](https://account.mongodb.com/account/login). 
   2. Obtain the connection string for MongoDB Compass to connect.
   3. Create a database named `english_study` if it does not already exist, and set up the default collection named `sentences`.
   4. Obtain the connection string for the Python project. The format should be:
   ```shell
   MONGO_URI=mongodb+srv://<your_username>:<your_password>@english.xxxxxx.mongodb.net/english_study?retryWrites=true&w=majority&appName=english_study
   ```
   5. Ensure the `<default_database_name>` is `english_study`.
   6. Fill in the `.env` file.
   7. Run the following command to initialize the english_study database and the sentences collection:
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

