import random
import sys
import time
import os

# Cool feature that I borrowed from https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing
def print_slow(str, wait):
    for letter in str:
        sys.stdout.write(letter)
        time.sleep(wait)

#Adventure Game James Portune
os.system('cls' if os.name == 'nt' else 'clear')
print_slow("Last night, you went to sleep in your own home.", .1)
os.system('cls' if os.name == 'nt' else 'clear')
print_slow("\nNow, you wake up in a locked room.", .1)
os.system('cls' if os.name == 'nt' else 'clear')
print_slow("\nCould there be a key hidden somewhere?", .1)
os.system('cls' if os.name == 'nt' else 'clear')
print_slow("\nIn the room, you can see:\n", .1)

#The menu function
def menu(list, question):
    for item in list:
        print(1 + list.index(item), item)
    return int(input(question))

#This is a lit of the items in the room:
items = ["Backpack", "Painting", "Vase", "Bowl", "Door"]

keyLocation = random.randint(1,4)

#The key is not found:
keyFound = "No"
loop = 1

while loop == 1:
    choice = menu(items, "What do you want to inspect?")
    print("")
    if choice < 5:
        if choice == keyLocation:
            os.system('cls' if os.name == 'nt' else 'clear')
            print_slow(". . . . .\n", .3)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nYou found a small key in the", items[choice -1])
            keyFound = "Yes"
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print_slow(". . . . .\n", .3)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("You found nothing in the", items[choice -1])
    elif choice == 5:
        if keyFound == "Yes":
            loop = 0
            os.system('cls' if os.name == 'nt' else 'clear')
            print_slow("\nYou insert the key in the keyhole and turn it.", .1)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nThe door is locked. You need to find a key.")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Choose a number less than 6.")