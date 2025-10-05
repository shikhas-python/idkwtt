print("welcome to treasure island!! \nYour mission is to find the treasure??? \nLet's start>>")

print("you're at a cross road. Where do you wanna go? Left or Right?\n")
Q1 = input("type L or R\n")

if Q1 == "L":
    print("you reached a lake, you'll have to find the castle now!\n")
    Q2 = input("Do you want to swim or wait?\n")
    if Q2 == "wait":
        print("great patience is the key!\nA boat picked you up and dropped you at the castle's door!\nThere are three gates: Red, Yellow, Blue\n")
        Q3 = input("which gate would you go into?")
        if Q3 == "Red":
            print("OH LORD!! You're burned by a fire....\n GAME OVER")
        elif Q3 == "Blue":
            print("AAAAAAAHHHHHHHHH.... You got eaten by beasts!!\n GAME OVER")
        elif Q3 == "Yellow":
            print("YOU FOUND THE TREAURE...... HAVE A GREAT DAYYYY!!")
        else:
            print("GAME OVER")
    else :
        print("You are attacked by trout!\nGAME OVER")
else :
    print("HEHEHEHE!!!! YOOOOUUUU fell into a HOLEEEE!!!\nBetter luck next time")



        






