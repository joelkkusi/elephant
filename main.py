word = "apple"
guesses = 5

print("Guessing Game")
print("Topic: Fruit")
print("You'll start of with " + str(guesses) + " chances to guess the word.")

for attempt in range(guesses):
    guess = input("Guess the word: ")

    if guess == word:
        print("Congratulations! You guessed the word!")
        break
    else:
        guesses -= 1
        print("You have " + str(guesses) + " guesses left.")
else:
    print("Sorry, you ran out of guesses. The word was " + word)
