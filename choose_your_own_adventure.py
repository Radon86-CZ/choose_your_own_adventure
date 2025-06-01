name = input("Type your name: ")
print("Welcome " + str(name) + " to this adventure!")

answer = input("You are on a road, which way do you want to go? (left / right) ").lower()

if answer == "left":
    answer = input("You come to a river, do you want to walk around it or swim across? (walk / swim) ")

    if answer == "walk":
        print("You swam across and were attacked by a shark. ")

    if answer == "swim":
        print("You walked for a long time and ran out of food. ")

elif answer == "right":
    answer = input("You come to a bridge. Do you want to cross it or go back? (cross / back) ")

    if answer == "cross":
        print("You crossed the bridge and found a treasure chest. Do you want to open it? (yes / no) ")

        if answer == "yes":
            print("You opened the chest and found a lot of gold. You won! ")

        if answer == "no":
            print("You ignored the chest and kept walking. You were attacked by goblins. ")

    if answer == "back":
        print("You go back to the main road and are ambushed by some bandits.")

else:
    print("You lose!")

