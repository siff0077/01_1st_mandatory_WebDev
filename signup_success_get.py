from bottle import get, view

from is_user_logged_in import is_user_logged_in

@get("/signup-success")
@view("signup_success")
def signup_success_view():
    return dict(user_is_logged_in=is_user_logged_in())
