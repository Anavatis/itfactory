from app import db


class Employee(db.Model):
    __tablename__ = 'employee'

    # :TODO employee_id
    name = db.Column(db.String(255), unique=False)
    phone_number = db.Column(db.String(255), primary_key=True)

    def to_dict(self):
        return dict(name=self.name,
                    phone_number=self.phone_number)

