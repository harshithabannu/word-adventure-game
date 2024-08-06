import random

def text_adventure_game():
    health_points = 100
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest.")
    print("You see a path to the left, a path to the right, and a path straight ahead.")

    while True:
        choice1 = input("Do you go left, right, or straight? ").lower()

        if choice1 == "left":
            print("You walked down the path and you found a tunnel and an underground passage.")
            choice2 = input("Do you go into the tunnel or underground? ").lower()
            if choice2 == "tunnel":
                print("You walk down the path and find a treasure chest!")
                print("But, it's locked!")
                choice3 = input("Do you try to pick the lock or search for a key? ").lower()
                if choice3 == "pick":
                    if random.random() < 0.5:
                        print("You successfully pick the lock and find a magical sword!")
                        print("Congratulations, you won the game!")
                        break
                    else:
                        print("You failed to pick the lock and lost 20 health points.")
                        health_points -= 20
                elif choice3 == "search":
                    print("You find a key hidden in a nearby rock.")
                    print("You unlock the chest and find a treasure map!")
                    choice4 = input("Do you follow the map or explore the tunnel? ").lower()
                    if choice4 == "follow":
                        print("You find a hidden cave with a treasure chest filled with gold and jewels!")
                        print("Congratulations, you found the treasure!")
                        break
                    elif choice4 == "explore":
                        print("You find a hidden door that leads to a secret room.")
                        choice5 = input("Do you enter the room or go back? ").lower()
                        if choice5 == "enter":
                            print("You find a magical amulet that gives you superpowers!")
                            print("Congratulations, you won the game!")
                            break
                        elif choice5 == "go back":
                            print("You are back where you started.")
                        else:
                            print("Invalid choice. Please choose enter or go back.")
                else:
                    print("Invalid choice. Please choose pick or search.")
            elif choice2 == "underground":
                print("You find a hidden door that leads to a secret room.")
                choice6 = input("Do you enter the room or search the passage? ").lower()
                if choice6 == "enter":
                    print("You find a magical sword that gives you superpowers!")
                    print("Congratulations, you won the game!")
                    break
                elif choice6 == "search":
                    print("You find a clue that leads you back to the forest.")
                    print("You are back where you started.")
                else:
                    print("Invalid choice. Please choose enter or search.")
            else:
                print("Invalid choice. Please choose tunnel or underground.")
        elif choice1 == "right":
            print("You are caught by a wild animal and lost 30 health points.")
            health_points -= 30
        elif choice1 == "straight":
            print("You walk down the path and find a river.")
            choice7 = input("Do you cross the river or follow it? ").lower()
            if choice7 == "cross":
                print("You find a hidden village on the other side.")
                choice8 = input("Do you enter the village or explore the surroundings? ").lower()
                if choice8 == "enter":
                    print("You meet the village elder who gives you a magical amulet.")
                    print("Congratulations, you won the game!")
                    break
                elif choice8 == "explore":
                    print("You find a hidden cave with a treasure map.")
                    print("You are one step closer to finding the treasure!")
                else:
                    print("Invalid choice. Please choose enter or explore.")
            elif choice7 == "follow":
                print("You find a waterfall that leads to a hidden cave.")
                choice9 = input("Do you enter the cave or go back? ").lower()
                if choice9 == "enter":
                    print("You find a treasure chest filled with gold and jewels!")
                    print("Congratulations, you found the treasure!")
                    break
                elif choice9 == "go back":
                    print("You are back where you started.")
                else:
                    print("Invalid choice. Please choose enter or go back.")
            else:
                print("Invalid choice. Please choose cross or follow.")
        else:
            print("Invalid choice. Please choose left, right, or straight.")

        if health_points <= 0:
            print("You ran out of health points. Game over.")
            break

        print(f"Health points: {health_points}")

text_adventure_game()
