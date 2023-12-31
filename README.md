# API upload an image

- **API upload an image** project written in Django REST Framework 


## Technologies Used
* Python 3.11
* Django 4.2.5
* Redis 
* Celery
* Django REST 
* Google Cloud Storage 
* PostgreSQL 
* Docker-compose
* Django-Alluth


## Available Urls

### Users
- admin/
- api/v1/accounts/
- api/v1/accounts/register/

### Images

- api/v1/images/

### Documentations 

- ^api/swagger/
- ^api/redoc/

## How To Set Up Locally
> First of all, you need to:
> - Create a **bucket in GCS <a href="https://console.cloud.google.com/storage/create-bucket">link </a>**, with the name of your desire. 
> - Create **IAM Policy <a href="https://console.cloud.google.com/iam-admin/serviceaccounts"> link </a>**, GENERATE A KEY and download *.json file with the credentials. 
> - PUT YOUR CREDENTIALS TO THE SOURCE OF THIS PROJECT AND CHANGE THE NAME TO "private_credentials.json" (look at settings.py)


The easiest approach is to run docker-compose.
The docker-compose approach is based on google cloud storage. 

## How to run

- Copy this repo from GitHub:
```git
git clone https://github.com/ochernyi/api-upload-an-image.git
```
- Create venv and activate it through terminal:
```git
python -m venv venv

#Windows activaition:
myvenv\Scripts\activate

#Unix or Linux activation:
source myvenv/bin/activate
pip install -r requirements.txt
```
1. Configure your database settings in `settings.py`.
2. Apply database migrations: `python manage.py migrate`
3. Create a superuser for admin access: `python manage.py createsuperuser`
4. Run the development server: `python manage.py runserver`

- go to the project folder
- run `docker-compose up -d --build`
- create a test super account with `docker-compose exec backend python manage.py create_test_superuser`
- visit `localhost:8000/admin/` or `127.0.0.1:8000/admin/` and paste the generated credentials

### Running Tests

To run the tests, follow these steps:

- In folder **accounts** run `tests.py`
- In folder **images** run `tests.py`
