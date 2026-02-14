import random
import time

characters = {
    "happy": "(≧◡≦) 🎉",
    "sad": "(╥﹏╥) 💔",
    "thinking": "(•_•) 🤔",
    "excited": "٩(◕‿◕)۶ ✨",
    "angry": "(ಠ_ಠ) 🔥"
}

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

number = random.randint(1, 100)
attempts = 0
max_attempts = 7

slow_print("🎮 Welcome to the Ultimate Number Guessing Game!")
slow_print(f"Computer says: I'm thinking of a number between 1 and 100 {characters['thinking']}")
slow_print(f"You only have {max_attempts} attempts... Good luck! {characters['excited']}\n")

while attempts < max_attempts:
    try:
        guess = int(input("👉 Enter your guess: "))
        attempts += 1
        
        if guess < number:
            slow_print(f"Too low! {characters['sad']} Try aiming higher!")
        elif guess > number:
            slow_print(f"Too high! {characters['angry']} Come down a bit!")
        else:
            slow_print(f"\nBOOM! You got it! {characters['happy']}")
            slow_print(f"It took you {attempts} attempts. You're a guessing master! 🏆")
            break
        
        slow_print(f"Attempts left: {max_attempts - attempts}\n")
    
    except ValueError:
        slow_print("⚠️ Please enter a valid number!")

if attempts == max_attempts and guess != number:
    slow_print(f"\nGame Over! The number was {number}. {characters['sad']}")
    slow_print("Better luck next time! 🍀")
