from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('app_config')

db = SQLAlchemy(app)


from app.mod_stocks.controller import mod_stocks as stocks
app.register_blueprint(stocks)


db.create_all()