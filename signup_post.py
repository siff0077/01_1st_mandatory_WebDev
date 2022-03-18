from bottle import redirect, request, post
import re
import uuid

import global_file

@post("/signup")
def signup():
    # get the info from the form and validate
    errors = []
    form_inputs = {}

    # first name
    new_user_first_name = request.forms.get("new_user_first_name")
    if not new_user_first_name:
        errors.append("first-name-missing")
    elif len(new_user_first_name) < 2 or len(new_user_first_name) > 20:
        errors.append("first-name-length")
    if new_user_first_name:
        form_inputs["first-name"] = new_user_first_name

    # last name
    new_user_last_name = request.forms.get("new_user_last_name")
    if not new_user_last_name:
        errors.append("last-name-missing")
    else:
        form_inputs["last-name"] = new_user_last_name

    # email
    new_user_email = request.forms.get("new_user_email")
    if not new_user_email:
        errors.append("email-missing")
    elif not re.match(global_file.REGEX_EMAIL, new_user_email):
        errors.append("email-invalid")
    if not new_user_email == '':
        form_inputs["email"] = new_user_email

    # password
    new_user_password = request.forms.get("new_user_password")
    if not new_user_password:
        errors.append("password-missing")
    elif len(new_user_password) < 6:
        errors.append("password-short")

    # potential error messages
    if not errors == []:
        error_string = f'{"=error&".join(errors)}=error'
        form_input_string = ''
        for value in form_inputs:
            form_input_string += f"&{value}={form_inputs[value]}"
        return redirect(f"/signup?{error_string}{form_input_string}")
    
    # append user to USERS
    new_user = {
        "first_name": new_user_first_name,
        "last_name": new_user_last_name,
        "email": new_user_email,
        "password": new_user_password,
        "id": str(uuid.uuid4())
    }
    global_file.USERS.append(new_user)

    return redirect("/signup-success")
