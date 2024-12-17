name = "Sqiddyinkster🤣"
print(f"Welcome to {name}'s choose ur own adventure game! Let's get started.")
print("You find yourself in a dark room with 2 doors. One is red and one is blue.")
door_choice = input("Which door do you go in? Type 'red' for the red door or 'blue' for the blue door: ")

if door_choice == "red":
    print("You walk into the red door and meet a mad scientist who's on a mission to rule the village he lives in!")
    choice_1 = input("Do you want to help? Type '1' for help or '2' for don't help: ")
    if choice_1 == "1":
        print("""__________SUCCESS__________
        You help him achieve village domination! In return, he teleports you home.""")
    else:
        print("""__________GAME OVER__________
        You say no, and the scientist grabs a laser gun and vaporizes you.""")
elif door_choice == "blue":
    print("You walk into the blue door and find a turtle who asks you to eat a fish.")
    choice_2 = input("Do you eat the fish? Type '1' for yes or '2' for no: ")
    if choice_2 == "1":
        print("""__________SUCCESS__________
        The turtle thanks you and gives you a magical shell that can grant one wish.""")
    else:
        print("""__________GAME OVER__________
        The turtle becomes angry and throws you out of the room.""")
else:
    print("Invalid choice. Please select either 'red' or 'blue'.")
