from application import db

class EmployeeTable(db.Model):
    emp_id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50),  nullable=False)
    email = db.Column(db.String(50), unique = True, nullable=False)
    phone_number =  db.Column(db.String(20) , nullable = True)
    address =  db.Column(db.String(200), nullable = True)

    #contructor of the call
    def __init__(self , fullname , email , phone_number , address):
        self.fullname = fullname
        self.email = email
        self.phone_number = phone_number
        self.address = address
