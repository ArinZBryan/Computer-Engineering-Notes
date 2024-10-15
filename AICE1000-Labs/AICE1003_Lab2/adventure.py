from random import randint

room_items = ["bow", "armour", "boomerang", "shield", "sword"]

def treasure_room() -> None:
    print("You have found the ultimate treasure chest! You win the game!")

def item_room() -> None:
    idx = randint(0, 4)
    print(f"You found {room_items[idx]}, you decide to pick it up!")
    return

def monster_room() -> bool:
    print("You have entered a room with a monster!")
    choice = input("Do you choose to fight or flee?")
    if (choice == "fight"):
        return fight_monster()
    elif (choice == "flee"):
        print("You fled back to the starting room.")
        return True
    else:
        while (choice != "fight" and choice != "flee"):
            choice = input("Invalid choice. Please choose to fight or flee.")
            if (choice == "fight"):
                return fight_monster()
            elif (choice == "flee"):
                print("You fled back to the starting room.")
                return True
            else:
                continue
        
            
def fight_monster() -> bool:
    print("You are fighting the monster...")
    roll = randint(0, 10)
    if (roll > 3):
        print("You defeated the monster! You win!")
        return True
    else:
        print("The monster defeated you. You lose the game.")
        return False

def starting_room():
    doors = 3
    treasure_door = randint(1, doors)
    print(f"You are in a room with {doors} doors.")
    while True:
        door_to_enter = int(input(f"Which door (1 - {doors}) do you choose? "))
        if (door_to_enter == treasure_door):
            treasure_room()
            break
        else:
            if (randint(0,1) == 1):
                item_room()
                continue
            else:
                res = monster_room()
                if (res == None): continue
                elif (res == True) : continue
                else: return
            
starting_room()