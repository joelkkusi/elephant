import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()

print("Welcome to the Guessing Game!")

topic = input("Enter the topic of the word: ").lower()
word = input("Enter the " + topic + " to guess: ").lower()
guesses = int(input("Enter the number of guesses: "))

clear()

print("Guessing Game")
print("Topic of the word: " + topic)
print("You'll start of with " + str(guesses) + " chances to guess the " + topic + ".")

for attempt in range(guesses):
    guess = input("Guess the " + topic + ": ").lower()

    if guess == word:
        print("Congratulations! You guessed the " + topic + " correctly!")
        break
    else:
        clear()
        guesses -= 1
        print("You have " + str(guesses) + " guesses left.")
else:
    clear()
    print("Sorry, you ran out of guesses.\n"
          "The " + topic + " was: " + word)
