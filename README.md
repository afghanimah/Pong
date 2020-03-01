# Pong
Pong implemented in pyglet for learning purposes

Goal is to "over engineer" after it becomes playable

# Update:
After "over engineering" pong, I have developed a pyglet
extension library of sorts, so you can also use this repo
to see an example of how the pygletplus package is used with
a simple game like pong.  The game may be missing some things,
but it's complete overall and the extension package can be used
with pyglet to make multi-scene games easier to make.

# pygletplus
game.py has Game which is a scene manager.

scene.py has Scene which can be used to make your own custom
game scenes.  Scenes are controller managers.

controller.py has Controller which can be used as different states
for each scene.  Make custom controllers to have different
behaviours for input and update.

resourcemanager.py has ResourceManager which makes loading
resources easier.  It will assume there's a resources/ directory
to load from.

entity.py and physicalentity.py are used to represent objects
in the game world.  PhysicalEntity just adds velocity to the
base Entity class.
