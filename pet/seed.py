import json
from model import db, DogMovie, connect_to_db

def load_data_from_json(filename):
    with open(filename) as file:
        data = json.load(file)
    return data

def seed_dog_movies(data):
    for movie_data in data:
        movie = DogMovie(
            title=movie_data['title'],
            movie_rating=movie_data['movie_rating'],
            comments=movie_data['comments'],
        )
        db.session.add(movie)

    db.session.commit()

if __name__ == '__main__':
    from app import app
    connect_to_db(app)
    
    # Specify the path to your JSON data file
    json_data = load_data_from_json('data/dog_movies.json')
    
    # Seed the DogMovie table with data from the JSON file
    seed_dog_movies(json_data)
