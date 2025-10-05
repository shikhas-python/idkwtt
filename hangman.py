import random

hangman = [''' 
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
    _|___
 ''', 
 '''   _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |       
     |
    _|___
''', 
'''   _______
     |/      |
     |      (_)
     |      \|/
     |       
     |       
     |
    _|___
''',
 '''   _______
     |/      |
     |      (_)
     |      \|
     |       
     |       
     |
    _|___
''', 
'''   _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
    _|___
''',
'''   _______
     |/      |
     |      
     |      
     |       
     |      
     |
    _|___
''',
'''   
     |/      
     |      
     |      
     |       
     |      
     |
    _|___
''']


lives = 6

word = ["ant", "babboon", "badger", "bat", "bear",  "beaver", "camel", "cat", "clam", "cobra", "cougar", "coyote", "crow", "deer", "dog", "donkey", "duck", "eagle", "ferret", "fox", "frog", "goat", "goose", "hawk", "lion", "lizard", "llama", "mole", "rat", "raven", "rhino", "shark", "sheep", "spider", "toad", "turkey", "turtle", "wolf", "wombat", "zebra"]

random_word = (random.choice(word))

word_length = len(random_word)

placeholder = ""
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False

correct_letter = []

while not game_over:
     choose = input("choose a letter\n").lower()
     
     display = ""

     for letter in random_word:
         if letter == choose:
             display += letter
             correct_letter.append(choose)
         elif letter in correct_letter:
             display+= letter
         
             if lives == 0:
                 print("you lose")
             
         else:
             display += "_"

     print(display)
    
     if choose not in random_word:
         lives -= 1
         if lives == 0:
             game_over = True
             print("you lose!")
             
     
     if "_" not in display:
         game_over = True
         print("you win!")

     print(hangman[lives])


