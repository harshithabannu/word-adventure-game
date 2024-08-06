def text_adventure_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest.")
    print("You see a path to the left and a path to the right.")

    choice1 = input("Do you go left or right? ").lower()

    if choice1 == "left":
        print("You walked down the path and you found a tunnel and an underground passage.")
        choice2 = input("Do you go into the tunnel or underground? ").lower()
        if choice2 == "tunnel":
            print("You walk down the path and find a treasure chest!")
            print("Congratulations, you found the treasure!")
        elif choice2 == "underground":
            print("the path was ended")
            
        else:
            print("Invalid choice. Please choose tunnel or underground.")
    elif choice1 == "right":
        print("You are caught by a wild animal and your adventure ends!")
    else:
        print("Invalid choice. Please choose left or right.")

text_adventure_game()

