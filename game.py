*Rock, Paper, Scissors Game*
```
import random

def game():
    while True:
        user = input("Enter your choice (rock/paper/scissors): ").lower()
        choices = ["rock", "paper", "scissors"]
        computer = random.choice(choices)

        print(f"\nUser chose {user}, computer chose {computer}.\n")

        if user == computer:
            print(f"Both players selected {user}. It's a tie!")
        elif user == "rock":
            if computer == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif user == "paper":
            if computer == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif user == "scissors":
            if computer == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    game()
```

*Number Guessing Game*
```
import random

def game():
    number_to_guess = random.randint(1, 10)
    guess = None
    attempts = 0

    while guess != number_to_guess:
        guess = int(input("Guess a number between 1 and 10: "))
        attempts += 1
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")

    print(f"Congratulations! You found the number in {attempts} attempts.")

if __name__ == "__main__":
    game()
```

*Mad Libs Game*
```
print("Welcome to Mad Libs Game!")

name = input("Enter a name: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
adjective3 = input("Enter one more adjective: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
animal = input("Enter an animal: ")
food = input("Enter a food: ")

story = f"Once upon a time, {name} was a {adjective1} person. " \
        f"They had a {adjective2} {noun1} and a {adjective3} {noun2}. " \
        f"One day, they saw a {animal} eating {food}."

print(story)
```

Choose one!
