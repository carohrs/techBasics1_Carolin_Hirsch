# --- Game State ---

#escape game
inventory = []

# Items in the room
items_in_room = [
    {"name": "Torch", "type": "tool", "description": "Lights up dark places."},
    {"name": "Apple", "type": "food", "description": "Restores a small amount of health."},
    {"name": "Key", "type": "tool", "description": "Opens a locked door."},
    {"name": "Map", "type": "tool", "description": "Shows the layout of the dungeon."},
    {"name": "Rock", "type": "junk", "description": "A heavy, useless rock."},
    {"name": "Potion", "type": "healing", "description": "A magical red liquid."}
]

MAX_INVENTORY_SIZE = 5

def show_inventory():
    #checking if the list is empty first
    if len(inventory) == 0:
        print("Your inventory is empty.")
    else:
        print("You have:")
        for item in inventory:
            print(item.get("name"))

def show_room_items():
    if len(items_in_room) == 0:
        print("The room is empty.")
    else:
        print("Items in the room:")
        for item in items_in_room:
            print(item.get("name"))

def pick_up(item_name):
    #checking if the list is full first
    if len(inventory) >= MAX_INVENTORY_SIZE:
        print("Your inventory is full.")
    else:
        if len(items_in_room) == 0:
            print("There are no items in the room.")
        else:
            for item in items_in_room:
                if item["name"].lower() == item_name:
                    inventory.append(item)
                    items_in_room.remove(item)
                    print(f"You picked up the {item['name']}.")
                    return
            print(f"There is no {item_name} in the room.")

def drop(item_name):
    for item in inventory:
        if item["name"].lower() == item_name:
            inventory.remove(item)
            items_in_room.append(item)
            print(f"You dropped the {item['name']}.")
            return

    print(f"You don't have a {item_name} in your inventory.")

def use(item_name):
    for item in inventory:
        if item["name"].lower() == item_name:
            if item["name"] == "Key":
                print("You use the Key to unlock the heavy wooden door. You escape the dungeon! YOU WIN!")
                return "win"

            elif item["type"] in ["food", "healing"]:
                print(f"You consume the {item['name']}. You feel refreshed.")
                inventory.remove(item)

            else:
                print(f"You use the {item['name']}, but nothing special happens.")
            return ""

    print(f"You don't have a '{item_name}' in your inventory to use.")
    return ""

def examine(item_name):
    all_items = inventory + items_in_room
    for item in all_items:
        if item["name"].lower() == item_name:
            print(f"{item['name']}: {item['description']}")
            return

    print(f"Cannot find {item_name} to examine.")

# --- Game Loop ---

def game_loop():
    print("Welcome to the Inventory Game!")
    print("Type 'help' for a list of commands.")

    while True:
        command = input("\n> ").strip().lower()

        match command.split():
            case ["help"]:
                print("Commands: inventory, look, pickup [item], drop [item], use [item], examine [item], quit")
            case ["inventory"]:
                show_inventory()
            case ["look"]:
                show_room_items()
            case ["pickup", item_name]:
                pick_up(item_name)
            case ["drop", item_name]:
                drop(item_name)
            case ["use", item_name]:
                status = use(item_name)
                if status == "win":
                    break
            case ["examine", item_name]:
                examine(item_name)
            case ["quit"]:
                print("Thanks for playing!")
                break
            case _: # else
                print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    game_loop()