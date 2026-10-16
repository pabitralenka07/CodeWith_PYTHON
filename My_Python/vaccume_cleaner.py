# Vacuum Cleaner Problem
# Simple Reflex Agent

def vacuum_cleaner(rooms, position):
    print("\n--- Initial Environment ---")
    for room, status in rooms.items():
        print(f"{room}: {status}")
    print("Vacuum Position:", position)

    while "Dirty" in rooms.values():

        if rooms[position] == "Dirty":
            print(f"\n{position} is Dirty")
            print("Action: SUCK")
            rooms[position] = "Clean"

        else:
            print(f"\n{position} is Clean")

            dirty_rooms = [
                room for room, status in rooms.items()
                if status == "Dirty"
            ]

            if dirty_rooms:
                next_room = dirty_rooms[0]
                print(f"Action: MOVE from {position} to {next_room}")
                position = next_room

    print("\n--- Final Environment ---")
    for room, status in rooms.items():
        print(f"{room}: {status}")

    print("Vacuum Position:", position)
    print("Action: STOP")
    print("All rooms are clean!")


rooms = {
    "A": "Dirty",
    "B": "Clean",
    "C": "Dirty",
    "D": "Dirty"
}

start_position = "A"

vacuum_cleaner(rooms, start_position)
