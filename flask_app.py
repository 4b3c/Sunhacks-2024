from flask import Flask, redirect, url_for, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['nm']  # Get the input from the form
        return redirect(url_for('success', name=user))
    return render_template('test.html')  # Show the HTML form

# Success page that takes the user's name
@app.route('/success/<name>')
def success(name):
    return f'Welcome {name}!'

if __name__ == '__main__':
    app.run(debug=True)

