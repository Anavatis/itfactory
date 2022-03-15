from app import db


class Employee(db.Model):
    __tablename__ = 'employee'

    name = db.Column(db.String(255), unique=False)
    phone_number = db.Column(db.String(255), primary_key=True)

