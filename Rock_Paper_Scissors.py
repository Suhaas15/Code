import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user = int(input("What do you choose?: Type 0 for Rock, 1 for Paper and 2 for Scissors."))
comp=random.randint(0,2)

if user==0:
    print(rock)
elif user==1:
    print(paper)
elif user==2:
    print(scissors)
else:
    print("Wrong input!")

if comp==0:
    print(rock)
elif comp==1:
    print(paper)
else:
    print(scissors)

if user==comp:
    print("Its a draw!")
elif user==0 and comp==2:
    print("You win!")
elif user==1 and comp==0:
    print("You win!")
elif user==2 and comp==1:
    print("You win!")
else:
    print("You lose!")