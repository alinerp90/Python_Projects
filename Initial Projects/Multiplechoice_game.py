""" 
Build a game with multiple choices option, which the player should choose the correct answer to win the game.
"""

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

question_1 = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"  ').lower()


if question_1 == "left":
    question_2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.  ').lower()

    if question_2 == "wait":
        question_3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?  ").lower()

        if question_3 == "red":
            print("Burned by fire. Game Over.")

        elif question_3 == "blue":
            print("Eaten by beasts. Game Over.")

        elif question_3 == "yellow":
            print("You found the treasure! You Win!")

        else:
            print("You chose a door that doesn\'t exist. Game Over.")

    elif question_2 == "swim":
        print("Attacked by a trout. Game over.")

    else:
        print("You are dumb? You put an invalid answer. Game over")

elif question_1 == "right":
    print("Fall into a hole. Game over.")

else:
    print("You are dumb? You put an invalid answer. Game over")