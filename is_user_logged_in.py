from bottle import request
import jwt
from jwt.exceptions import InvalidSignatureError

import global_file

def is_user_logged_in():
    user_is_logged_in = False
    
    # if the jwt cookie is in SESSIONS and is valid set user_is_logged_in to value from user_information (True) else print error
    if request.get_cookie("jwt", secret="secret") and request.get_cookie("jwt", secret="secret") in global_file.SESSIONS:
        try:
            user_information = jwt.decode(request.get_cookie("jwt", secret="secret"), global_file.JWT_VALIDATION_KEY, algorithms=["HS256"]) or 'Nothing'
            user_is_logged_in = user_information["user_is_logged_in"]
        except InvalidSignatureError as error:
            print(f"Invalid signature error: {error}")

    return user_is_logged_in