#import the F;ask and render_template class from flask module
from flask import Flask, render_template, redirect, url_for, request

#Create flask object and assign to app
app = Flask(__name__)

app.config["DEBUG"] = True #This will do same as: app.run(debug = 'True')

#Use decorators to link functions to url
@app.route('/')
@app.route('/hello')
def hello():
    return "Hello, World!"

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
            return redirect(url_for('welcome')) #after giving correct credentials it will 302 redirect to welcome page

    return render_template('login.html', error = error)



#Running app
if __name__ == '__main__':
    app.run(debug = 'True')
