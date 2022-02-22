from bottle import post, redirect, response, request
import global_file
import re
import uuid
import jwt
import time

@post("/login")
def _():
  # VALIDATE
  # FIRST THING: Always check if the vriable was passed in the form
  if not request.forms.get("user_email"):
    return redirect("/login?error=user_email")
  if not re.match(global_file.REGEX_EMAIL, request.forms.get("user_email")):
    return redirect("/login?error=user_email")

  user_password = request.forms.get("user_password")
  user_email = request.forms.get("user_email")
  # FIRST THING: Always check if the vriable was passed in the form
  if not request.forms.get("user_password"):
    return redirect(f"/login?error=user_password&user-email={user_email}")
  if len(request.forms.get("user_password")) < 6:
    return redirect(f"/login?error=user_password&user-email={user_email}")
  if len(request.forms.get("user_password")) > 50:
    return redirect(f"/login?error=user_password&user-email={user_email}")

  for user in global_file.USERS:
    if request.forms.get("user_email") == user["email"] and request.forms.get("user_password") == user["password"]:
      
      user_session_id = str(uuid.uuid4())
      global_file.SESSIONS.append(user_session_id)
      response.set_cookie("uuid4", user_session_id)
      encoded_jwt_user_email = jwt.encode({"user_email":user_email}, global_file.COOKIE_SECRET, algorithm="HS256")
      print("#"*30)
      print(encoded_jwt_user_email)
      jwt_session = str(encoded_jwt_user_email)
      global_file.SESSIONS.append(jwt_session)
      response.set_cookie("user_email", encoded_jwt_user_email)

      return redirect("/admin")
      # SUCCESS

  return redirect("/login?error=unknown_user_information")