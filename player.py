class Player:

    def __init__(self, x, y):
        '''
        Creates a new Player.
        :param x: x-coordinate of position on map
        :param y: y-coordinate of position on map
        :return:

        This is a suggested starter class for Player.
        You may add new parameters / attributes / methods to this class as you see fit.
        Consider every method in this Player class as a "suggested method":
                -- Suggested Method (You may remove/modify/rename these as you like) --
        '''
        self.x = x
        self.y = y
        self.inventory = []
        self.victory = False
        self.score = 0
        self.moves = 0

    def move(self, dx, dy):
        '''
        Given integers dx and dy, move player to new location (self.x + dx, self.y + dy)
        :param dx: The difference between the new and old x coordinate
        :param dy: The difference between the new and old y coordinate
        :return: The new x and y coordinates
        '''

        self.x += dx
        self.y += dy

        return self.x, self.y

    def move_north(self):
        '''These integer directions are based on how the map must be stored
        in our nested list World.map
        Returns new coordinate values from Player.move'''
        return self.move(-1, 0)

    def move_south(self):
        return self.move(1, 0)

    def move_east(self):
        return self.move(0, 1)

    def move_west(self):
        return self.move(0, -1)

    def add_item(self, item):
        '''
        Add item to inventory.
        :param item: Item being picked up and put into the player's inventory
        :return:
        '''

        self.inventory.append(item)

    def remove_item(self, item):
        '''
        Remove item from inventory.
        :param item: Item chosen to be removed
        :return:
        '''

        self.inventory.remove(item)

    def get_inventory(self):
        '''
        Return inventory.
        :return: The player's current inventory
        '''

        return "Inventory: {0}".format(self.inventory)

    def get_score(self):
        '''
        Return score
        :return: The player's current score
        '''

        return "Score: {0}".format(self.score)
