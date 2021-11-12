# flask_chat
Little chat web app with Flask

Install and create virtualenv 
https://docs.python-guide.org/dev/virtualenvs/ : 
```
python -m pip install --user virtualenv
virtualenv venv
```
Activate virtualenv and install packages : 
```
source venv/bin/activate
pip install Flask
pip install flask-socketio
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
