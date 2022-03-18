from bottle import redirect, response, request, post
import re
import jwt

from global_file import JWT_VALIDATION_KEY, REGEX_EMAIL, SESSIONS, USERS


@post("/login")
def login_post():
    
    # email
    user_email = request.forms.get("user_email")
    if not user_email:
        return redirect("/login?error=user_email")
    if not re.match(REGEX_EMAIL, user_email):
        return redirect("/login?error=user_email")
    
    # password
    if not request.forms.get("user_password"):
        return redirect(f"/login?error=user_password&user_email={user_email}")
    
    # if email and password match a user's, log in, set session, set cookie and redirect to admin
    for user in USERS:
        if user["email"] == user_email and user["password"] == request.forms.get("user_password"):
            user["user_is_logged_in"] = True
            user_session_jwt = jwt.encode(user, JWT_VALIDATION_KEY, algorithm="HS256")
            SESSIONS.append(user_session_jwt)
            response.set_cookie("jwt", user_session_jwt, secret="secret")
            return redirect("/admin")

    return redirect("/login?error=no_user")
