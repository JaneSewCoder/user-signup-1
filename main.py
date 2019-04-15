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
    template = jinja_env.get_template('sign_up_form.html')
    return template.render()
    #return render_template('sign_up_template.html')

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

    if not is_entered(username): 
        username_error = 'Please enter a username.'
    else:
        username_error =''
    
    if not is_entered(password): 
        password_error = 'Please enter a password.'
    else:
        if password_length >= 3 and password_length <= 20:
           password_error = "Password must be between 3 and 20 characters long."
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
        if email_length >= 3 and email_length <= 20 or '@' and '.' not in email:
            email_error = "Please enter a valid email."

    if not username_error and not password_error and not password_verify_error and not email_error:
        # do i need to add the welcome copy here?
        return redirect('/valid_sign_up')
    else:
        template = jinja_env.get_template('sign_up_form.html')
        return template.render(username_error=username_error, 
        password_error=password_error, 
        password_verify_error=password_verify_error, 
        email_error=password_verify_error)

@app.route('/valid_sign_up')
def valid_sign_up():
    username = request.form('username')
    #request.args.get instead on line above?
    template =jinja_env.get_template('welcome.html')
    return template.render(username=username)

app.run()