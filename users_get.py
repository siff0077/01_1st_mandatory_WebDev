from bottle import get, view
import global_file

@get("/users")
@view("users")
def _():
  return dict(users=global_file.USERS)