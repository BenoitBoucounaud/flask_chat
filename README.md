# flask_chat
Little chat web app with Flask

## MongDB
Install MongoDB : https://docs.mongodb.com/manual/installation/
To run MongoDB on Ubuntu : https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/#run-mongodb-community-edition

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
