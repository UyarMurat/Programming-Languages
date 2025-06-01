
# Playing with loops & inputs




print("Welcome to Treasue Island.")
print("Your mission is to find the treasure")
choice_1 = input('You\'re at a crossroad, where do you want to go? '
                 'Type "left" or "right".').lower()

if choice_1 == "left":
    #Game goes on
    choice_2 = input('You\'ve come to a lake. There is an island in the middle of the lake. '
                     'Type "wait" to wait for a boat. '
                     'Type "swim" to swim accross.').lower()
    
    if choice_2 == "wait":
        #Game goes on
        choice_3 = input("You arrive at the island unharmed. There is a house with 3 doors. "
              "One red, one yellow and one blue. "
              "Which colour do you choose.").lower()
        
        if choice_3 == "yellow":
            print("You found the treasure. You win!")

        elif choice_3 == "blue":
            print("You enter a room full of beasts. Game Over.")

        elif choice_3 == "red":
            print("A Room full of fire. Game Over.")

        else:
            print("Game Over.")

    else:
        print('You got attacked by an angry trout. Game Over.')

else:
    print("You fell in to a hole. Game Over.")