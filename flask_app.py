import json
from flask import Flask, redirect, url_for, jsonify, request, render_template
from flask_cors import CORS
import classes
app = Flask(__name__)
CORS(app)

user = None

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['nm']  # Get the input from the form
        password = request.form['pw']
        try: #Check if user already exists
            with open('user_data.json', 'r') as file:
                user_data = json.load(file)
                user = user_data["user_obj"]
                print(user)

        except FileNotFoundError: # Create a new user
            user_data = {
                "username": user,
                "passphrase": password,
                "user_obj": classes.User(f_name=user,l_name=user,password=password).__dict__
            }
            with open('user_data.json', 'w') as json_file:
                json.dump(user_data, json_file)

        return redirect(url_for('addTask'))
    return render_template('login.html') 

@app.route('/taskboard', methods=['GET', 'POST'])
def addTask():
    if request.method == 'POST':
        name = request.form.get('name')
        dropdown1 = request.form.get('Main Category')
        dropdown2 = request.form.get('Subcategory')
        dropdown3 = request.form.get('Rating')
        datetime = request.form.get('datetime')  # From 'datetimeField' ID

        # Process the data (for now, just print it)
        print(f"Name: {name}")
        print(f"Dropdown 1: {dropdown1}")
        print(f"Dropdown 2: {dropdown2}")
        print(f"Dropdown 3: {dropdown3}")
        print(f"Date and Time: {datetime}")

        return redirect(url_for('success'))
    return render_template('addTask.html') 

# Success page that takes the user's name
@app.route('/success/')
def success():
    return f'Welcome!'

if __name__ == '__main__':
    app.run(debug=True)

