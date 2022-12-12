# include 4 tables here: BankAcct, Equipment, Order, Order-Equipment tables here
from app import db
from datetime import datetime

class BankAcct(db.Model):
    id = db.Column(db.Integer, primary_key=True)