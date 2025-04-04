# Treasure Island Game

print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
way = input('Your on a cross road where do you want to go?\n Type "left" or "right" ').lower()
if way == "left":
    print("You've came to lake and there is an island in the middle of the lake")
    boat = input('Type "wait" to wait for a boat. type "swim" to cross ').lower()
    if boat == "wait":
        print("You have arrived at the island of unharmed there is a house with three doors")
        doors = input("One red, yellow , blue which colour do you choose? ").lower()
        if doors == "yellow":
            print("You've won the treasure!!")
        elif doors == "red" and doors == "blue":
            print("You've lost the game")
        else:
            print("You've entered wrong inputs")
    else:
        print("Game over")
elif way == "right":
    print("Game Over because you fell into a hole ")
else:
    print("You've entered wrong inputs")

