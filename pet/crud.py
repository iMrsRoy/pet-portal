from model import db, User

def create_user(petname, email, password):
    new_user = User(petname=petname, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

def get_users():
    return User.query.all()

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def get_user_by_id(id):
    return User.query.get(id)

def create_rating(user, movie_rating, score):
    """Create and return a new rating."""

    rating = movie_rating(user=user, movie_rating=movie_rating, score=score)

    return rating

def update_user_password(user, new_password):
    user.password = new_password
    db.session.commit()

def delete_user(user):
    db.session.delete(user)
    db.session.commit()


