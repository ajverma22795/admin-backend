from config import USER_COLLECTION
from datetime import datetime
import pymongo
def add_user(userId, password, firstName, lastName):
    try:
        result = USER_COLLECTION.insert_one(
            {
                "userId":userId,
                "password":password,
                "firstName":firstName,
                "lastName":lastName,
                "created_date":datetime.now(),
                "update_date":datetime.now()
            }
        )
        return {
            "status":1,
            "message":"user inserted successfully"
        }
    except pymongo.errors.DuplicateKeyError:
        return {
            "status":-1,
            "message":"user already exist"
        }

def update_user(userId, password, firstName, lastName):
    try:
        result = USER_COLLECTION.update_one(
            {
                "userId":userId,
            },
            {
                "$set":{
                    "password":password,
                    "firstName":firstName,
                    "lastName":lastName,
                    "update_date":datetime.now()
                }
            }
            
        )
        if result.matched_count > 0:
            return {
                "status":1,
                "message":"user updated successfully"
            }
        else:
            return {
            "status":-1,
            "message":"user not found!"
        }
    except Exception as e:
        return {
            "status":-1,
            "message":str(e)
        }
        
def delete_user(userId):
    try:
        result = USER_COLLECTION.delete_one(
            {
                "userId":userId
            }
        )
        if result.deleted_count > 0:
            return {
                "status":1,
                "message":"user deleted successfully"
            }
        else:
            return {
            "status":-1,
            "message":"user not found!"
        }
    except Exception as e:
        return {
            "status":-1,
            "message":str(e)
        }

def validate_user(userId, password):
    try:
        result = USER_COLLECTION.find_one(
            {
                "userId":userId
            }
        )
        if result:
            if result['password']==password:
                return {
                    "status":1,
                    "firstName":result['firstName'],
                    "lastName":result['lastName'],
                    "message":"user verified successfully"
                }
            else:
                return {
                    "status":0,
                    "message":"incorrect password"
                }
        else:
            return {
            "status":-1,
            "message":"user not found!"
        }
    except Exception as e:
        return {
            "status":-1,
            "message":str(e)
        }
