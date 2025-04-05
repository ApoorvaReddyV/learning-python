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
game_images = [rock, paper, scissors]
user = int(input("What do you choose? Type 0 for rock, 1 for paper , 2 for scissors.\n"))
print("you choose: ")
if user >= 0 and user <= 2:
    print(game_images[user])
computer = random.randint(0, 2)
print("Computer choose: ")
print(game_images[computer])
if computer == 0 and user == 1:
    print("You win!!")
elif computer == 1 and user == 0:
    print("computer wins!!")
elif computer == 1 and user == 2:
    print("You win!!")
elif computer == 2 and user == 1:
    print("Computer wins!!")
elif computer == 0 and user == 2:
    print("Computer wins!!")
elif computer == 2 and user == 0:
    print("You win!!")
elif computer == user:
    print("It's a draw")
elif user >= 3:
    print("You entered invalid inputs.You loose!!")

