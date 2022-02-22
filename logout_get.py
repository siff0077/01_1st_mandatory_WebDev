from bottle import get, redirect, request
import uuid
import jwt
import time

@get("/logout")
def _():
  user_session_id = request.get_cookie("uuid4")
  sessions.remove(user_session_id)
  jwt_session = request.get_cookie("user_email")
  sessions.remove(jwt_session)
  return redirect("/login")