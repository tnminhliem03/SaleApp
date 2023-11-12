from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

<<<<<<< HEAD
app.secret_key = '!@#$%^&*()~AGDSVB'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/saledbv1?charset=utf8mb4' % quote('Liemkute03')
=======
app.secret_key = '~!@##$%^&*()HGYUJKO123453'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/saledbv1?charset=utf8mb4' % quote('Admin@123')
>>>>>>> 33daaebf4c1d056d1a53ade8b6fd1f89ac3707b3
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True


db = SQLAlchemy(app = app)
login = LoginManager(app = app)