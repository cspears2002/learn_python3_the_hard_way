print("You see a passage that leads right and another one that leads left.")
print("Which way do you want to go?")
print("1. Right")
print("2. Left")

direction = input("> ")

if direction == "1":
    print("You see an orc!")
    print("What do you do?")
    print("1. Fight")
    print("2. Flee")

    action = input("> ")
    if action != "2":
        print("The orc chops you in half!")
    else:
        print("You live to fight another day!")

elif direction == "2":
    print("You see gold!")
    print("What do you do?")
    print("1. Take it.")
    print("2. Leave it.")

    action = input("> ")
    if action == "1":
        print("You're rich!")
    else:
        print("You're poor!")

else:
    print(f"{direction} does not make any sense.")
    print("Goodbye!")
