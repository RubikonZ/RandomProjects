# Text adventure состоит из комнат (например: комната, в которой есть различные предметы, с которыми можно
# взаимодействовать. В одной из комнат точно должна быть одна SpecialExitDoor, закрытая ключом и заканчивающая игру.
import random as rnd


n_of_rooms = 3
n_of_doors = n_of_rooms - 1
n_of_max_items = 3
n_of_keys = 1


class Item:
    """ Main ITEM class """
    item_id = 0  # Each generated item has ID
    item_size_list = ['tiny', 'small', 'medium', 'large', 'enormous']  # Наверное надо держать эти листы вне класса
    durability_list = ['fragile', 'very durable', 'sturdy', 'flexible', 'breakable']
    quality = ['new', 'used', 'terrible', 'broken']
    material = ['wooden', 'metallic', 'plastic', 'fiber', 'stone']

    def __init__(self):
        Item.item_id += 1
        self.item_size = rnd.choice(self.item_size_list)
        self.durability = rnd.choice(self.durability_list)
        self.item_name = self.__class__.__name__
        self.item_generated()

    def item_generated(self):
        print(f"Generated {self.item_name}, item id: {self.item_id}")


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
    door_id = 0

    def __init__(self):
        Door.door_id += 1
        print(f"Generated {__class__.__name__.lower()}, door id: {self.door_id}")


class UsualDoor(Door):
    """ Door between rooms, there is at least 1 door between 2 rooms """

    def __init__(self):
        super().__init__()
        print(f"Generated {__class__.__name__.lower()}, door id: {self.door_id}")


class SpecialExitDoor(Door):
    """ Only 1 exists to end the game """
    def __init__(self):
        super().__init__()
        self.is_unlocked = False
        self.special_door_exists = False
        print(f"Generated special DOOR")

    def exists(self):
        return self.special_door_exists

    def door_unlocked(self):
        return self.is_unlocked


class Room:
    """ Game consists of Rooms between which player can walk and interact with items """
    room_id = 0
    room_type = ['dungeon', 'apartment', 'closet', 'corridor']  # Can later make as subclasses to add variety
    illumination_type = ['blindingly bright', 'dark', 'dusk', 'dim', 'very dark', 'barely lit']
    environment_type = ['lovecraft-ish', 'hi-tech', 'urban', 'filthy', 'sterile']
    items_list = [Pen, Bottle, Gun, Chair, Key]  # List of all possible items
    door_list = [UsualDoor, SpecialExitDoor]

    def __init__(self):
        Room.room_id += 1
        self.room = Room.room_id
        self.room_type = rnd.choice(self.room_type)
        self.illumination = rnd.choice(self.illumination_type)
        self.env = rnd.choice(self.environment_type)
        self.items_in_room = []  # Enforced room to have exit
        self.actual_items = []
        self.contains_key = False
        self.player_in_room = False

        self.generate_room_filling(n_of_max_items)
        self.generate_room_doors()

    def generate_room_filling(self, max_items):
        """ generates ITEMS in room you entered, which are in 'items_in_room' list"""
        for item in range(rnd.randint(0, max_items)):
            self.items_in_room.append(rnd.choice(self.items_list))  # Storing list of items for each room
        print(f"Generating room #{self.room_id}:")
        print(f"There are {len(self.items_in_room)} items")
        print(f"Room seems to be {self.room_type}, which is {self.illumination} and looks {self.env}. You can also see next items:")

        # Adding items to item list
        for item in range(len(self.items_in_room)):  # Actual creation of items which were in list of items
            print(f'{item + 1}) ', end='')
            self.actual_items.append(self.items_in_room[item]())
        # Adding doors to item list

    def generate_room_doors(self):
        """ generates DOORS in room you entered """
        self.actual_items.append(SpecialExitDoor())
        if (len(game.list_of_rooms) + 1) < n_of_rooms:
            doors_in_room = rnd.choice(range(1, 3))
            game.n_of_doors -= doors_in_room
            for door in range(doors_in_room):
                self.actual_items.append(Door())
        else:
            for door in range(len(game.list_of_rooms)):
                self.actual_items.append(Door())

    def room_contains_key(self):
        """ Check if room has key """
        if Key in self.items_in_room:
            return True


class GameManager:
    """ Здесь происходит весь процесс игры: начало, конец, обработка команд """
    def __init__(self, n_of_rooms):
        self.list_of_rooms = []  # Maybe add 'Beginning room' (to fill index 0)
        self.player_has_key = False
        self.game_is_running = True
        self.number_of_rooms = n_of_rooms  # Initial amount of rooms in 'game'
        self.special_door_unlocked = None
        self.n_of_doors = n_of_rooms - 1
        # for _ in range(0, self.number_of_rooms):  #  Might return
        #     self.list_of_rooms.append(Room)

    def start_game(self):
        """ Generates rooms and SHOULD PLACE PLAYER in one of them """
        game.list_of_rooms.append(Room())  # Пока сделано для одной комнаты
        start_room = self.list_of_rooms[0]
        self.current_room_key = start_room.room_contains_key()
        print(self.current_room_key)

    def place_player(self):
        """ chooses in which room player starts """
        self.start_room = self.list_of_rooms.index((rnd.choice(self.list_of_rooms)))
        print(f'\nPlayer is in a room #{self.start_room + 1}')

    def input_handler(self):  # Много повторений, наверняка есть более простой способ
        """ Обработка команд игрока """
        plr_input = str(input()).lower().split()
        if len(plr_input) < 2:
            return

        if plr_input[0] == 'take':
            if plr_input[1] == 'key':
                self.take_key()
            else:
                print('There is no such item in a room')
        elif plr_input[0] == 'unlock':
            if plr_input[1] == 'specialdoor':
                if self.player_has_key:
                    self.special_door_unlocked = True
                    print('You have unlocked the door')
                else:
                    print("You don't have a key")
            else:
                print(f"There is no {plr_input[1]} in a room")
        elif plr_input[0] == 'enter':
            if plr_input[1] == 'specialdoor':
                if self.special_door_unlocked:
                    print('You finished the game 8)')
                    self.game_is_running = False
                else:
                    print("You don't have a key")
            elif plr_input[1] == 'door':
                self.enter_new_door()
            else:
                print(f"You can't enter {plr_input[1]}")
        else:
            print('There is no such command')

    def game_process(self):
        """ Main process where whole game is happening"""
        self.start_game()
        self.place_player()
        while self.game_is_running:
            self.input_handler()

    def enter_new_door(self):
        self.new_room = Room()
        self.list_of_rooms.append(self.new_room)
        print(f'You entered new room {len(self.list_of_rooms)} with id {self.list_of_rooms.index(self.new_room)}')

    def take_key(self):
        if self.current_room_key:
            self.player_has_key = True
            current_room.current_room_key = False
            print('Player took the key')


if __name__ == '__main__':
    while True:
        start = str(input('Start new game? (Y/N): ')).lower()
        if start == 'y':
            game = GameManager(n_of_rooms)
            print(f'{n_of_rooms} rooms in this adventure')
            game.game_process()
        elif start == 'n':
            break
        else:
            print('Wrong input. Try again')
            continue
