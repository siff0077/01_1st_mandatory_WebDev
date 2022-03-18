from bottle import get, redirect, view

import global_file
from is_user_logged_in import is_user_logged_in

@get("/users")
@view("users")
def users_view():
    if not is_user_logged_in():
        return redirect("/login")
    return dict(users=global_file.USERS, user_is_logged_in=is_user_logged_in())

