import random 
user_chose = input("what do you choose? rock/paper/scissors? \n")

generate = ["rock", "paper", "scissors"]

option = print(random.choice(generate))

if option == "paper":
    print( "compter chose" +
    '''  ___
---     ____)___
          ______)
          _______)
         _______)
---.__________)
''')
    if user_chose == "rock":
        print("you lose!")
    elif user_chose == "paper":
        print("Tie!")
    elif user_chose == "scissors":
        print("you Win!")
elif option == "scissors":
    print("computer chose" +'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''')
    if user_chose == "rock":
        print("you Win!")
    elif user_chose == "paper":
        print("you Lose!")
    elif user_chose == "scissors":
        print("Tie")
else:
    print("computer chose" + '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')
    if user_chose == "rock":
        print("Tie")
    elif user_chose == "paper":
        print("you Win")
    elif user_chose == "scissors":
        print("you Lose")
    



