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

def is_entered(text):
    try:
        str(text)
        return True
    except ValueError:
        return False

@app.route('/', methods=['POST'])
def validate_signup():
    username = request.form['username']
    password = request.form['password']
    password_verify = request.form['password_verify']
    email = request.form['email']
    password_length = len(password)
    email_length = len(email)

    username_error = ''
    password_error = ''
    password_verify_error = ''
    email_error = ''

    if len(username) >= 3 or len(username) <= 20: 
        username_error = 'Please enter a username.'
    else:
        username_error =''
    
    if not is_entered(password): 
        password_error = 'Please enter a password.'
    else:
        if password_length >= 3 and password_length <= 20:
           password_error = "Password must be 3 to 20 characters in length."
           password_error = ''
    
    if not is_entered(password_verify): 
        password_verify_error = 'Please reenter your password.'
    else:
        if password_verify != password:
            password_verify_error = "Passwords do not match."
            password_verify_error = ''

    if not is_entered(email):
        email_error = ''
    else:
        if email_length >= 3 and email_length <= 20 or '@' not in email and '.' not in email:
            email_error = "Please enter a valid email."

    if not username_error and not password_error and not password_verify_error and not email_error:
        # do i need to add the welcome copy here?
        return redirect('/valid_sign_up')
    else:
        return render_template('sign_up_form.html', username_error=username_error, 
        password_error=password_error, 
        password_verify_error=password_verify_error, 
        email_error=password_verify_error)
    
    return render_template('sign_up_form.html')

@app.route('/valid_sign_up')
def valid_sign_up():
    username = request.form('username')
    #request.args.get instead on line above?
    return render_template('welcome.html', username=username)

app.run()