from bottle import get, redirect, request, view

import global_file 
from is_user_logged_in import is_user_logged_in

@get("/update-tweet/<id>")
@view("update_tweet.html")
def edit_tweet_view(id):
    if not is_user_logged_in():
        return redirect("/login")
    
    tweet_to_edit = {}
    error = request.params.get("error")
    
    # find tweet to edit based on id in url
    for index, tweet in enumerate(global_file.TWEETS):
        if tweet["id"] == id:
            tweet_to_edit = tweet
    
    return dict(user_is_logged_in=is_user_logged_in(), tweet=tweet_to_edit, error=error)
