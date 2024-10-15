from random import randint

#def randint(a: int, b:int) -> int: return 0 

room_items = ["bow", "armour", "boomerang", "shield", "sword"]
visited_rooms = []
picked_up_items = []

def treasure_room() -> None:
    print("You have found the ultimate treasure chest! You win the game!")

def item_room(items: list[str]) -> str:
    idx = randint(0, 4)
    print(f"You found {room_items[idx]}, you decide to pick it up!")
    items.append(room_items[idx])

def monster_room(items: list[str]) -> bool:
    print("You have entered a room with a monster!")
    choice = input("Do you choose to fight or flee?")
    if (choice == "fight"):
        return fight_monster(items)
    elif (choice == "flee"):
        print("You fled back to the starting room.")
        return True
    else:
        while (choice != "fight" and choice != "flee"):
            choice = input("Invalid choice. Please choose to fight or flee.")
            if (choice == "fight"):
                return fight_monster(items)
            elif (choice == "flee"):
                print("You fled back to the starting room.")
                return True
            else:
                continue
                      
def fight_monster(items : list[str]) -> bool:
    print("You are fighting the monster...")
    roll = randint(0, 10)
    if (roll >= 4 - len(items)):
        print("You defeated the monster! You win!")
        return True
    else:
        print("The monster defeated you. You lose the game.")
        return False

def starting_room():
    doors = 3

    
    correct_door = randint(1, doors)
    print(f"You are in a room with {doors} doors.")
    while True:
        door_to_enter = int(input(f"Which door (1 - {doors}) do you choose? "))
        visited_rooms.append(door_to_enter)
        if (door_to_enter == correct_door):
            treasure_room()
            break
        else:
            if (randint(0,1) == 0):
                picked_up_items.append(item_room(room_items))
                continue
            else:
                res = monster_room(picked_up_items)
                if (res == None): continue
                elif (res == True) : continue
                else: break
    return (visited_rooms, picked_up_items)
