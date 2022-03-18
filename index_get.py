from bottle import get, view


from is_user_logged_in import is_user_logged_in

@get("/")
@view("index")
def index_view():
    
    return dict(user_is_logged_in=is_user_logged_in())
