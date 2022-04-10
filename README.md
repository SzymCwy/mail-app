
# Mail app

Simpl email app made in django rest framework. The idea of application was to 
create application which allows to send emails. There are 3 models. Mailbox
stores information about the connection to smtp server. Template is used to store data
of the mail message - Topic, attatchment and content. Email takes 2 foreign keys - Mailbox and Template, information
about the recipients - to, cc, bcc arrays. Reply email and both date and sent date.



## Setup

Install Django on your computer

Install required libraries
```bash 
pip install -r requirements.txt
```
Run migrations to create database migrations, firstly for app because of modified User.
```bash 
py manage.py makemigrations
```

```bash 
py manage.py migrate
```

```bash 
py manage.py makemigrations mailapp
```
```bash 
py manage.py migrate mailapp
```

Create superuser to manage program
```bash 
py manage.py migrate mailapp
```

Run the server
```bash 
py manage.py migrate mailapp
```
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file.
Name, user, password, host and port are required to login to postgresql database and secret is django
secret key and celery_url is needed to connect celery to redis.

`NAME`
`USER`
`PASSWORD`
`HOST`
`PORT`
`SECRET`
`CELERY_URL`

## Authors

- [@Szymon Cwynar](https://www.github.com/szymcwy)


## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/szymon-cwynar-b1b4b5232/)


