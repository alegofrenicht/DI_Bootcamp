# 🌟 Exercise 1: Door
# 1. Create a Door class, it has only the following attributes:
#       id (int) : An id number, use a class variable objs that counts how many door have been created so far and use this number as the id of the door.
#       locked (boolean)
#       next (List of Door obs) : The next doors available from this one
#
# 2. Create a method can_go_to(self, other_door) in the Door class that checks if the path from this door to other_door can be made (the locked doors cannot be opened !).
#
# 3. Bonus: Display the path
# 4. Bonus 2: Add an integer variable KEYS that holds a limited number of keys available to open locked doors (each key can be used only once).

class Door:
    doors = 0
    keys = 3
    def __init__(self, locked: bool):
        Door.doors += 1
        self.id = Door.doors
        self.locked = locked
        self.next = []

    def __str__(self):
        print(f"Door number {self.id}")
    def can_go_to(self, other_door):
        if other_door.locked:
            self.next.append(f"Door {other_door.id}")
            print(f'You entered door number {other_door.id}')
        else:
            if Door.keys > 0:
                use_key = input(f'Door number {other_door.id} is locked! You wanna use the key? y/n')
                if use_key == 'y':
                    Door.keys -= 1
                    other_door.locked = True
                    self.next.append(f"Door {other_door.id}")
                    print(f'You entered door number {other_door.id}')
                elif use_key == 'n':
                    print(f'Door number {other_door.id} is locked')

            else:
                print(f'Door number {other_door.id} is locked')

door_one = Door(True)
door_two = Door(False)
door_three = Door(True)
door_four = Door(True)
door_one.can_go_to(door_two)
door_one.can_go_to(door_three)
door_one.can_go_to(door_four)
print(door_one.next)

