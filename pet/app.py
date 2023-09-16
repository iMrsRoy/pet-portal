import os
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
            return render_template(url_for('dog_parks.html)'))  
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
        print("HELLOOOOO")
        return redirect(url_for('dog_parks'))
    # Fetch the user's pet name from the database
    petname = db.current_user.petname
    return render_template('dog_parks.html', petname=petname, google_maps_api_key=google_maps_api_key)





if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True)
