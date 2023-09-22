import os, crud, random
from flask import Flask, render_template, request, redirect, url_for, session
# from flask_sqlalchemy import SQLAlchemy
from model import db, User, connect_to_db, DogPark



app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']
google_maps_api_key = os.environ.get('GOOGLEMAPS_KEY')


@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Validate the login credentials (you should have this logic)
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            session['user_id'] = user.id  # Store user ID in the session
            return redirect(url_for('dog_parks'))  
        # # Redirect to the welcome route
        else:
        #     # Handle invalid credentials
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

    
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        petname = request.form['petname']
        email = request.form['email']
        password = request.form['password']
        new_user = User(petname=petname, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/dog_parks', methods=['POST', 'GET'])
def dog_parks():
    if request.method == 'POST':
        #print("HELLOOOOO")
        return redirect(url_for('dog_parks'))
    # Fetch the user's by using session
    user_id = session.get('user_id')
    if user_id:
        user = crud.get_user_by_id(user_id)
        petname = user.petname
        return render_template('dog_parks.html', petname=petname, google_maps_api_key=google_maps_api_key)
    else:
        return redirect(url_for('register'))
    

@app.route('/dog_movies', methods=['POST', 'GET'])
def dog_movies():
        if request.method == 'POST':
            return redirect(url_for('dog_games'))
        
        user_id = session.get('user_id')
        if user_id:
            user = crud.get_user_by_id(user_id)
            petname = user.petname
            return render_template('dog_movies.html', petname=petname)
    
# @app.route('/dog_games', methods=['POST', 'GET'])
# def dog_games():
#         if request.method == 'POST':
#             return redirect(url_for('dog_games'))
        
#         user_id = session.get('user_id')
#         if user_id:
#             user = crud.get_user_by_id(user_id)
#             petname = user.petname
#             return render_template('dog_games.html', petname=petname)
# Define the choices for the game
choices = [
    {
        "name": "Tug-War",
        "img": "https://www.everypaw.com/.imaging/mte/everypaw/590x330/dam/dog-breed-guides/cavapoo/cavapoo-2.jpg/jcr:content/cavapoo-2.jpg"
    },
    {
        "name": "Belly-Rubs",
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0Lep6KiEVa6HtATMbK96Ehz8QpGYhop7lMg&usqp=CAU"
    },
    {
        "name": "Feed-Treats",
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbf_t_GtIRvcqZnY87jYj7Zafe-ILfO05A-ODxyAP-OocD55w7qoGCg66aO3zCgTLahLM&usqp=CAU"
    }
]

# Function to generate the computer's choice
def generate_computer_choice():
    return random.choice(choices)

# Function to determine the game result
def determine_winner(user_choice, computer_choice):
    if user_choice["name"] == computer_choice["name"]:
        return "It's a tie!"
    elif (
        (user_choice["name"] == "Tug-War" and computer_choice["name"] == "Feed-Treats") or
        (user_choice["name"] == "Belly-Rubs" and computer_choice["name"] == "Tug-War") or
        (user_choice["name"] == "Feed-Treats" and computer_choice["name"] == "Belly-Rubs")
    ):
        return "You win!"
    else:
        return "Computer wins!"

from flask import render_template, request, session
import random

@app.route('/dog_games', methods=['GET', 'POST'])
def dog_games():
    if request.method == 'POST':
        # Handle the game logic here based on user's choice
        user_choice_name = request.form.get('user_choice')
        user_choice = next((c for c in choices if c["name"] == user_choice_name), None)
        computer_choice = generate_computer_choice()

        # Determine the game result based on user_choice and computer_choice
        game_result = determine_winner(user_choice, computer_choice)

        # Pass the choices list and game_result to the template context
        return render_template('dog_games.html', game_result=game_result, choices=choices)

    # Check if the user is logged in by looking for their user_id in the session
    user_id = session.get('user_id')
    if user_id:
        # If the user is logged in, retrieve their data (e.g., petname) from your data store
        user = crud.get_user_by_id(user_id)
        petname = user.petname
        return render_template('dog_games.html', choices=choices, petname=petname)

    # If the user is not logged in, you can handle this case as needed
    # For example, you can redirect them to the login page or show a message
    return render_template('login.html')  # You should replace 'login.html' with your actual login template




# For add more routes and logic to support my code goes



if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True)
