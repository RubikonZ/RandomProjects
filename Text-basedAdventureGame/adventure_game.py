# Текстовое приключение состоит из ВИДОВ (например: комната, в которой есть различные предметы, взаимодействующие между
# собой. Внутри комнат также можно фокусироваться на предметах/примечательных объектах
import random as rnd

# class InteractableObject: # Need to classify which items are interactable and which are part of room (window/door/etc)

class Item:
    """ Main ITEM class """
    item_id = 0  # Each generated item has ID
    item_size_list = ['tiny', 'small', 'medium', 'large', 'enormous']
    durability_list = ['fragile', 'very durable', 'sturdy', 'flexible', 'breakable']
    quality = ['new', 'used', 'terrible', 'broken']

    def __init__(self):
        Item.item_id += 1
        self.item_size = rnd.choice(self.item_size_list)
        self.durability = rnd.choice(self.durability_list)


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
        print(f"Generated gun, item id: {self.item_id}")


class Room:
    """ Game consists of Rooms between which player can walk and interact with random items """
    room_id = 0
    room_type = ['dungeon', 'apartment', 'closet', 'corridor']
    illumination_type = ['usual', 'blindingly bright', 'dark', 'dusk', 'dim', 'very dark', 'hazy']
    environment_type = ['lovecraftian', 'hi-tech', 'urban', 'filthy', 'sterile']

    def __init__(self):
        Room.room_id += 1
        self.room_type = rnd.choice(self.room_type)
        self.illumination = rnd.choice(self.illumination_type)
        self.env = rnd.choice(self.environment_type)
        self.items_list = [Pen(), Pen(), Pen(), Bottle(), Bottle(), Bottle(), Gun(), Gun(), Gun()] # Generated list of chosen items
        rnd.shuffle(self.items_list)
        self.nmbr_of_items_in_room = rnd.randint(0, 4)
        self.items_in_room = rnd.sample(self.items_list, self.nmbr_of_items_in_room) # Choosing random items from item list
        print(f"There are {len(self.items_in_room)} items in a room {self.room_id}")

    def generate_room(self):
        """ """
        # print(f"You've entered {self.room}, it looks {self.illumination} and on the first glance seems {self.env}")
        pass

    def generate_items(self):
        """ Should generate random items """
        self.number_of_items = rnd.randint(0, 3)
        print(self.number_of_items)
        for item_number in range(self.number_of_items):
            rnd.choice(item_list)

    # def exit_room(self):


class GameManager:

    def __init__(self):
        self.rooms = []
        self.game_is_running = True
        self.number_of_rooms = rnd.randint(1, 4)

    def start_game(self):
        for generated_room in range(1, self.number_of_rooms):
            Room()
            print(f'Generated room {generated_room}')
        # print(f"You've entered {self.room}, it looks {self.illumination} and on the first glance seems {self.env}")

    # def game(self):
    #     while self.game_is_running:



if __name__ == '__main__':
    room = GameManager()
    room.start_game()
    # room.generate_items()
