from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

class User(db.Model):
    
    """A user."""
    __tablename__ = "users"
    
    id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    petname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    
    def __repr__(self):
        return f"<User user_id={self.id} email={self.email}>"

class Review(db.Model):
    """Review Table"""
    __tablename__ = "review"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    dog_park_id = db.Column(db.Integer, db.ForeignKey('dog_parks.id'), nullable=False)
    park_rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)

class DogPark(db.Model):
    """DogPark Table"""
    __tablename__ = "dog_parks"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

class DogMovie(db.Model):
    """DogMovie Table"""
    __tablename__ = "DogMovie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    movie_rating = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.Text)
    dog_park_id = db.Column(db.Integer, db.ForeignKey('dog_parks.id'), nullable=False)
  

def connect_to_db(flask_app, db_uri="postgresql:///dogs", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

# db comment
if __name__ == "__main__":
    from app import app
    with app.app_context():
        db.init_app(app)
        connect_to_db(app) # its need to be here to be connected to the database
        # db.drop_all()
        # db.create_all()
        
        # user = User(petname="Fido", email="bob@bobbies.com", password="poop")
        # db.session.add(user)
        # db.session.commit()
        # users = User.query.all()
        # print(users)