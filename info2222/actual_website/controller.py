from bottle import route, get, post, request, redirect, static_file

import model

#-----------------------------------------------------------------------------
'''
    This file will handle our typical Bottle requests and responses 
    You should not have anything beyond basic page loads, handling forms and 
    maybe some simple program logic
'''
#-----------------------------------------------------------------------------
# Static file paths
#-----------------------------------------------------------------------------

# Allow image loading
@route('/img/<picture:path>')
def serve_pictures(picture):
    return static_file(picture, root='img/')

#-----------------------------------------------------------------------------

# Allow CSS
@route('/css/<css:path>')
def serve_css(css):
    return static_file(css, root='css/')

#-----------------------------------------------------------------------------

# Allow javascript
@route('/js/<js:path>')
def serve_js(js):
    return static_file(js, root='js/')

#-----------------------------------------------------------------------------
# Pages
#-----------------------------------------------------------------------------

# Redirect to login
@get('/')
@get('/home')
def get_index():
    return model.index_page()

#-----------------------------------------------------------------------------

# Display the login page
@get('/login')
def get_login_controller():
    return model.login_page()

# Attempt the login
@post('/login')
def post_login():
    # Handle the form processing
    username = request.forms.get('user_name')
    password = request.forms.get('user_password')
    
    # Call the appropriate method
    return model.login_check(username, password)


#-----------------------------------------------------------------------------

@get('/profile')
def get_about():
    return model.profile_page()

#-----------------------------------------------------------------------------

@get('/message')
def get_messages():
    return model.messages_page()
   

#-----------------------------------------------------------------------------

@get('/<topic>')
def get_content(topic):
    return model.content_page(topic)
