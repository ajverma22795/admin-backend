from config import ADMIN_COLLECTION
from datetime import datetime
import pymongo


def admin_signup(adminId, password, firstName, lastName, fatherName, dob, firstSchool):
    try:
        result = ADMIN_COLLECTION.insert_one(
            {
                "adminId":adminId,
                "password":password,
                "firstName":firstName,
                "lastName":lastName,
                "fatherName":fatherName,
                "dob":dob,
                "firstSchool":firstSchool,
                "created_date":datetime.now(),
                "update_date":datetime.now()
            }
        )
        return {
            "status":1,
            "message":"admin inserted successfully"
        }
    except pymongo.errors.DuplicateKeyError:
        return {
            "status":-1,
            "message":"admin already exist"
        }

def admin_login(adminId, password):
    try:
        result = ADMIN_COLLECTION.find_one(
            {
                "adminId":adminId
            }
        )
        if result:
            if result['password']==password:
                return {
                    "status":1,
                    "message":"admin login successfully"
                }
            else:
                return {
                    "status":0,
                    "message":"incorrect password"
                }
        else:
            return {
            "status":-1,
            "message":"adminId not found!"
        }
    except Exception as e:
        return {
            "status":-1,
            "message":str(e)
        }
        
def forgot_admin(adminId, fatherName, dob, firstSchool):
    try:
        result = ADMIN_COLLECTION.find_one(
            {
                "adminId":adminId
            }
        )
        if result:
            if fatherName:
                if result['fatherName']==fatherName:
                    return {
                        "status":1,
                        "message":"admin verified"
                    }
                else:
                    return {
                        "status":0,
                        "message":"unable to verify"
                    }
            elif dob:
                if result['dob']==dob:
                    return {
                        "status":1,
                        "message":"admin verified"
                    }
                else:
                    return {
                        "status":0,
                        "message":"unable to verify"
                    }
            elif firstSchool:
                if result['firstSchool']==firstSchool:
                    return {
                        "status":1,
                        "message":"admin verified"
                    }
                else:
                    return {
                        "status":0,
                        "message":"unable to verify"
                    }
        else:
            return {
            "status":-1,
            "message":"adminId not found!"
        }
    except Exception as e:
        return {
            "status":-1,
            "message":str(e)
        }
        
        
def create_new_admin_password(adminId, password):
    try:
        result = ADMIN_COLLECTION.update_one(
            {
                "adminId":adminId,
            },
            {
                "$set":{
                    "password":password,
                    "update_date":datetime.now()
                }
            }
        )
        if result.matched_count > 0:
            return {
                "status":1,
                "message":"admin new password created successfully"
            }
        else:
            return {
            "status":-1,
            "message":"adminId not found!"
        }
    except Exception as e:
        return {
            "status":-1,
            "message":str(e)
        }