from flask import Flask, render_template, request
from init_db import db_connection
from werkzeug.security import check_password_hash

app = Flask(__name__)

try:
    cursor, connection = db_connection(r"./databases/database.db")
    cursor.execute("""SELECT ItemType, Ingredients, Description, course, flavour, Price FROM menu;""")
    menu_items = cursor.fetchall()
    cursor.close()
    connection.close()
except:
    print("Database connection error")

@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', items=menu_items)

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email= request.form['email']
        pwd = request.form['pwd']

        try:
            cursor, connection = db_connection(r"./databases/database.db")
            cursor.execute("""SELECT Name, Email, pwdhash FROM customer;""")
            users_list = cursor.fetchall()
            cursor.close()
            connection.close()
        except:
            print("Database connection error")

        # Check the password hash of the user in database
        print(pwd)
        if check_password_hash(users_list[2][2], pwd):
            return "<!Doctype html><html lang='en'><head><title>Test</title></head><body></body><h1>Logged in</h1></html>"
        else:
            return "<!Doctype html><html lang='en'><head><title>Test</title></head><body></body><h1>wrong password</h1></html>"
    else:
        return render_template('login.html')


@app.route('/feedback')
def feedback():
    return render_template('feedback.html')


if __name__ == "__main__":
    app.run(debug=True)
