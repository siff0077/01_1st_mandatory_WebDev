from bottle import post, request, redirect
import global_file
import uuid
import jwt
import time

@post("/signup")
def _():
  # VALIDATE


  user_id = str(uuid.uuid4())
  user_firstname = request.forms.get("user_firstname")
  user_lastname = request.forms.get("user_lastname")
  user_email = request.forms.get("user_email")
  user_password = request.forms.get("user_password")

  # encoded_jwt_user_information = jwt.encode({"user_id":user_id, "user_email":user_email, "user_firstname":user_firstname, "user_lastname":user_lastname}, "30b6aad5-493e-4253-8de6-1d118d36f633cae8b31a-7ee7-4c8e-9adf-5cc98b3e3af4", algorithm="HS256")

  # print("#"*30)
  # print(encoded_jwt_user_information)

  user = {"id":user_id, "email":user_email, "firstname":user_firstname, "lastname":user_lastname, "password":user_password}
  global_file.USERS.append(user)
  print(global_file.USERS)
  return redirect(f"/signup-succes?user-email={user_email}&user-firstname={user_firstname}&user-lastname={user_lastname}&user-password={user_password}")
