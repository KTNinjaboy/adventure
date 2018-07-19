class Location:

    def __init__(self, index, points, brief, long):
        '''
        Creates a new location.

        Data that could be associated with each Location object:
        a position in the world map,
        a brief description,
        a long description,
        a list of available commands/directions to move,
        items that are available in the location,
        and whether or not the location has been visited before.
        Store these as you see fit.

        This is just a suggested starter class for Location.
        You may change/add parameters and the data available for each Location class as you see fit.
  
        The only thing you must NOT change is the name of this class: Location.
        All locations in your game MUST be represented as an instance of this class.
        '''

        self.index = index
        self.points = points
        self.brief = brief
        self.long = long
        self.times_visited = 0

    def get_brief_description(self):
        '''Return str brief description of location.'''

        return self.brief

    def get_full_description(self):
        '''Return str long description of location.'''

        return self.long

    def available_actions(self):
        '''
        -- Suggested Method (You may remove/modify/rename this as you like) --
        Return list of the available actions in this location.
        The list of actions should depend on the items available in the location
        and the x,y position of this location on the world map.'''

        if self.index == "1":
            return ["go west"]

        elif self.index == "2":
            return ["go east", "go south", "go west"]

        elif self.index == "3":
            return ["go north", "go west"]

        elif self.index == "4":
            return ["go north", "go east", "go south", "go west"]

        elif self.index == "5":
            return ["go south", "go in exam room"]

        elif self.index == "6":
            return ["go north", "go east"]

        elif self.index == "7":
            return ["go east"]


class Item:

    def __init__(self, name, start, target, target_points):
        '''Create item referred to by string name, with integer "start"
        being the integer identifying the item's starting location,
        the integer "target" being the item's target location, and
        integer target_points being the number of points player gets
        if item is deposited in target location.

        This is just a suggested starter class for Item.
        You may change these parameters and the data available for each Item class as you see fit.
        Consider every method in this Item class as a "suggested method":
                -- Suggested Method (You may remove/modify/rename these as you like) --

        The only thing you must NOT change is the name of this class: Item.
        All item objects in your game MUST be represented as an instance of this class.
        '''

        self.name = name
        self.start = int(start)
        self.target = int(target)
        self.points = int(target_points)

    def get_starting_location(self):
        '''Return int location where item is first found.'''

        return self.start

    def get_name(self):
        '''Return the str name of the item.'''

        return self.name

    def get_target_location(self):
        '''Return item's int target location where it should be deposited.'''

        return self.target

    def get_target_points(self):
        '''Return int points awarded for depositing the item in its target location.'''

        return self.points


