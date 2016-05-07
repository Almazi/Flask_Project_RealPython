#import the F;ask and render_template class from flask module
from flask import Flask, render_template

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

@app.route('/search/<search_queries>')
def search(search_queries):
    return search_queries

@app.route("/integer/<int:value>")
def int(value):
    value = value + value**5
    print(value) #This will print on terminal / ide
    return "Integering" #This will show on browser
@app.route("/float/<float:value>")
def float(value):
    value = value / 1.0
    print(value)
    return format(value) #Showing the value on browser after formatting

@app.route("/check/<path:value>")
def check(value):
    print(value)
    return "UTF Path"

#Will add the response along with status code at the end, which is optional but good for RESTful API
@app.route("/response/<name>")
def responses(name):
    if name.lower() == "almazi":
        return "The name is zi, {}".format(name), 200
    else:
        return "Not found", 404

#Running app
if __name__ == '__main__':
    app.run(debug = 'True')
