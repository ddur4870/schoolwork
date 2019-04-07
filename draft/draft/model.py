'''
    Our Model class
    This should control the actual "logic" of your website
    And nicely abstracts away the program logic from your page loading
    It should exist as a separate layer to any database or data structure that you might be using
    Nothing here should be stateful, if it's stateful let the database handle it
'''
import view, sql, json
from datetime import datetime

# Initialise our views, all arguments are defaults
page_view = view.View()
db = sql.SQLDatabase()
db.database_setup()

# TUPLE
# ID[0], NAME[1], PASSWORD[2], AGE[3], BIO[4], ADMIN[5]
user = None


#-----------------------------------------------------------------------------
# Index
#-----------------------------------------------------------------------------

def index_page():
    return page_view("index")

#-----------------------------------------------------------------------------
# Login / rego 
#-----------------------------------------------------------------------------

def logout():
    global user
    user = None

def registration_page():
    return page_view("register")

def login_page():
    return page_view("login", error="noError")

# Check the login credentials
def login_check(username, password):
    global user

    if db.check_credentials(username, password):
        user = db.get_user(username)
        return page_view("loginFeedback/validLogin", name=user[1])
    else:
        return page_view("loginFeedback/invalidLogin")

# Check the registration credentials
def registration_check(username, password, confirmation, age):
    global user

    errors = []

    if password != confirmation:
        errors.append("Your passwords did not match.")

    if not any(char.isdigit() for char in password):
        errors.append("Your password must contain at least 1 number.")

    if not any(char.isupper() for char in password):
        errors.append("Your password must contain at least 1 capital letter.")
    
    if len(password) < 6:
        errors.append("Your password must be at least 6 characters long.")

    # errors is true when array is not empty
    if errors:
        return page_view("regoFeedback/invalidRego", error="  ".join(errors))
    else:
        db.add_user(username, password, age)
        user = db.get_user(username)
        return page_view("regoFeedback/validRego", name=user[1])
    
#-----------------------------------------------------------------------------
# Pages
#-----------------------------------------------------------------------------

def profile_page():
    global user
    if user == None:
        return page_view("login", error="profile")
    else:
        return page_view("profile", name=user[1], age=user[3], bio=user[4])

def messages_page():
    global user
    if user == None:
        return page_view("login", error="messages")
    else:
        messages = db.get_user_messages(user[1])
        return page_view("messages", name=user[1], messages=json.dumps(messages))

def content_page(topic):
    return {
        'ht-cs': page_view("content/ht-cs"),
        'jas': page_view("content/jas"),
        'pyt': page_view("content/pyt"),
        'apach': page_view("content/apach"),
        'ngin': page_view("content/ngin"),
        'aws': page_view("content/aws"),
        'azure': page_view("content/azure"),
        'digoc': page_view("content/digoc"),
        'net': page_view("content/net"),
        'php': page_view("content/php"),
        'frames': page_view("content/frames"),
        'stack': page_view("content/stack"),
        'ends': page_view("content/ends")
    }[topic]

#-----------------------------------------------------------------------------#-----------------------------------------------------------------------------
# Forms
#-----------------------------------------------------------------------------

def new_bio(bio):
    global user
    db.update_bio(user[1], bio)
    user = db.get_user(user[1])

def add_message(to, message):
    global user
    # https://docs.python.org/3/library/time.html#time.strftime
    time = datetime.now().strftime('%A, %d %b %Y %I:%M %p ') 
    db.add_new_message(user[1], to, message, time)