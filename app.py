from flask import Flask, render_template, request, redirect, url_for
from init_db import db_connection
from werkzeug.security import generate_password_hash, check_password_hash

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

    if request.method == 'POST':
        fName = request.form['fname']
        lName = request.form['lname']
        sEmail = request.form['email']
        phone = request.form['phoneNum']
        sPwd = request.form['pwd'] 
        print(fName, lName, sEmail, phone, sPwd)
        try:
            cursor, connection = db_connection(r"./databases/database.db")
            cursor.execute("""INSERT INTO customer('Name','Email','pwdhash','phone_number') VALUES (?,?,?,?);""", ( fName + " " + lName, sEmail, generate_password_hash(sPwd), phone))
            connection.commit()
            cursor.close()
            connection.close()
        except:
            return "<!Doctype html><html lang='en'><head><title>Test</title></head><body></body><h1>Database connection error</h1></html>"

        return redirect(url_for('login'))
    else:
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
            return "<!Doctype html><html lang='en'><head><title>Test</title></head><body></body><h1>Database connection error</h1></html>"
        
        user = {}
        
        for i, n in enumerate(users_list):
            user[users_list[i][1].lower()] = users_list[i][2]

        # Check the password hash of the user in database
        if (email.lower() in user) and (user[email.lower()], pwd):
            return redirect(url_for('index'))
        else:
            return "<!Doctype html><html lang='en'><head><title>Test</title></head><body></body><h1>wrong password</h1></html>"
    else:
        return render_template('login.html')


@app.route('/feedback')
def feedback():
    return render_template('feedback.html')


if __name__ == "__main__":
    app.run(debug=True)
