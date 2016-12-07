import random
from adven import *

game = Game("Monument 14")

#locations
bus = game.new_location("School Bus {n, e},""You and 13 other students survived the crash, and have safely climbed out.")
doors = game.new_location("Front Doors {e},""You walk up to the front doors of the Superstore, but you are unable to see inside because it is pitch black.")
store = game.new_location("Superstore {n, e, w},""You walk up to the store doors and look inside, but there are no lights on inside. You pull the handle on the door, and it opens. A student finds a light switch and flips it on, and you find that the store has everything you need to survive.")
inside_store = game.new_location("Main Entrance {w, n},""You and your fellow students walk further into the store. The younger kids are still freaking out due to the crash, so a couple other older students walk them over to the kitchen and make pizza and slushies to calm them down.")
kitchen = game.new_location("Pizza Shack {s},""You feel a huge temperature change as you walk into the pizza shack. You see the kids scattered all around the room eating their slushies and pizza. You notices that most of them have made a mess on their face. Typical.")
athletics = game.new_location("Sports Section {n, e},""Walking into the sports section of the store, you can see Jake and Brayden in there. You look around and you can see several beer bottles scattered across the floor. Jake notices you at the room entrance, and he offers you a bottle..\nYou look on some of the shelves and find several small bottles of steroids, some of them partially empty.")
cafe = game.new_location("Cafeteria {e},""You walk into the room that used to be an isle in the store, but was turned into a cafe by some of the students. Tables have been formed by short shelves and chairs are pillows or bean bags that were found somewhere in the store.")
attic = game.new_location("Astrid's Space {up},""You look up and see a lamp, a stack of books and a few blankets in the attic. There is a ladder leading up. Is this where Astrid has been hiding?")
storage = game.new_location("Storage Room {w},""You open a door and find yourself in an enormous storage room. Inside you find a ton of items, but the gas masks, flashlights, and walkie talkies catch your eye.")
dorms = game.new_location("Dorm Rooms {w},""You walk into the hallway with several different doors. Inside the doors are bedrooms assigned to specific people, mine included. Around the corner, you see a larger area with blankets and pillows set up for the younger kids.")
outside = game.new_location("Outside of Store {e, w},""You look around at the entrance of the store. Above you, the store's name is partially lit up with lights, but some of the lights have died.\n The stores looks like new, but there are zero cars nearby.")
bus2 = game.new_location("Broken Down Bus {e, n},""You walk over to the school bus, and all you can notice is the damage. The metal has been severely dented, and there is still smoke coming out from the engine. Unless Mrs. Wooly comes back with help, we'll be stuck here.)



#connections
game.new_connection("inside_store", kitchen, athletics [NORTH], [WEST])
game.new_connection("athletics", cafe, attic [NORTH], [EAST])
game.new_connection("doors", inside_store [EAST])
game.new_connection("cafe", dorms [EAST])
game.new_connection("store", doors, inside_store [EAST], [WEST], [NORTH])
game.new_connection("attic", cafe [UP], [WEST])
game.new_connection("bus", doors, superstore [EAST])
game.new_connection("outside", doors [EAST])
game.new_connection("kitchen", inside_store [SOUTH])
game.new_connection("dorms", cafe [EAST], [WEST])
game.new_connection("bus2", doors [EAST], [NORTH])
game.new_connection("storage", cafe [WEST])



#items
flashlight = storage.new_object("flashlights", "Several small black flashlights. These could in handy.")
gas_mask = storage.new_object("gas masks", "You look over and see several gas masks laying on a large shelf on the other side of the room. These will be much needed.")
walkie_talkie = storage.new_object("walkie talkie", "Next to the gas masks, you see about 7 walkie talkies. These will be useful for the older students.")
steriods = athletics.new_object("bottle of steriods", "You pick up a tiny bottle containing steriods. You shouldn't be taking this, but you decide to take it with you anyway.")
pistol = storage.new_object("pistol", "On one of the far shelves, you find a pistol hidden behind a a pile of items. You don't know how or why it got in a superstore, but you take with you for safe keeping.")



#NPC Characters
robbie = Animal("Robbie")
robbie.set_location(doors)
appleton.set_allowed_locations = ([doors])
game.add_actor(robbie)

appleton = Animal("Mr. Appleton")
appleton.set_location(doors)
appleton.set_allowed_locations = ([doors])
game.add_actor(appleton)



#Function to leave building
def open_door(game, thing):
    if not "gas_mask" in game.player.inventory and "walkie_talkie" in game.player.inventory:
        game.output("You walk outside of the building, and you instantly feel a rush of rage go through your veins.\n You are blood type O-negative, therefore if you are exposed to the air, you start to go mad.")
        player.terminate()
    if not "gas_mask" in game.player.inventory:
        game.output("This isn't a smart idea. Are you sure you aren't forgetting something?")
    else:
        game.output("You put on your gas mask and step outside. You can tell that the air is extremely thick, and outside, everything is severely damaged due to the hailstorm, and it is very dark.\n It would be best if you didn't wander far.")



#required items
doors.make_requirement(gas_mask)
outside.make_requirement(gas_mask, walkie_talkie)


#player
player = game.new_player(bus)

game.run()