class World:

    def __init__(self, mapdata, locdata, itemdata):
        '''
        Creates a new World object, with a map, and data about every location and item in this game world.

        You may ADD parameters/attributes/methods to this class as you see fit.
        BUT DO NOT RENAME OR REMOVE ANY EXISTING METHODS/ATTRIBUTES.

        :param mapdata: name of text file containing map data in grid format (integers represent each location, separated by space)
                        map text file MUST be in this format.
                        E.g.
                        1 -1 3
                        4 5 6
                        Where each number represents a different location, and -1 represents an invalid, inaccessible space.
        :param locdata: name of text file containing location data (format left up to you)
        :param itemdata: name of text file containing item data (format left up to you)
        :return:
        '''

        self.map = self.load_map(mapdata) # The map MUST be stored in a nested list as described in the docstring for load_map() below
        # self.locations ... You may choose how to store location and item data.
        self.locations = self.load_locations(locdata) # This data must be stored somewhere. Up to you how you choose to do it...
        self.items = self.load_items(itemdata) # This data must be stored somewhere. Up to you how you choose to do it...

    def load_map(self, filename):
        '''
        THIS FUNCTION MUST NOT BE RENAMED OR REMOVED.
        Store map from filename (map.txt) in the variable "self.map" as a nested list of integers like so:
            1 2 5
            3 -1 4
        becomes [[1,2,5], [3,-1,4]]
        RETURN THIS NEW NESTED LIST.
        :param filename: string that gives name of text file in which map data is located
        :return: return nested list of integers representing map of game world as specified above
        '''

        self.map = open(filename, 'r')

        map = []

        for line in self.map:
            line = line.split()
            map.append(line)

        self.map.close()

        return map

    def load_locations(self, filename):
        '''
        Store all locations from filename (locations.txt) into the variable "self.locations"
        however you think is best.
        Remember to keep track of the integer number representing each location.
        Make sure the Location class is used to represent each location.
        Change this docstring as needed.
        :param filename: string that gives name of text file in which location data is located
        :return: a nested list of location and its description
        '''

        self.locations = open(filename, 'r')

        places = []

        for line in self.locations:

            line = line.strip("\n")
            split_line = line.split()

            if split_line[0] == "LOCATION":

                index = split_line[1]
                points = self.locations.readline().strip("\n")
                brief = self.locations.readline().strip("\n")
                long = self.locations.readline().strip("\n")

                check_end = self.locations.readline().strip("\n")

                while check_end != "END":
                    long = "{0} {1}".format(long, check_end)
                    check_end = self.locations.readline().strip("\n")

                self.locations.readline()

                loc = Location(index, points, brief, long)
                places.append(loc)

        self.locations.close()

        return places

    def load_items(self, filename):
        '''
        Store all items from filename (items.txt) into ... whatever you think is best.
        Make sure the Item class is used to represent each item.
        Change this docstring accordingly.
        :param filename:
        :return:
        '''

        self.items = open(filename, 'r')

        things = []

        for line in self.items:

            line = line.strip("\n")

            start = line
            target = self.items.readline().strip("\n")
            points = self.items.readline().strip("\n")
            name = self.items.readline().strip("\n")
            self.items.readline()

            stuff = Item(name, start, target, points)
            things.append(stuff)

        self.items.close()

        return things

    def get_location(self, x, y):
        '''Check if location exists at location (x,y) in world map.
        Return Location object associated with this location if it does. Else, return None.
        Remember, locations represented by the number -1 on the map should return None.
        :param x: integer x representing x-coordinate of world map
        :param y: integer y representing y-coordinate of world map
        :return: Return Location object associated with this location if it does. Else, return None.
        '''

        if int(self.map[x][y]) in range(1234567):
            return self.locations[int(self.map[x][y])]

        else:
            return None

    def is_action(self, action):
        '''
        Checks if the player entered an action.
        Returns True or False whether the action the player entered is valid. True if action is an action. False otherwise.
        :param action: The player's input
        :return: True if player's input is an action. False otherwise.
        '''

        valid_actions = ["look", "inventory", "score", "quit", "go", "pickup", "drop"]

        if action[0] in valid_actions:
            return True

        else:
            return False

    def do_action(self, player, position, items, action, look_used):
        '''
        Reads the action that is requested to be done.
        Return whether the action was completed or if it has an error and tells the player what is the correct
        format to type in order to do the action.
        :param player: The player's current location index
        :param position: The player's current location object
        :param items: The list of item objects
        :param action: The player's input
        :return:
        '''

        if action == "" or not self.is_action(action.split()):
            return "Your action could not be processed.", look_used

        action = action.split()

        items_list = []

        for product in items:
            items_list.append(product.name.lower())

        tcard = "As you look around you notice a T-Card on the floor"
        lucky_pen = "As you look around you notice your lucky pen on the floor"
        cheat_sheet = "You see your cheat sheet on the ground"

        if len(action) == 1:

            if action[0] == "look":
                look_used = True
                return position.get_full_description(), look_used

            elif action[0] == "inventory":
                return player.get_inventory(), look_used

            elif action[0] == "score":
                return player.get_score(), look_used

            elif action[0] == "quit":
                return "GAME OVER!!!", look_used

            elif action[0] == "go":
                return "[go (direction: north, east, south, west)]", look_used

            elif action[0] == "pickup":
                return "[pickup (item name)]", look_used

            elif action[0] == "drop":
                return "[drop (item name)]", look_used

            else:
                return "[menu]", look_used

        elif len(action) >= 2:
            if action[0] == "look":
                return "[look]", look_used

            elif action[0] == "inventory":
                return "[inventory]", look_used

            elif action[0] == "score":
                return "[score]", look_used

            elif action[0] == "quit":
                return "[quit]", look_used

            elif action[0] == "go":

                action_details = ""
                for i in range(1, len(action)):
                    action_details = action_details + action[i] + " "
                action = [action[0], action_details.rstrip(" ")]

                if action[1] == "in exam room":

                    if len(player.inventory) == 3:
                        return "There seems to be a lock to get into the exam room. It's a lock with a 3-digit code. (HINT: The numbers were on pieces of paper throughout the building)", look_used

                    else:
                        return "You are missing the required items needed to enter and write the exam.", look_used

                elif action[1] == "north":
                    (x, y) = player.move_north()
                    if self.get_location(x, y) is None:
                        player.move_south()
                        return "That way is blocked", look_used

                    if position.times_visited == 1:
                        player.score += int(position.points)

                    player.moves += 1
                    return "Moved north", look_used

                elif action[1] == "east":
                    (x, y) = player.move_east()
                    if self.get_location(x, y) is None:
                        player.move_west()
                        return "That way is blocked", look_used

                    if position.times_visited == 1:
                        player.score += int(position.points)

                    player.moves += 1
                    return "Moved east", look_used

                elif action[1] == "south":
                    (x, y) = player.move_south()
                    if self.get_location(x, y) is None:
                        player.move_north()
                        return "That way is blocked", look_used

                    if position.times_visited == 1:
                        player.score += int(position.points)

                    player.moves += 1
                    return "Moved south", look_used

                elif action[1] == "west":
                    (x, y) = player.move_west()
                    if self.get_location(x, y) is None:
                        player.move_east()
                        return "That way is blocked", look_used

                    if position.times_visited == 1:
                        player.score += int(position.points)

                    player.moves += 1
                    return "Moved west", look_used

                else:
                    return "[go (direction: north, east, south, west)]", look_used

            elif action[0] == "pickup":

                action_details = ""
                for i in range(1, len(action)):
                    action_details = action_details + action[i] + " "
                action = [action[0], action_details.rstrip(" ")]

                if action[1] in items_list:

                    item_index = 0
                    for product in items:

                        if action[1] == product.name.lower():

                            if int(position.index) == items[item_index].start:

                                if action[1] in player.get_inventory().lower():
                                    return "You have already picked up your {0}.".format(items[item_index].name), look_used

                                player.add_item(items[item_index].name)
                                player.moves += 1
                                player.score += items[item_index].points

                                split_long = position.long.split(". ")

                                if items[item_index].name == "Lucky Pen":

                                    for line in split_long:

                                        if line == lucky_pen:
                                            split_long.remove(lucky_pen)

                                elif items[item_index].name == "T-card":

                                    for line in split_long:

                                        if line == tcard:
                                            split_long.remove(tcard)

                                elif items[item_index].name == "Cheat Sheet":

                                    for line in split_long:

                                        if line == cheat_sheet:
                                            split_long.remove(cheat_sheet)

                                new_long = '. '.join(split_long)
                                position.long = new_long
                                return "You picked up {0}.".format(items[item_index].name), look_used

                            else:
                                return "{0} was not found in this location.".format(items[item_index].name), look_used

                        else:
                            item_index += 1

                else:
                    return "You can not pick this up, it is too heavy for you to carry it around.", look_used

            elif action[0] == "drop":

                action_details = ""
                for i in range(1, len(action)):
                    action_details = action_details + action[i] + " "

                action = [action[0], action_details.rstrip(" ")]

                if action[1] in items_list:

                    item_index = 0
                    for product in items:

                        if action[1] == product.name.lower():

                            if len(player.inventory) != 0:
                                for item in player.inventory:

                                    if action[1] == item.lower():

                                        if product.start != int(position.index):
                                            product.start = int(position.index)

                                        player.remove_item(items[item_index].name)
                                        player.moves += 1

                                        split_long = position.long.split(". ")

                                        if action[1] == "lucky pen":
                                            split_long.insert(2, lucky_pen)

                                        elif action[1] == "t-card":
                                            split_long.insert(2, tcard)

                                        elif action[1] == "cheat sheet":
                                            split_long.insert(2, cheat_sheet)

                                        new_long = ". ".join(split_long)
                                        position.long = new_long

                                        return "You dropped {0}.".format(items[item_index].name), look_used

                                    else:
                                        return "{0} is not in your inventory.".format(items[item_index].name), look_used
                            else:
                                return "{0} is not in your inventory.".format(items[item_index].name), look_used

                        else:
                            item_index += 1

                else:
                    return "{0} is not in your inventory.".format(action[1]), look_used

            else:
                return "[menu]", look_used

        else:
            return "[menu]", look_used

    def unlock(self, combo):
        '''
        Checks to see if the player's input is correct lock combo.
        Returns whether of not lock combo is correct to unlock the exam room
        :param combo: The lock combo that the player guessed
        :return: True if lock got unlocked, False otherwise.
        '''

        if combo == "6-4-9":
            return True

        else:
            return False
