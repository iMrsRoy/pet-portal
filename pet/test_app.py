# test_app.py
from pytest import *
from app import determine_winner


def test_determine_winner():
    # Test a scenario where the user wins
    user_choice = {"name": "Tug-War"}
    computer_choice = {"name": "Feed-Treats"}
    result = determine_winner(user_choice, computer_choice)
    assert result == "You win!"

    # Test a scenario where it's a tie
    user_choice = {"name": "Tug-War"}
    computer_choice = {"name": "Tug-War"}
    result = determine_winner(user_choice, computer_choice)
    assert result == "It's a tie!"

    # Test a scenario where the computer wins
    user_choice = {"name": "Feed-Treats"}
    computer_choice = {"name": "Tug-War"}
    result = determine_winner(user_choice, computer_choice)
    assert result == "Computer wins!"

    # Add more test cases as needed

# Run the tests
