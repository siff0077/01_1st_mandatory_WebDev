from bottle import get, request, view

from is_user_logged_in import is_user_logged_in

@get("/login")
@view("login")
def login_view():

    error = request.params.get("error")

    # get email from params to set as value in input 
    user_email = request.params.get("user_email")

    return dict(error=error, user_email=user_email, user_is_logged_in=is_user_logged_in())