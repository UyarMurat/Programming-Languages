#Rock, Paper, Scissors game

import random

#Asci Art was copied

paper = '''     
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)'''

rock = '''    
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Lisst
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors. "))

if user_choice >= 0 and user_choice <=2:
    print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer choice:")
print(game_images[computer_choice])

print(f"Computer choose {computer_choice}")
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!")
elif computer_choice == user_choice:
    print("It's a draw!")
