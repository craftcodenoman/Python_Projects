import random

def choose_word():
    words = ["python", "programming", "hangman", "developer", "computer", "challenge"]
    return random.choice(words) 

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    print("Welcome to the Hangman Game! ")
    
    word = choose_word()
    guessed_letters = set()
    attempts = 6 

    while attempts > 0:
        print("Word:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print(" Invalid input! Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(" You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            attempts -= 1
            print(f" Incorrect! You have {attempts} attempts left.")
        else:
            print("Correct guess!")

        if all(letter in guessed_letters for letter in word):
            print(f" Congratulations! You guessed the word: {word} ")
            break
    else:
        print(f"Game Over! The word was: {word}")


hangman()
