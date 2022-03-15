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

    def to_dict(self):
        employees = [e.to_dict for e in self.employees]
        return dict(name=self.name,
                    employees=employees)


class Visit(db.Model):

    index = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    visited_on = db.Column(db.DateTime(), default=datetime.utcnow)
    store_name = db.Column(db.String(255), db.ForeignKey(Store.name))
    employee_phone = db.Column(db.String(255), db.ForeignKey(Employee.phone_number))
    latitude = db.Column(db.Float())
    longitude = db.Column(db.Float())

    def to_dict(self):
        return dict(visited_on=self.visited_on.timestamp(),
                    store_name=self.store_name,
                    employee_phone=self.employee_phone,
                    latitude=self.latitude,
                    longitude=self.longitude)
