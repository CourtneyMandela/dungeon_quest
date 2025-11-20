import random

def setup_player():
    """
    Prompts the user to create their player profile.

    Returns:
        dict: A dictionary containing player stats with the following keys:
            - "name" (str): Player's name (entered by user)
            - "health" (int): Starting health, set to 10
            - "inventory" (list): Starts as an empty list
    """
    player_name = input("Enter your name: ")
    player = {
        "name": player_name,
        "health": 10,
        "inventory": []
    }
    return player


def create_treasures():
    """
    Creates a dictionary of treasures, where each treasure has a value.
    """
    treasures = {
        "gold coins": random.randint(3, 12),
        "silver ring": random.randint(3, 12),
        "leather pouch": random.randint(3, 12),
        "iron dagger": random.randint(3, 12),
        "wooden shield": random.randint(3, 12),
        "health potion": random.randint(3, 12),
        "mana potion": random.randint(3, 12),
        "torch": random.randint(3, 12),
        "rope coil": random.randint(3, 12),
        "lockpick set": random.randint(3, 12),
        "small ruby": random.randint(3, 12),
        "silver necklace": random.randint(3, 12),
        "old key": random.randint(3, 12),
        "map scroll": random.randint(3, 12),
        "gemstone": random.randint(3, 12)
    }
    return treasures


def display_options(room_number):
    """
    Displays available options for the player in the current room.
    """
    print(f"\nYou are in room {room_number}")
    print("What would you like to do?")
    print("1. Search for treasure")
    print("2. Move to next room")
    print("3. Check health and inventory")
    print("4. Quit the game")


def search_room(player, treasures):
    """
    Simulates searching the current room.
    """
    outcome = random.choice(["treasure", "trap"])

    if outcome == "treasure":
        room_treasure = random.choice(list(treasures.keys()))
        player["inventory"].append(room_treasure)
        print(f"You search the room and find: {room_treasure}!")
    else:
        player["health"] -= 2
        print("A trap is triggered! You lose 2 health.")
        print(f"Your health is now: {player['health']}")


def check_status(player):
    """
    Displays the player’s current health and inventory.
    """
    print(f"\nHealth: {player['health']}")
    if player["inventory"]:
        print("Inventory:", ", ".join(player["inventory"]))
    else:
        print("Inventory: You have no items yet.")


def end_game(player, treasures):
    """
    Ends the game and displays a summary.
    """
    total_score = 0
    for item in player["inventory"]:
        if item in treasures:
            total_score += treasures[item]

    print("\n--- Game Summary ---")
    print(f"Final Health: {player['health']}")
    if player["inventory"]:
        print("Final Inventory:", ", ".join(player["inventory"]))
    else:
        print("Final Inventory: No items collected.")
    print(f"Total treasure value: {total_score}")
    print("Game Over! Thanks for playing.")


def run_game_loop(player, treasures):
    """
    Main game loop that manages the rooms and player decisions.
    """
    for room_number in range(1, 6):

        if player["health"] <= 0:
            print("\nYou have no health left!")
            end_game(player, treasures)
            return

        print(f"\n--- Entering room {room_number} ---")

        in_room = True

        while in_room:
            display_options(room_number)
            choice = input("Enter your choice (1–4): ")

            if choice == "1":
                search_room(player, treasures)
                if player["health"] <= 0:
                    print("You succumb to your injuries...")
                    end_game(player, treasures)
                    return

            elif choice == "2":
                print(f"You leave room {room_number} and move on...")
                in_room = False

            elif choice == "3":
                check_status(player)

            elif choice == "4":
                print("You decide to leave the dungeon early.")
                end_game(player, treasures)
                return

            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

    print("\nYou have explored all 5 rooms in the dungeon!")
    end_game(player, treasures)


def main():
    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    run_game_loop(player, treasures)


if __name__ == "__main__":
    main()
