# flask_chat
Little chat web app with Flask

## MongDB
Install MongoDB : https://docs.mongodb.com/manual/installation/   
To run MongoDB on Ubuntu : https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/#run-mongodb-community-edition

Create database and admin user (in mongod):  
```
use chatbase
db.users.insert({
    name: 'admin',
    password: 'password',
    creation_date: Date(),
    admin: true,
    online : false
})
```

## Virtualenv and requirtements
Install and create virtualenv 
https://docs.python-guide.org/dev/virtualenvs/ : 
```
python -m pip install --user virtualenv
virtualenv venv
```
Activate virtualenv and install requirtements : 
```
source venv/bin/activate
pip install -r requirements.txt
```

Daactivate virtualenv : 
```
deactivate
```

Tell your terminal the application to work with by exporting the FLASK_APP environment variable:
```
export FLASK_APP=main
```

Run flask : 
```
flask run
```
Application [here](http://127.0.0.1:5000)


## Docs 
[Flask](https://flask.palletsprojects.com/en/2.0.x/)
[Jinja2](https://jinja.palletsprojects.com/en/3.0.x/templates/)
[MongoDB](https://docs.mongodb.com)