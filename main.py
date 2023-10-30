import random
from art import logo


def game(difficulty):
  random_number = random.randint(1, 100)
  if difficulty == "easy":
    guesses = 10
    print("You have 10 guesses to guess the number between 1 and 100")
  elif difficulty == "hard":
    guesses = 5
    print("You have 5 guesses to guess the number between 1 and 100")
  else:
    print("Invalid difficulty level")
    return
  for _ in range(guesses):
    guess = int(input("Guess a number: "))
    guesses -= 1
    if guess == random_number:
      print("You guessed the number!")
      return
    elif guess < random_number:
      print("Too low")
    else:
      print("Too high")
    print(f"you have {guesses} attempts remaining to guess the number")
    if guesses == 0 and guess != random_number:
      print(f"Game over. YOU LOSE. The number was {random_number}")


print(logo)
print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
game(difficulty)
