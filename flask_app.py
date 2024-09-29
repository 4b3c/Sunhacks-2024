import pickle
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
        name = request.form['nm']  # Get the input from the form
        password = request.form['pw']
        try: #Check if user already exists
            with open(f'{name}.pkl', 'rb') as file:
                user = pickle.load(file)
                print(f"user already exists: {user}")

        except FileNotFoundError: # Create a new user
            
            user = classes.User(f_name=name,l_name=name,password=password)
            print(f"user doesnt exist, creating: {user}")

            with open(f'{name}.pkl', 'wb') as pickle_file:
                pickle.dump(user, pickle_file)

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

        #---Debugging----
        # print(f"Label: {label}")
        # print(f"Dropdown 1: {category}")
        # print(f"Dropdown 2: {subcategory}")
        # print(f"Dropdown 3: {rating}")
        # print(f"Date and Time: {type(datetime)}")

        added = user.add_task(label, category, subcategory, rating )
        print(f"Task was added?: {added}")
        print(user.get_subcategory_scores())

        return redirect(url_for('addTask'))
    
    user_stats = user.get_piechart()
    lbls = list(user_stats.keys())
    stat = list(user_stats.values())
    return render_template('addTask.html', label_list=lbls, data_list=stat, todo_list={}) 

# Success page that takes the user's name
@app.route('/success/')
def success():
    return f'Welcome!'

if __name__ == '__main__':
    app.run(debug=True)

