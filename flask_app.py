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
    global user
    if request.method == 'POST':
        user = request.form['nm']  # Get the input from the form
        password = request.form['pw']
        try: #Check if user already exists
            with open('user_data.json', 'r') as file:
                user_data = json.load(file)
                user = classes.User(**user_data["user_obj"])

        except FileNotFoundError: # Create a new user
            user = classes.User(f_name=user,l_name=user,password=password)
            user_data = {
                "username": user,
                "passphrase": password,
                "user_obj": user.__dict__
            }
            with open('user_data.json', 'w') as json_file:
                json.dump(user_data, json_file)

        return redirect(url_for('addTask'))
    return render_template('login.html') 


@app.route('/taskboard', methods=['GET', 'POST'])
def addTask():
    global user
    if request.method == 'POST':
        label = request.form.get('name')
        category = request.form.get('Main Category')
        subcategory = request.form.get('Subcategory')
        rating = request.form.get('Rating')
        datetime = request.form.get('datetime')
        print(user)

        # print(f"Label: {label}")
        # print(f"Dropdown 1: {category}")
        # print(f"Dropdown 2: {subcategory}")
        # print(f"Dropdown 3: {rating}")
        # print(f"Date and Time: {type(datetime)}")

        user.add_task(label, category, subcategory, rating )

        return redirect(url_for('addTask'))
    return render_template('addTask.html') 

# Success page that takes the user's name
@app.route('/success/')
def success():
    return f'Welcome!'

if __name__ == '__main__':
    app.run(debug=True)

