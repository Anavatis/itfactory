from datetime import datetime

from app import db
from models.employee import Employee

store_employee = db.Table('store_employee',
    db.Column('store_name',
              db.String(255),
              db.ForeignKey('store.name'),
              primary_key=True),
    db.Column('employee_phone',
              db.String(255),
              db.ForeignKey('employee.phone_number'),
              primary_key=True)
)


class Store(db.Model):
    __tablename__ = 'store'

    name = db.Column(db.String(255), primary_key=True)
    employees = db.relationship('Employee', secondary=store_employee, lazy='subquery',
        backref=db.backref('stores', lazy=True))


class Visit(db.Model):

    index = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    visited_on = db.Column(db.DateTime(), default=datetime.utcnow)
    store_name = db.Column(db.String(255), db.ForeignKey(Store.name))
    latitude = db.Column(db.Float())
    longitude = db.Column(db.Float())
