from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app=Flask(__name__)
app.config['DEBUG'] = True

#this is where the html used to be

#sign_up_form = sign_up_form.format(username='', username_error='', password='', password_error='', password_verify='', password_verify_error='', email='', email_error='')

@app.route('/')
def sign_up_form():
    return render_template('sign_up_form.html')

@app.route('/', methods=['POST'])
def validate_signup():
    username = request.form['username']
    password = request.form['password']
    password_verify = request.form['password_verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    password_verify_error = ''
    email_error = ''

    if len(username) <= 3 or len(username) >= 20: 
        username_error = 'Please enter a valid username.'
    
    if len(password) == 0: 
        password_error = 'Please enter a password.'
    elif len(password) <= 3 and len(password) >= 20:
        password_error = "Password must be 3 to 20 characters in length."
    
    if password_verify != password:
        password_verify_error = "Passwords do not match."

    if len(email) > 0:
        if '@' not in email and '.' not in email:
            email_error = "Please enter a valid email."

    if not username_error and not password_error and not password_verify_error and not email_error:
        # do i need to add the welcome copy here?
        return render_template('welcome.html', username=username)
    else:
        return render_template('sign_up_form.html', username_error=username_error, 
        password_error=password_error, 
        password_verify_error=password_verify_error, 
        email_error=email_error)
    
@app.route('/valid_sign_up')
def valid_sign_up():
    username = request.args.get('username') 
    return render_template('welcome.html', username=username) #, username=username

app.run()