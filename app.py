from flask import Flask, render_template
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

# @app.route('/users')
# def users():
#     return render_template('users.html', user=user)

@app.route('/login')
def logins(methods=['GET', 'POST']):
    return render_template('login.html')

@app.route('/menu')
def menu():
    return render_template('menu.html', items=menu_items[0:5])

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')


if __name__ == "__main__":
    app.run(debug=True)
