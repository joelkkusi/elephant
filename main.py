import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()

while True:
    print("Welcome to the Guessing Game!")

    topic = input("Enter the topic of the word: ").lower()
    word = input("Enter the " + topic + " to guess: ").lower()

    while True:
        guess_validation = input("Enter the number of guesses: ").strip()
        if guess_validation.isdigit() and int(guess_validation) > 0:
            guesses = int(guess_validation)
            break
        print("Please enter a number.")

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
            print("You have " + str(guesses) + " guesses left to guess the " + topic + ".")
    else:
        clear()
        print("Sorry, you ran out of guesses.\n"
              "The " + topic + " was: " + word + "\n")

