import random

print(r"""
  ________                                __  .__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ _/  |_|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \   |  | |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >  |__| |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/             \/     \/          \/            \/    \/     \/       """)
print("Welcome to the Number Guessing Game!!")
print("Im thinking of a number between 1 and 100.")
diff=input("Choose a difficulty. Type 'easy' or 'hard': ")

number = random.randint(1,100)
attempts=0
guess=0

if diff=="hard":
    attempts=5
elif diff=="easy":
    attempts=10

print(f"You have {attempts} attempts remaining to guess the number.")
guess=int(input("Make a guess: "))

def guess_again():
    global guess
    print("Guess again.")
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess=int(input("Make a guess: "))

win=False

while attempts>0:
    if guess>number:
        attempts-=1
        print("Too high")
        if attempts>0:
            guess_again()
    elif guess<number:
        attempts-=1
        print("Too low")
        if attempts>0:
            guess_again()
    elif guess==number:
        win=True
        print(f"You got it! The answer was {number}.")
        break

if win==False:
    print("You've run out of guesses. Refresh the page to try again!")
