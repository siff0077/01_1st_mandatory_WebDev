from bottle import get, redirect, request, view

from is_user_logged_in import is_user_logged_in

@get("/create-tweet")
@view("create_tweet")
def index_view():
    if not is_user_logged_in():
        return redirect("/login")
    
    error = request.params.get("error")
    
    return dict(user_is_logged_in=is_user_logged_in(), error=error)
