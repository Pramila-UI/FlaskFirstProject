from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# need to add the secret key
app.secret_key = "flask-secret_key-2lfdxa^_^q"

## postgres database setting for the sqlalchemy
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:root12345@localhost/flask_demo_db"

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:root12345@demo-django-instance.ct3mrfrtn3nf.ap-south-1.rds.amazonaws.com/demo_database"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from employee.views import *



if __name__ == "__main__":
    app.run(debug=True)
