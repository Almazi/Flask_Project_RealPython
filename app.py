#import the F;ask and render_template class from flask module
from flask import Flask, render_template, redirect, url_for, request, session, flash, g #g saves the object based on queries which resets after every request
from functools import wraps #for login decorators
import sqlite3

#Create flask object and assign to app
app = Flask(__name__)
app.secret_key = "My Layday" #adding secret key to make a session encryption key. Session relys on cookie. This key helps to access actual data on server side
app.config["DEBUG"] = True #This will do same as: app.run(debug = 'True')
app.database = "sample.db"
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
    g.db = connect_db() #saving the temporary conection object
    qur = g.db.execute('select * from posts') #qur will query/fethc the data from posts table
    #print(qur) #this will show a <sqlite3.Cursor object at 0x00000186EEB9E030>
    #print(qur.fetchall()) #this will print a tuple
    posts = []
    post_dictionary = {}
    for row in qur.fetchall():
        post_dictionary["title"] = row[0] #title is taken from row[0] of all fetched tuple data
        post_dictionary["description"] = row[1] #description is taken from row[1] of all fethced data
        #print(post_dictionary) #it will show the dictionary of datas with key and value
        #posts.append(post_dictionary) #it will add the dictionary key and value to list
        #print(posts) #it will show the list
        #posts.append(dict(title = row[0], description = row[1]))
    posts.append(post_dictionary)
    #posts = [dict(title = row[0], description = row[1]) for row in qur.fetchall()] #list comprehenson of same for loop above: after fetching the data from posts it will save it in a dictionary "posts"
    g.db.close() #closing the database
    return render_template('index.html', posts = posts) #passing the posts list to template

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


def connect_db():
    return sqlite3.connect(app.database)

#Running app
if __name__ == '__main__':
    app.run(debug = 'True')
