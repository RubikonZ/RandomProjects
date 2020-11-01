# Текстовое приключение состоит из ВИДОВ (например: комната, в которой есть различные предметы, взаимодействующие между
# собой. Внутри комнат также можно фокусироваться на предметах/примечательных объектах
import random as rnd

# class InteractableObject: # Need to classify which items are interactable and which are part of room (window/door/etc)
n_of_rooms = 1
n_of_max_items = 3
n_of_keys = 1
n_of_doors = 2

class Item:
    """ Main ITEM class """
    item_id = 0  # Each generated item has ID
    item_size_list = ['tiny', 'small', 'medium', 'large', 'enormous']
    durability_list = ['fragile', 'very durable', 'sturdy', 'flexible', 'breakable']
    quality = ['new', 'used', 'terrible', 'broken']
    material = ['wooden', 'metallic', 'plastic', 'fiber', 'stone']

    def __init__(self):
        Item.item_id += 1
        self.item_size = rnd.choice(self.item_size_list)
        self.durability = rnd.choice(self.durability_list)
        # print(f"Generated {__class__.__name__}")  # Find out how to print __class__.__name__ for each subclass as well


class Chair(Item):
    def __init__(self):
        super().__init__()
        self.material = rnd.choice(self.material)
        print(f"Generated {__class__.__name__.lower()}, item id: {self.item_id}")


class Glass(Item):
    """ type of material """
    def __init__(self):
        super().__init__()
        self.durability = 'fragile'


class Bottle(Glass):
    liquid_color = ['blood-ish', 'transparent', 'purple', 'very dark', 'orange']
    filled = ['empty', 'almost empty', 'half full', 'full and completely untouched']

    def __init__(self):
        super().__init__()
        print(f"Generated bottle, item id: {self.item_id}")


class Pen(Item):
    def __init__(self):
        super().__init__()
        self.item_size = 'small'
        print(f"Generated pen, item id: {self.item_id}")


class Gun(Item):
    def __init__(self):
        super().__init__()
        self.item_size = 'small'
        self.durability = rnd.choice(self.quality)
        print(f"Generated {self.item_size}, {self.durability} gun, item id: {self.item_id}")


class Key(Item):
    def __init__(self):
        super().__init__()
        print(f"Generated {__class__.__name__.lower()}, item id: {self.item_id}")


class Door:
    """ Door between rooms, there is at least 1 door between 2 rooms """
    pass


class SpecialExitDoor(Door):
    """ Only 1 exists to end the game """
    def __init__(self):
        self.is_unlocked = False
        print(f"Generated special DOOR")

    def door_unlocked(self):
        return self.is_unlocked


class Room:
    """ Game consists of Rooms between which player can walk and interact with random items """
    room_id = 0
    room_type = ['dungeon', 'apartment', 'closet', 'corridor']
    illumination_type = ['usual', 'blindingly bright', 'dark', 'dusk', 'dim', 'very dark', 'hazy']
    environment_type = ['lovecraft-ish', 'hi-tech', 'urban', 'filthy', 'sterile']
    items_list = [Pen, Bottle, Gun, Chair, Key]  # List of all possible items

    def __init__(self):
        Room.room_id += 1
        self.room_type = rnd.choice(self.room_type)
        self.illumination = rnd.choice(self.illumination_type)
        self.env = rnd.choice(self.environment_type)
        self.items_in_room = [SpecialExitDoor]  # Enforced room to have exit
        self.actual_items = []
        self.contains_key = False

    def generate_room_filling(self):
        """ generates ITEMS which are in 'items_in_room' list"""
        for item in range(rnd.randint(0, 4)):
            self.items_in_room.append(rnd.choice(self.items_list))  # Storing list of items for each room
        print(f"Generating room #{self.room_id}:")
        print(f"There are {len(self.items_in_room)} items")
        print(f"Room seems to be {self.room_type}, which is {self.illumination} and looks {self.env}. You can also see next items:")
        for item in self.items_in_room:  # Actual creation of items which were in list of items
            self.actual_items.append(item())

    # def generate_items(self):
    #     """ Should generate random items """
    #     self.number_of_items = rnd.randint(0, 3)
    #     print(self.number_of_items)
    #     for item_number in range(self.number_of_items):
    #         rnd.choice(item_list)

    def room_contains_key(self):
        """ Check if room has key """
        if Key in self.items_in_room:
            self.contains_key = True
            return self.contains_key


class GameManager:

    def __init__(self, n_of_rooms):
        self.list_of_rooms = []
        self.player_has_key = False
        self.game_is_running = True
        self.number_of_rooms = n_of_rooms
        self.special_door_unlocked = None
        for _ in range(0, self.number_of_rooms):
            self.list_of_rooms.append(Room)

    def start_game(self):
        """ Generates rooms and SHOULD PLACE PLAYER in one of them """
        for room in self.list_of_rooms:  # This should only work if there is 1 room. (refactor to work with many rooms)
            only_room = room()
            only_room.generate_room_filling()
            self.current_room_key = only_room.room_contains_key()
            self.special_door_unlocked = only_room.actual_items[0].is_unlocked
            # if self.special_door_unlocked is None:
            #     self.special_door_unlocked = only_room.actual_items[0].is_unlocked
        self.place_player()

    def game_process(self):
        """ Main process where whole game is happening"""
        while self.game_is_running:
            plr_input = str(input()).lower().split()
            if plr_input[0] == 'take':
                if plr_input[1] == 'key':
                    if self.current_room_key:
                        self.player_has_key = True
                        print('You picked up a key')
                    else:
                        print('There is no key in a room')
                else:
                    print('There is no such item in a room')
            elif plr_input[0] == 'unlock':
                if plr_input[1] == 'door':
                    if self.player_has_key:
                        self.special_door_unlocked = True
                        print('You have unlocked the door')
                    else:
                        print("You don't have a key")
                else:
                    print(f"There is no {plr_input[1]} in a room")
            elif plr_input[0] == 'enter':
                if plr_input[1] == 'door':
                    if self.special_door_unlocked:
                        print('You finished the game 8)')
                        self.game_is_running = False
                    else:
                        print("You don't have a key")
                else:
                    print(f"You can't enter {plr_input[1]}")
            else:
                print('There is no such command')


    def place_player(self):
        """ chooses in which room player starts """
        self.start_room = self.list_of_rooms.index((rnd.choice(self.list_of_rooms)))
        print(f'\nPlayer is in a room #{self.start_room + 1}')


if __name__ == '__main__':
    while True:
        start = str(input('Start new game? (Y/N): ')).lower()
        if start == 'y':
            game = GameManager(n_of_rooms)
            game.start_game()
            game.game_process()
        elif start == 'n':
            break
        else:
            print('Wrong input. Try again')
            continue


