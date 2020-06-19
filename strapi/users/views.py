from flask import request,jsonify,flash,url_for
from flask_login import login_user,current_user,logout_user,login_required
from strapi.models import Users
from strapi import db
from flask_restful import Resource,reqparse
from flask_jwt_extended import create_access_token
from strapi.users.token import generate_confirmation_token, confirm_token
from strapi.users.email import send_email
import json
import datetime


parser = reqparse.RequestParser()

class Usersapi(Resource):
    def get(self):
        return {
            "status": 200,
            "message": "user landing page"
        },200

    def post(self):
        parser.add_argument("fullname", type=str ,required=True)
        parser.add_argument("dob", type=int,required=True)
        parser.add_argument("phone", type=int,required=True)
        parser.add_argument("address", type=str,required=True)
        parser.add_argument("ofaddress", type=str,required=True)
        parser.add_argument("email", type=str,required=True)
        parser.add_argument("password", type=str,required=True)
        parser.add_argument("marital", type=str,required=True)
        args = parser.parse_args()
        # print(args)
        if all([args.get(field, False) for field in ["fullname", "dob","phone","address","ofaddress","email","marital"]]):
            user = Users(fullname = args["fullname"], dob = args["dob"], phone = args["phone"],
                         address = args["address"], ofaddress = args["ofaddress"],email = args["email"],
                         password=args["password"],marital = args["marital"],admin=False,confirmed=False,confirmed_on=datetime.datetime.now())
            serial_user = user.json()
            db.session.add(user)
            db.session.commit()
            token = generate_confirmation_token(user.email)
            confirm_url = url_for('confirmapi',token = token,_external=True)
            print(confirm_url)
            subject = "Please confirm your email"
            html = f"Thanks for signing up, follow this link to activate your account {confirm_url}" 
            send_email(user.email,subject,html)
            return {
                "status": 200,
                "message": "New user created",
                "user"   : serial_user
                },200
        return {"status": "BAD REQUEST"},404

class Resendapi(Resource):
    def get(self):
        return {"status": 200, "message": "Landing page"}

    def post(self):
        if current_user.email and current_user.confirmed:
            return {"Status": 200, "message": "User confirmed already"}
        else:
            args = parser.parse_args()
            token = generate_confirmation_token(user.email)
            confirm_url = url_for('confirmapi',token = token,_external=True)
            print(confirm_url)
            subject = "Please confirm your email"
            html = f"Thanks for signing up, follow this link to activate your account {confirm_url}" 
            send_email(user.email,subject,html)

        

class Confirmapi(Resource):
    def post(self,token):
        try:
            email = confirm_token(token)
        except:
            return {"status":"invalid Confirmation link"}
        user = Users.query.filter_by(email=email).first_or_404()
        if user.confirmed:
            return {"status":"Account confirmed already"}
        else:
            user.confirmed = True
            user.confirmed_on = datetime.datetime.now()
            db.session.add(user)
            db.session.commit()
            return {"status": 200, "Message": "User email confirmed"}
        return {"status": 200, "Message": "back to home page"}


# for clicking on resending of token and also verification of unconfirmed account
class Unconfirmapi(Resource):
    @login_required
    def post(self):
        if current_user.confirmed:
            return {"status": 200, "message":"you have been confirmed"}
        confirm_url = url_for('confirmapi',token = token,_external=True)
        return {"status": 300,"message": f"You have not been confirmed. goto {confirm_url} to be confirmed"}


class Loginapi(Resource):
    def get(self):
        email = "me@gsi.com"
        user = Users.query.filter_by(email=email).first_or_404()
        data = user.json()
        return {"status": 200, "message" : "user found","user": data }

    def post(self):
        parser.add_argument("email", type=str,required=True)
        parser.add_argument("password", type=str,required=True)
        args = parser.parse_args(strict=True)
        user = Users.query.filter_by(email = args["email"]).first_or_404()
        # print(user.password)
        # print(args["email"])
        if user:
            if user.password == args["password"]:
                token = create_access_token(identity=args["email"])
                return {
                    "status" : 200,
                    "message": "Login Successful",
                    "token"  : token,
                    },200
        return {"status": 500,
                "message":"Invalid Credentials"
                },500
