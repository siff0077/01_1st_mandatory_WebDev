from bottle import redirect, post

import global_file

@post("/remove-tweet/<id>")
def delete_tweet_post(id):

    # find tweet to delete based on id i url
    for index, tweet in enumerate(global_file.TWEETS):
        if tweet["id"] == id:
            global_file.TWEETS.pop(index)

    return redirect("/admin")