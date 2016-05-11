import sqlite3

with sqlite3.connect("sample.db") as connection:
    c = connection.cursor()
    c.execute("drop TABLE posts") #To debug the error. if the db is opened alrady it will close and reopen otherwise it shows error
    c.execute("CREATE TABLE posts(title TEXT, description TEXT)")

    c.execute("INSERT INTO posts VALUES('Name: ', 'Almazi')")
    c.execute("INSERT INTO posts VALUES('Date: ', 'May 12, 2016')")
    c.execute("INSERT INTO posts VALUES('Mood: ', 'Awesome!')")
    c.execute("INSERT INTO posts VALUES('Reason: ', 'After trying for so long on my windows pc I logged into ubuntu, upgraded it, updated everything, installed everything needed for flask and here I am launched my first Flask app on Heroku!!!!')")
