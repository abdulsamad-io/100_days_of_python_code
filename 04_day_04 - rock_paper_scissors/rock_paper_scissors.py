import random

print ('''
__________               __     __________                                      _________      .__                                  
\______   \ ____   ____ |  | __ \______   \_____  ___________    ___________   /   _____/ ____ |__| ______ _________________  ______
 |       _//  _ \_/ ___\|  |/ /  |     ___/\__  \ \____ \__  \ _/ __ \_  __ \  \_____  \_/ ___\|  |/  ___//  ___/  _ \_  __ \/  ___/
 |    |   (  <_> )  \___|    <   |    |     / __ \|  |_> > __ \\  ___/|  | \/  /        \  \___|  |\___ \ \___ (  <_> )  | \/\___ \ 
 |____|_  /\____/ \___  >__|_ \  |____|    (____  /   __(____  /\___  >__|    /_______  /\___  >__/____  >____  >____/|__|  /____  >
        \/            \/     \/                 \/|__|       \/     \/                \/     \/        \/     \/                 \/ 
''')

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

print ("Welcome to ROCK - PAPER - SCISSORS game\n\n")
cpu_choice = random.randint(1,3)

user_choice = input("Select one by typing : ROCK, PAPER or SCISSORS: ").lower()
if user_choice == "rock":
    user_choice = rock
elif user_choice == "paper":
    user_choice = paper
elif user_choice == "scissors":
    user_choice = scissors
else:
    print("Select the right choice !!!. Game Over !!!")

if cpu_choice == 1:
    cpu_choice = rock
elif cpu_choice == 2:
    cpu_choice = paper
else:
    cpu_choice = scissors

print (f"COMPUTER is {cpu_choice} \n PLAYER is {user_choice} ")

if user_choice == cpu_choice:
    print ('''            
   __| |_ __ __ ___      __
  / _` | '__/ _` \ \ /\ / /
 | (_| | | | (_| |\ V  V /
  \__,_|_|  \__,_| \_/\_/
    ''')

elif (
     (user_choice == rock and cpu_choice ==scissors) or
     (user_choice == paper and cpu_choice == rock) or
     (user_choice == scissors and cpu_choice == paper)):
    print ('''                        
                              (_)      
  _   _  ___  _   _  __      ___ _ __  
 | | | |/ _ \| | | | \ \ /\ / / | '_ \ 
 | |_| | (_) | |_| |  \ V  V /| | | | |
  \__, |\___/ \__,_|   \_/\_/ |_|_| |_|
   __/ |                               
  |___/                                ''')

else:
    print ('''     
                             (_)      
   ___ _ __  _   _  __      ___ _ __  
  / __| '_ \| | | | \ \ /\ / / | '_ \ 
 | (__| |_) | |_| |  \ V  V /| | | | |
  \___| .__/ \__,_|   \_/\_/ |_|_| |_|
      | |                             
      |_|                             
    ''')

print ('play another game!!!')

