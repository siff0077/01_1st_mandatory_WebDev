from bottle import get, redirect, request, view
import jwt

import global_file
from is_user_logged_in import is_user_logged_in

@get("/admin")
@view("admin")
def admin_view():
    if not is_user_logged_in():
        return redirect("/login")
    
    # get user information to connect with own tweets and allow the user to edit or delete these
    user_session_jwt = request.get_cookie("jwt", secret="secret")
    if user_session_jwt not in global_file.SESSIONS:
        return redirect("/login")
    user_information = jwt.decode(user_session_jwt, global_file.JWT_VALIDATION_KEY, algorithms=["HS256"])
    user_id = user_information["id"]
    
    return dict(tweets=global_file.TWEETS, user_id=user_id, user_is_logged_in=is_user_logged_in())