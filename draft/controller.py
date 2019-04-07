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

@route('/content/img/<picture:path>')
def serve_pictures_two(picture):
    return static_file(picture, root='img/')

#-----------------------------------------------------------------------------

# Allow CSS
@route('/css/<css:path>')
def serve_css(css):
    return static_file(css, root='css/')

@route('/content/css/<css:path>')
def serve_css_two(css):
    return static_file(css, root='css/')

#-----------------------------------------------------------------------------

# Allow javascript
@route('/js/<js:path>')
def serve_js(js):
    return static_file(js, root='js/')

@route('/content/js/<js:path>')
def serve_js_two(js):
    return static_file(js, root='js/')

#-----------------------------------------------------------------------------
# Pages
#-----------------------------------------------------------------------------

# Redirect to home page
@get('/')
@get('/home')
def get_index():
    return model.index_page()

@get('/loginpage')
def get_login_page():
    return model.login_page()

#-----------------------------------------------------------------------------

@get('/logout')
def logout():
    model.logout()
    redirect('/')

@get('/register')
def rego():
    return model.registration_page()

# Attempt the login
@post('/login')
def post_login():
    # Handle the form processing
    username = request.forms.get('user_name')
    password = request.forms.get('user_password')
    
    # Call the appropriate method
    return model.login_check(username, password)

@post('/register')
def post_rego():
    # Handle the form processing
    username = request.forms.get('user_name')
    password = request.forms.get('user_password')
    confirmation = request.forms.get('user_password_confirm')
    age = request.forms.get('user_age')

    # Call the appropriate method
    return model.registration_check(username, password, confirmation, age)

@post('/newBio')
def post_bio():
    newBio = request.forms.get('new_bio')
    model.new_bio(newBio)
    redirect("/profile")


#-----------------------------------------------------------------------------

@get('/profile')
def get_about():
    return model.profile_page()

#-----------------------------------------------------------------------------

@get('/message')
def get_messages():
    return model.messages_page()

@post('/newMessage')
def new_message():
    recipient = request.forms.get('recipient')
    message = request.forms.get('message')

    model.add_message(recipient, message)
    redirect("/message")
   

#-----------------------------------------------------------------------------

@get('/content/<topic>')
def get_content(topic):
    return model.content_page(topic)

