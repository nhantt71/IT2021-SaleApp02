from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_login import LoginManager
import cloudinary


app = Flask(__name__)
app.secret_key = '%#%$#%$#G#$GGEG%H$%H%$H^HTH$Hdgdgdfgfd'
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:%s@localhost/saledb' % quote('Admin@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_RECORD_QUERIES"] = True
app.config['PAGE_SIZE'] = 6

db = SQLAlchemy(app)
login = LoginManager(app=app)


cloudinary.config(
    cloud_name='dsp3ymism',
    api_key='743313142469438',
    api_secret='wpyGYniqdIjJEzGntOe8WHbh6tg'
)



