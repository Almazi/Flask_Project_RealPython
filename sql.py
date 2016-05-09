import sqlite3

with sqlite3.connect("sample.db") as connection:
    c = connection.cursor()
    c.execute("drop TABLE posts") #To debug the error. if the db is opened alrady it will close and reopen otherwise it shows error
    c.execute("CREATE TABLE posts(title TEXT, description TEXT)")
    c.execute("INSERT INTO posts VALUES('Good: ', 'I am good!')")
    c.execute("INSERT INTO posts VALUES('Well: ', 'I am well!')")
