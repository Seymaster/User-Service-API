from strapi import db
import json
from datetime import datetime


class Users(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    fullname      = db.Column(db.String(128))
    dob           = db.Column(db.Integer)
    phone         = db.Column(db.Integer,unique=True)
    address       = db.Column(db.String(200),nullable=False)
    ofaddress     = db.Column(db.String(200),nullable=False)
    email         = db.Column(db.String(64), unique=True, index=True)
    password      = db.Column(db.String(100),nullable=False)
    marital       = db.Column(db.String(64),nullable=False)
    admin         = db.Column(db.Boolean,nullable=False,default=False)
    confirmed     = db.Column(db.Boolean ,nullable=False, default=False)
    confirmed_on  = db.Column(db.DateTime,nullable=True,default=datetime.now())
    date          = db.Column(db.DateTime,nullable=True,default=datetime.now())

    def __init__(self,fullname,dob,phone,address,ofaddress,email,password,admin,marital,confirmed,confirmed_on):
        self.fullname = fullname
        self.dob = dob
        self.phone = phone
        self.address = address
        self.ofaddress = ofaddress
        self.email    = email
        self.password = password
        self.marital = marital
        self.admin  = admin
        self.confirmed = confirmed
        self.confirmed_on = confirmed_on

    def json(self):
        return {'fullname': self.fullname, 'dob': self.dob, 'phone': self.phone, 'address': self.address,
                'ofaddress': self.ofaddress, 'email': self.email,'password': self.password, 'marital': self.marital}
    
# class Bookings(db.Model):
#     id            = db.Column(db.Integer, primary_key=True)
#     userID        = db.Column(db.Integer)
#     transactionID = db.Column(db.Integer)
#     name          = db.Column(db.String(80))
#     age           = db.Column(db.Integer)
#     address       = db.Column(db.String(240))
#     description   = db.Column(db.String(400))
#     amount        = db.Column(db.Integer)
#     date_created  = db.Column(db.DateTime,nullable=False,default=datetime.utcnow())

#     def __init__(self,userID,transactionID,name,age,address,description,amount):
#         self.userID        = userID
#         self.transactionID = transactionID
#         self.name          = name
#         self.age           = age
#         self.address       = address
#         self.description   = description
#         self.amount        = amount
    
#     def booking_serial(self):
#         return {'userID': self.userID, 'transactionID':self.transactionID, 'name': self.name, 'age': self.age,
#                 'address': self.address, 'description': self.description, 'amount': self.amount}

# class Services(db.Model):
#     id          = db.Column(db.Integer, primary_key=True)
#     name        = db.Column(db.String(60))
#     age         = db.Column(db.Integer)
#     address     = db.Column(db.String(200))
#     description = db.Column(db.String(500))
#     date        = db.Column(db.DateTime,nullable=False,default=datetime.utcnow())

#     def __init__(self,name,age,address,description):
#         self.name            = name
#         self.age             = age
#         self.address         = address
#         self.description     = description

#     def service_serial(self):
#         return {'name': self.name, 'age': self.age, 'address': self.address, 'description':self.description}
    

# class Contacts(db.Model):
#     id        = db.Column(db.Integer, primary_key=True)
#     firstname = db.Column(db.String(60))
#     lastname  = db.Column(db.String(60))
#     email     = db.Column(db.String(100))
#     message   = db.Column(db.String(1000))
#     date      = db.Column(db.DateTime,nullable=False,default=datetime.utcnow())

#     def __init__(self,firstname,lastname,email,message):
#         self.firstname = firstname
#         self.lastname  = lastname
#         self.email     = email
#         self.message   = message

#     def user_serialize(self):
#         return {'firstname': self.firstname, 'lastname': self.lastname, 'email': self.email, 'message':self.message}

db.create_all()

