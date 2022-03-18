from bottle import get, run, static_file


############### MODULES ###############
import index_get          # GET
import login_get          # GET
import signup_get         # GET
import users_get          # GET
import admin_get          # GET
import signup_success_get # GET
import logout_get         # GET
import create_tweet_get   # GET
import update_tweet_get   # GET

import signup_post        # POST
import login_post         # POST
import create_tweet_post  # POST
import remove_tweet_post  # POST
import update_tweet_post  # POST

import is_user_logged_in  # Sends a request

############### CSS ###############
@get("/app.css")
def _():
  return static_file("app.css", root=".")


############### RUN HOST/SERVER ###############
run(host="127.0.0.1", port=5555, debug=True, reloader=True, server="paste")