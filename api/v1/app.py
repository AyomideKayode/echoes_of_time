#!/usr/bin/python3
""" Flask Application """
from flask import Flask, abort, make_response, jsonify, render_template, request, redirect, url_for
from models import storage
from api.v1.views import app_views
from flask_cors import CORS
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.route('/')
def index():
    return render_template('index.html', title="Home")


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    """Signs up a user.
    This function handles the sign-up process for a user.
    It retrieves the username, email, and password from the request form,
    generates a hashed password, creates a new user object,
    saves it to the database, and redirects the user to the login page.

    Returns:
        A redirect response to the login page.
    """
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        hashed_password = generate_password_hash(password)
        user = User(username=username, email=email, password=hashed_password)
        user.save()
        return redirect(url_for('login'))
    return render_template('sign_up.html', title="Sign Up")


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handles the login functionality.
    This function is responsible for handling the login process.
    It checks if the request method is POST,
    retrieves the username and password from the request form,
    and verifies the credentials against the stored user data.
    If the credentials are valid, it redirects the user to the
    dashboard page. Otherwise, it redirects the user back to the login page.

    Returns:
        If the request method is POST and the credentials are valid,
        it redirects the user to the dashboard page.
        Otherwise, it redirects the user back to the login page.
    """
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = storage.get(User, username)
        # Assuming you're using a session or token for login
        # I still think we might change this when you
        # implement the firebase auth
        if user and check_password_hash(user.password, password):
            return redirect(url_for('dashboard', user_id=user.id))
        else:
            return redirect(url_for('login'))
    return render_template('login.html', title="Login")


@app.route('/dashboard/<user_id>')
def dashboard(user_id):
    """ Dashboard Route
    """
    user = storage.get(User, user_id)
    if not user:
        return not_found
    return render_template('dashboard.html', user=user, title="Dashboard")


@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
        404: description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port='5000', threaded=True)
