from bottle import redirect, request, post
import time

import global_file

@post("/update-tweet/<id>")
def edit_tweet_post(id):
    
    # title
    tweet_title = request.forms.get("edit_tweet_title")
    if not tweet_title:
        print("No title")
    
    # description
    tweet_description = request.forms.get("edit_tweet_description")
    if not tweet_description:
        print("No description")
    
    # it's not possible to post a tweet without a title or description
    if not tweet_title:
        if not tweet_description:
            return redirect(f"/update-tweet/{id}?error=empty")
    
    # find tweet to update and update the relevant values
    for index, tweet in enumerate(global_file.TWEETS):
        if tweet["id"] == id:
            tweet["title"] = tweet_title
            tweet["description"] = tweet_description
            tweet["time_edited"] = time.localtime()

    return redirect("/admin")
