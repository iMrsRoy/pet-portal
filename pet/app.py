from flask import Flask, render_template, request, redirect, url_for, session
import os, crud, random, json, requests
# from flask_sqlalchemy import SQLAlchemy
from model import db, User, connect_to_db



app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']


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
    google_maps_api_key = os.environ.get('GOOGLEMAPS_KEY')
    
    zipCode = os.environ.get('zipCode')
    w_api = os.environ.get('WAPI_KEY')
    
    def getWeatherByZipCode(zipCode):
        url = f"https://api.openweathermap.org/data/2.5/weather?zip={zipCode}&appid={w_api}&units=imperial"
        response = requests.get(url)
    
        if response.status_code == 200:
            jsonWeatherData = json.loads(response.content)
            return {
            "City": jsonWeatherData["name"],
            "Current Temperature": jsonWeatherData["main"]["temp"],
            "Feels Like Temperature": jsonWeatherData["main"]["feels_like"],
            "Humidity": jsonWeatherData["main"]["humidity"],
            "Sunrise": jsonWeatherData['sys']['sunrise'],
            "Sunset": jsonWeatherData['sys']['sunset'],
            "Description": " ".join([weatherCondition["description"] for weatherCondition in jsonWeatherData["weather"]]),
        }
        else:
            return None 
        if request.method == 'POST':
            return redirect(url_for('dog_parks'))
    user_id = session.get('user_id')
    if user_id:
        user = crud.get_user_by_id(user_id)
        petname = user.petname   
        # weather = None
        zip_code = request.form.get('zipCode')
        weather = getWeatherByZipCode(zip_code)
        return render_template('dog_parks.html', petname=petname, google_maps_api_key=google_maps_api_key, weather=weather)
    else:
        return redirect(url_for('register'))


# @app.route('/dog_parks', methods=['POST', 'GET'])
# def dog_parks():
#     if request.method == 'POST':
#         #print("HELLOOOOO")
#         return redirect(url_for('dog_parks'))
#     # Fetch the user's by using session
#     user_id = session.get('user_id')
#     if user_id:
#         user = crud.get_user_by_id(user_id)
#         petname = user.petname
#         print(google_maps_api_key)
#         return render_template('dog_parks.html', petname=petname, google_maps_api_key=google_maps_api_key)
#     else:
#         return redirect(url_for('register'))
    

@app.route('/dog_movies', methods=['POST', 'GET'])
def dog_movies():
        if request.method == 'POST':
            return redirect(url_for('dog_games'))
        
        user_id = session.get('user_id')
        if user_id:
            user = crud.get_user_by_id(user_id)
            petname = user.petname
            return render_template('dog_movies.html', petname=petname)
    



# Define the choices outside of the route function
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

# Define the determine_winner function outside of the route function
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

@app.route('/dog_games', methods=['GET', 'POST'])
def dog_games():
    user_id = session.get('user_id')
    petname = "Your Pet's Name"  # Default petname
    if user_id:
        user = crud.get_user_by_id(user_id)
        petname = user.petname

    # Initialize game_result
    game_result = None

    if request.method == 'POST':
        # Handle the game logic here based on user's choice
        user_choice_name = request.form.get('user_choice')
        user_choice = next((c for c in choices if c["name"] == user_choice_name), None)
        
        if user_choice is not None:
            computer_choice = generate_computer_choice()
            game_result = determine_winner(user_choice, computer_choice)
        else:
            game_result = "Will I get treat this time? "

    # Pass the choices list and game_result to the template context
    return render_template('dog_games.html', game_result=game_result, choices=choices, petname=petname)

# Define the generate_computer_choice function outside of the route function
def generate_computer_choice():
    return random.choice(choices)




# For add more routes and logic to support my code goes
@app.route('/load_movies', methods=['GET'])
def load_movies():
    with open('dog_movies.json', 'r') as json_file:
        data = json.load(json_file)

    for item in data:
        movie = db.DogMovie(
            title=item['title'],
            movie_rating=item['movie_rating'],
            comments=item['comments']
        )
        db.session.add(movie)

    db.session.commit()

    return "Movies loaded successfully!"
def dog_movies():
    movies = DogMovie.query.all()
    return render_template('movie.html', petname="Your Pet's Name", movies=movies)

if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True)
