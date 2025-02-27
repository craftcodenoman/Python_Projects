import random

def computer_guess():
    print("🤖 Welcome to the Guess the Number Game! 🎯")
    print("Think of a number between 1 and 100, and I (computer) will try to guess it! 🤔")
    input("Press Enter when you're ready...")

    low = 1
    high = 100
    attempts = 0

    while True:
        guess = random.randint(low, high)  # کمپیوٹر کا اندازہ
        attempts += 1

        print(f"\nIs your number {guess}?")
        feedback = input("Type 'h' if too high, 'l' if too low, or 'c' if correct: ").lower()

        if feedback == 'h':
            high = guess - 1  # اگر اندازہ زیادہ ہے، حد کو کم کر دیں
        elif feedback == 'l':
            low = guess + 1  # اگر اندازہ کم ہے، حد کو بڑھا دیں
        elif feedback == 'c':
            print(f"🎉 Yay! I guessed your number {guess} in {attempts} attempts. 🏆")
            break
        else:
            print("❌ Invalid input! Please enter 'h', 'l', or 'c'.")

# گیم شروع کرنے کے لیے فنکشن کال کریں
computer_guess()
