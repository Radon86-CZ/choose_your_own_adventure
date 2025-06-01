name = input("Type your name: ")
print("Welcome " + name + " to this adventure!")

answer = input("You are on a road, which way do you want to go? (left / right) ").lower()

if answer == "left":
    answer = input("You come to a river. Do you want to walk around it or swim across? (walk / swim) ").lower()

    if answer == "walk":
        print("You walked for a long time and ran out of food. You lose.")
    elif answer == "swim":
        print("You swam across and were attacked by a shark. You lose.")
    else:
        print("Invalid choice. You lose.")

elif answer == "right":
    answer = input("You come to a bridge. Do you want to cross it or go back? (cross / back) ").lower()

    if answer == "cross":
        answer = input("You crossed the bridge and found a treasure chest. Do you want to open it? (yes / no) ").lower()

        if answer == "yes":
            print("You opened the chest and found a lot of gold. You win!")
        elif answer == "no":
            print("You ignored the chest and kept walking. You were attacked by goblins. You lose.")
        else:
            print("Invalid choice. You lose.")

    elif answer == "back":
        print("You go back to the main road and are ambushed by bandits. You lose.")
    else:
        print("Invalid choice. You lose.")

else:
    print("Invalid choice. You lose.")
