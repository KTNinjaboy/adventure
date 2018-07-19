from game_data import World, Item, Location
from player import Player

if __name__ == "__main__":
    WORLD = World("map.txt", "locations.txt", "items.txt")
    PLAYER = Player(2, 4) # set starting location of player; you may change the x, y coordinates here as appropriate

    menu = ["look", "inventory", "score", "quit"]
    max_moves = 20

    look_used = False
    locked = True
    Guessing_lock = False

    print('''You studied in IB for all of last night and are certain that your belongings are in there. You get dropped off in front of IB by your parents around 2:00PM, a busy time for the university.
The university is packed with people, you see people walking to their classes and socializing. As you enter IB, you happen to notice people studying through the windows on the left.
You enter IB. Only to come to the shock that... its completely empty. As you look around you also notice that all windows,entrances, and exits have turned into red brick.
Leaving no way out. Your exam is in this building but in order to write it you must find your T-card, Lucky Pen, and Cheat Sheet.''')

    print("")

    while not PLAYER.victory:
        location = WORLD.get_location(PLAYER.x, PLAYER.y)

        if location is not None:
            if location.times_visited == 0:
                location.times_visited += 1
                print(location.long)

            else:
                if location != location:
                    location.times_visited += 1
                if not look_used:
                    print(location.brief)
                look_used = False

        print("Times Visited: {0}".format(location.times_visited))
        print("Moves: {0}".format(PLAYER.moves))

        print("What to do? \n")
        print("[menu]")

        for action in location.available_actions():
            print(action)

        for product in WORLD.items:
            if product.start == int(location.index):
                print("pickup")

        if len(PLAYER.inventory) != 0:
            print("drop")

        choice = input("\nEnter action: ")

        if choice == "[menu]":
            print("Menu Options: \n")
            for option in menu:
                print(option)
            choice = input("\nChoose action: ")

        (result, look_used) = WORLD.do_action(PLAYER, location, WORLD.items, choice.lower(), look_used)

        if result == "GAME OVER!!!" or PLAYER.moves == max_moves:
            print("You gave up on finding your materials required to enter and write the exam.\nYou bombed the exam.")
            print(result)
            break

        elif result == "There seems to be a lock to get into the exam room. It's a lock with a 3-digit code. (HINT: The numbers were on pieces of paper throughout the building)":
            print(result)
            Guessing_lock = True
            while locked:

                if PLAYER.moves >= max_moves:
                    print("\nYou failed to win the game within {0} moves. You bombed the test...".format(max_moves))
                    print("GAME OVER!!!")
                    break

                choice = input("\nEnter 3 digit code (x-x-x): ")

                guess = WORLD.unlock(choice)
                PLAYER.moves += 1

                if guess:
                    PLAYER.victory = True
                    PLAYER.score += 15
                    print("You have won the game! Now good luck on your exam!")
                    locked = False

            break

        elif Guessing_lock:
            break

        else:
            print(result)

    print("Final score: {0}".format(PLAYER.score))
    print("Total moves: {0}".format(PLAYER.moves))


