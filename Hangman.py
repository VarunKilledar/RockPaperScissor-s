import random

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["Varun","TheWholeMan","Ragnarok","thor","loki"]
Chosen_word = random.choice(word_list).lower()
print(Chosen_word)
blanks = []
for n in range(len(Chosen_word)):
    blanks.append("_")
lives = 6
end_game = False
while end_game == False:
    guess = input("enter the letter that you guess:").lower()
#Checking the user letter 
    for position in range(len(Chosen_word)):
        letter = Chosen_word[position]
        if letter == guess:
            blanks[position] = guess
            print(blanks)
    if guess not in Chosen_word:
        lives -= 1
        print(f"The remainig lives left with you:{lives}")
        if lives == 0:
            end_game = True
            print("You Losse ",'''
            
    |_______________``\ 
    [/]           [  ]
    [\]           | ||
    [/]           |  |
    [\]           |  |
    [/]           || |
   [---]          |  |
   [---]          |@ |
   [---]          |  |
  oOOOOOo         |  |
 oOO___OOo        | @|
oO/|||||\Oo       |  |
OO/|||||\OOo      |  |
*O\ x x /OO*      |  |
/*|  c  |O*\      |  |
   \_O_/    \     |  |
    \#/     |     |  |
 |       |  |     | ||
 |       |  |_____| ||__
_/_______\__|  \  ||||  \ 
/         \_|\  _ | ||\  \ 
|    V    |\  \//\  \  \  \ 
|    |    | __//  \  \  \  \ 
|    |    |\|//|\  \  \  \  \ 
------------\--- \  \  \  \  \ 
\  \  \  \  \  \  \  \  \  \  \ 
_\__\__\__\__\__\__\__\__\__\__\ 
__|__|__|__|__|__|__|__|__|__|__|
|___| |___|
|###/ \###|
\##/   \##/
 ``     ``  
 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
 
 ''')
    print(stages[lives])
        # break
    if "_" not in blanks:
        end_game = True
        print("You Won")





        



