#import the F;ask and render_template class from flask module
from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps #for login decorators
#Create flask object and assign to app
app = Flask(__name__)
app.secret_key = "My Layday" #adding secret key to make a session encryption key. Session relys on cookie. This key helps to access actual data on server side
app.config["DEBUG"] = True #This will do same as: app.run(debug = 'True')

#login decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first!")
            return redirect(url_for('login'))
    return wrap


#Use decorators to link functions to url
@app.route('/')
@app.route('/home')
@login_required
def home():
    #return "Hello, World!"
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods = ['GET', 'POST']) #HTTP method which is by default is a GET request when we dont mention it
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'Almazi' or request.form['password'] != 'Almazi':
            error = "Wrong credentials. Please type again."
        else:
            flash('You are just logged in')
            session['logged_in'] = True
            return redirect(url_for('home')) #after giving correct credentials it will 302 redirect to welcome page

    return render_template('login.html', error = error)

@app.route('/logout')
@login_required
def logout():
    flash('You are just logged out!')
    session.pop('logged_in', None) #Pop the logged_in key and delete it. If someone goes to /logout route then we pop out the logged_in key and replace with empty None dictionary
    return redirect(url_for('welcome')) #this home is functions name, will redirect to home function after going to logout url

#Running app
if __name__ == '__main__':
    app.run(debug = 'True')
