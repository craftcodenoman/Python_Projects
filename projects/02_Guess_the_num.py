import random

def guess_the_number():
    print(" Welcome to the Guess the Number Game! ")
    print("I have selected a number between 1 and 10. Can you guess it? ")

    
    select_number = random.randint(1, 10)
    attempts = 0  
    while True:
        try:
            guess = int(input("Enter your guess: "))  
            attempts += 1  
            if guess < select_number:
                print("Too low! Try again ")
            elif guess > select_number:
                print("Too high! Try again ")
            else:
                print(f"Congratulations! You guessed the number {select_number} in {attempts} attempts.")
                break  
        except ValueError:
            print("Invalid input! Please enter a valid number.")

guess_the_number()
