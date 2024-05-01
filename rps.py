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

import random

choice = [rock,paper,scissors]   

count = 1
score_player = 0
score_computer = 0  
while(count <= 5):
    player = int(input("\nWhat do you choose? \n    Enter:\n        -> 0 for rock\n        -> 1 for paper\n        -> 2 for scissors\n\n\n"))
    
    if player >= 3 or player < 0:
        print("You Chose An Invalid Number!")
        print("Game Over!")
        exit(0)
    else:
        print(choice[player])
        computer = random.randint(0,2)
        print(f"Computer chose:")
        print(choice[computer])
      

    if player == computer:
        print("It is a draw!")
        count += 1
        print(f"Player score : {score_player}")
        print(f"Computer score : {score_computer}\n")
    elif player == 0 and computer == 2:
        print("You WIN!")
        score_player += 1
        count += 1
        print(f"Player score : {score_player}")
        print(f"Computer score : {score_computer}\n")
    elif player == 2 and computer == 0:
        print("you lose")
        score_computer += 1
        count += 1
        print(f"Player score : {score_player}")
        print(f"Computer score : {score_computer}\n")
    elif player > computer:
        print("You WIN!")
        score_player += 1
        count += 1
        print(f"Player score : {score_player}")
        print(f"Computer score : {score_computer}\n")
    elif computer > player:
        print("You lose")
        score_computer += 1
        count += 1
        print(f"Player score : {score_player}")
        print(f"Computer score : {score_computer}\n")
    



if score_player == score_computer:
    print("\n\nIt's a DRAW!\n\n")
elif score_player > score_computer:
    print("\n\nYOU WON!\n\n")
else:
    print("\n\nyou lost\n\n")     
   





