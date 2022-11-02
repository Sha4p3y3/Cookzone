from flask import Flask, render_template, request, redirect, url_for
from sqlite3 import connect, IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

try:
    connection = connect(r"./databases/database.db")
    cursor = connection.cursor()
    cursor.execute("""SELECT ItemType, Ingredients, Description, course, flavour, Price FROM menu;""")
    menu_items = cursor.fetchall()
except:
    print("Database connection error")
finally:
    cursor.close()
    connection.close()

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
        try:
            connection = connect(r"./databases/database.db")
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO customer('Name','Email','pwdhash','phone_number') VALUES (?,?,?,?);""", ( fName + " " + lName, sEmail, generate_password_hash(sPwd), phone))
            connection.commit()
            cursor.close()
            connection.close()
        except (IntegrityError, ) as e:
            print("Exception: ", repr(e))
            return "<!Doctype html><html lang='en'><head><title>Cookzone</title></head><body></body><h1>Database connection error</h1></html>"
        finally:
            cursor.close()
            connection.close()
        return redirect(url_for('login'))
    else:
        return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email= request.form['email']
        pwd = request.form['pwd']

        try:
            connection = connect(r"./databases/database.db")
            cursor = connection.cursor()
            cursor.execute("""SELECT Name, Email, pwdhash FROM customer;""")
            users_list = cursor.fetchall()
        except (IntegrityError, ) as e:
            print("Exception: ", repr(e))
            return "<!Doctype html><html lang='en'><head><title>Cookzone</title></head><body></body><h1>Database connection error</h1></html>"
        finally:
            cursor.close()
            connection.close()
        user = {}
        
        for i, n in enumerate(users_list):
            user[users_list[i][1].lower()] = users_list[i][2]

        # Check the password hash of the user in database
        if (email.lower() in user) and (user[email.lower()], pwd):
            return redirect(url_for('index'))
        else:
            return "<!Doctype html><html lang='en'><head><title>Cookzone</title></head><body></body><h1>wrong password</h1></html>"
    else:
        return render_template('login.html')


@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    checkout = []
    if request.method == 'POST':
        return redirect(url_for('billing'), code=307)
    else:
        return "<!Doctype html><html lang='en'><head><title>Cookzone</title></head><body></body><h1>Cart if empty !</h1></html>"

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/billing', methods=['GET', 'POST'])
def billing():

    if request.method == 'POST':

        temp = []
        checkout = []
        for item, value in request.form.items():
            checkout.append(item)
        try:
            connection = connect(r"./databases/database.db")
            cursor = connection.cursor()
            for index, item in enumerate(checkout):
                cursor.execute("""SELECT Price FROM menu where ItemType =?;""", (item,))
                temp.append((index, item, cursor.fetchall()[0][0]))
            return render_template('billing.html', checked_out = temp)
        except (IntegrityError, ) as e:
            print("Exception: ", repr(e))
            return "<!Doctype html><html lang='en'><head><title>Cookzone</title></head><body></body><h1>Database error</h1></html>"
        finally:
            cursor.close()
            connection.close() 
    else:
        return "<!Doctype html><html lang='en'><head><title>Cookzone</title></head><body></body><h1>Billing Page error</h1></html>"

if __name__ == "__main__":
    app.run(debug=True)