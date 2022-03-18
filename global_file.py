import uuid
import time

USERS = []
SESSIONS = []
TWEETS = []


REGEX_EMAIL = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'

JWT_VALIDATION_KEY = f"{str(uuid.uuid4())}-{str(uuid.uuid4())}"

