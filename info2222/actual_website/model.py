import random
'''
    Our Model class
    This should control the actual "logic" of your website
    And nicely abstracts away the program logic from your page loading
    It should exist as a separate layer to any database or data structure that you might be using
    Nothing here should be stateful, if it's stateful let the database handle it
'''
import view

# Initialise our views, all arguments are defaults
page_view = view.View()

#-----------------------------------------------------------------------------
# Index
#-----------------------------------------------------------------------------

def index_page():
    return page_view("index")

#-----------------------------------------------------------------------------
# Login
#-----------------------------------------------------------------------------

def login_page():
    return page_view("login")

# Check the login credentials
def login_check(username, password):
    # By default assume bad creds
    login = True
    err_str = ""
    
    if username != "admin": # Wrong Username
        err_str += "Incorrect Username. "
        login = False
    
    if password != "password": # Wrong password
        err_str += "Incorrect Password."
        login = False
        
    if login: 
        return page_view("valid", name=username)
    else:
        return page_view("invalid", reason=err_str)
    
#-----------------------------------------------------------------------------
# Pages
#-----------------------------------------------------------------------------

def profile_page():
    return page_view("profile")

def messages_page():
    return page_view("messages")

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
        'ends': page_view("content/ends"),
    }[topic]

#-----------------------------------------------------------------------------
