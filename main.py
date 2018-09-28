from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

def valid_entry(user_data):
    if len(user_data) > 3 and len(user_data) < 20 and " " not in user_data:
        return True
    else:
        return False

def email_entry(user_data):
    if "@" and "." in user_data:
        return True
    else:
        return False

@app.route("/welcome", methods=['post'])
def user_signup():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    entry_error = "Error: Entry not valid. (0-20 characters, no spaces)"
    pass_error = "Error: Passwords do not match. "
    email_entry_error = "Error: Email is not valid."

    if not valid_entry(username):
        username_error = entry_error
    if not valid_entry(password):
        password_error = entry_error
    if not valid_entry(verify_password):
        verify_password_error = entry_error
    if not password == verify_password:
        password_error = pass_error
        verify_password_error = pass_error
    if email:
        if not email_entry(email):
            email_error = email_entry_error
        if not valid_entry(email):
            email_error = entry_error

    if not username_error and not password_error and not verify_password_error and not email_error:
        return render_template('welcome.html', username=username, password=password, verify_password=verify_password, email=email)
    else:
        return render_template('interface.html', username=username, username_error=username_error, password_error=password_error, verify_password_error=verify_password_error, email=email, email_error=email_error)

@app.route("/")
def index():
    return render_template('interface.html')

app.run()