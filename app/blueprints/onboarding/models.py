# include 4 tables here: BankAcct, Equipment, Order, OrderEquipment tables here
from app import db
from datetime import datetime


class BankAcct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    acct_type = db.Column(db.String(50), nullable=False, default='checking')
    acct_number = db.Column(db.Integer, nullable=False)
    routing_number = db.Column(db.Integer, nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(kwargs)
        db.session.add(self)
        db.session.commit()


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    orders_equipments = db.relationship('OrderEquipment', backref='order', lazy=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()


class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amazon_id = db.Column(db.String) # this will stay empty for now, or will need to create instances of computers, mouses, keyboards
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, default='no description provided')
    category = db.Column(db.String(50), default='no category provided')
    price = db.Column(db.Float, default=0.00)
    image = db.Column(db.String)
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    orders_equipments = db.relationship('OrderEquipment', backref='equipment', lazy=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()


class OrderEquipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    equipment_id = db.Column(db.Integer, db.ForeignKey('equipment.id'), nullable=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()