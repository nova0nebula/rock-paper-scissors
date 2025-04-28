#!/usr/bin/env python3

# Python Importing
import random

# Variables
choices: list = ["rock", "paper", "scissors"]

# Main Loop
while True:
    user: str = input("Rock, Paper, or Scissors? (or 'quit' to exit): ").lower()
    if user == "quit":
        print("Thanks for playing! 👋")
        break
    if user not in choices:
        print("Invalid choice. Try again.")
        continue

    computer: str = random.choice(choices)
    print(f"Computer chose {computer}.")

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win! 🎉")
    else:
        print("You lose. 😢")
