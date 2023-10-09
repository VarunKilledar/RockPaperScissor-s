import random
Rock = '''        
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\ 
                      '''

Paper = '''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|      

 '''
Scissor = '''                            
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \ 
|___/\___|_|___/___/\___/|_|  |___/ '''

win = "You Win"
Loss = "You Loos"


print(f"Welcome to the Rock Paper and Scissors Game:0 :Rock,1:Paper,2:Scissor\n")
RPC = [Rock,Paper,Scissor]

Input = int(input())
print("Player's")
print(RPC[Input])
print(" ")

Computer_chice = random.randint(0,2)
print("Computer's")
print(RPC[Computer_chice])

if Input == 2  and Computer_chice == 1:
    print({win})
elif Input == 1 and Computer_chice == 0:
    print({win})
elif Input ==0 and Computer_chice == 2:
    print({win}) 
elif Computer_chice == 0 and Input == 2:
    print({Loss})
elif Computer_chice == 1 and Input == 0 :
    print({Loss})
elif Computer_chice == 2 and Input == 1:
    print({Loss})
else:
    print("Please Enter a write number")

