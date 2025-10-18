import random
print('''
 _____ _   _ _____ _____ _____   _____ _   _  _____   _   _ _   ____  _________ ___________ 
|  __ \ | | |  ___/  ___/  ___| |_   _| | | ||  ___| | \ | | | | |  \/  || ___ \  ___| ___ \
| |  \/ | | | |__ \ `--.\ `--.    | | | |_| || |__   |  \| | | | | .  . || |_/ / |__ | |_/ /
| | __| | | |  __| `--. \`--. \   | | |  _  ||  __|  | . ` | | | | |\/| || ___ \  __||    / 
| |_\ \ |_| | |___/\__/ /\__/ /   | | | | | || |___  | |\  | |_| | |  | || |_/ / |___| |\ \ 
 \____/\___/\____/\____/\____/    \_/ \_| |_/\____/  \_| \_/\___/\_|  |_/\____/\____/\_| \_|
                                                                                            
''')

print("Welcome to the number guessing game!!!")
print("I AM THINKING OF A NUMBER BETWEEN 1 AND 100. \n CAN YOU GUESS IT?")

attempts_no = input("Choose your level 'easy' or 'hard' ? : ")

if attempts_no == "easy":
    attempts = 10
else:
    attempts = 5

print(f"You have {attempts} attempts")

number = random.randint(1, 100) 


while attempts > 0 :
    user_guess = int(input("Guess a number:"))

    if user_guess == number:
        print(f"THAT'S CORRECT THE NUMBER IS {number}")
        break
    else:
        attempts -= 1
        if user_guess < number: 
            print("TOO LOW")
        elif user_guess > number:
            print("TOO HIGH")
        print(f"You only have {attempts} left")

    if attempts == 0 :
        print(f"You lost all the attempts. The number was {number}\nClick refresh to start a new game")  




    
    