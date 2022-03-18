from bottle import get, request, redirect
import global_file

@get("/logout")
def logout():

    # remove cookie from session to log out the user
    user_session_id = request.get_cookie("jwt", secret="secret")
    global_file.SESSIONS.remove(user_session_id)
    
    return redirect("/login")