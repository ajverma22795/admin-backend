from collections import UserDict
from flask import Flask, request
import os
import json

from user import add_user, delete_user, update_user, validate_user
from admin import admin_signup, admin_login, forgot_admin, create_new_admin_password

headers = {
  'Content-Type': 'application/json'
}

app=Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/health')
def health():
    return "healthy"

@app.route('/addUser', methods=['POST'])
def addUser():
    input_data = json.loads(request.data)
    userId = input_data["userId"]
    password = input_data["password"]
    firstName = input_data["firstName"]
    lastName = input_data["lastName"]
    return json.dumps(add_user(userId, password, firstName, lastName))

@app.route('/updateUser', methods=['POST'])
def updateUser():
    input_data = json.loads(request.data)
    userId = input_data["userId"]
    password = input_data["password"]
    firstName = input_data["firstName"]
    lastName = input_data["lastName"]
    return json.dumps(update_user(userId, password, firstName, lastName))

@app.route('/deleteUser', methods=['POST'])
def deleteUser():
    input_data = json.loads(request.data)
    userId = input_data["userId"]
    return json.dumps(delete_user(userId))

@app.route('/validateUser', methods=['POST'])
def validateUser():
    input_data = json.loads(request.data)
    userId = input_data["userId"]
    password = input_data["password"]
    return json.dumps(validate_user(userId, password))

@app.route('/adminSignup', methods=['POST'])
def adminSignup():
    input_data = json.loads(request.data)
    adminId = input_data["adminId"]
    password = input_data["password"]
    firstName = input_data["firstName"]
    lastName = input_data["lastName"]
    fatherName = input_data["fatherName"]
    dob = input_data["dob"]
    firstSchool = input_data["firstSchool"]
    return json.dumps(admin_signup(adminId, password, firstName, lastName, fatherName, dob, firstSchool))

@app.route('/adminLogin', methods=['POST'])
def adminLogin():
    input_data = json.loads(request.data)
    adminId = input_data["adminId"]
    password = input_data["password"]
    return json.dumps(admin_login(adminId, password))

@app.route('/forgotAdmin', methods=['POST'])
def forgotAdmin():
    input_data = json.loads(request.data)
    adminId = input_data["adminId"]
    fatherName = input_data.get("fatherName")
    dob = input_data.get("dob")
    firstSchool = input_data.get("firstSchool")
    return json.dumps(forgot_admin(adminId, fatherName, dob, firstSchool))

@app.route('/createNewAdminPassword', methods=['POST'])
def createNewAdminPassword():
    input_data = json.loads(request.data)
    adminId = input_data["adminId"]
    password = input_data["password"]
    return json.dumps(create_new_admin_password(adminId, password))

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=5115)
