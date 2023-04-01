#!/bin/python3

#Game variables that can be changed!

#game background colour.
BACKGROUNDCOLOUR = 'ORANGE'

#map variables
MAPWIDTH  = 20
MAPHEIGHT = 10

#variables representing the different resources.
DIRT    = 0
GRASS   = 1
WATER   = 2
BRICK   = 3
WOOD    = 4
SAND    = 5
PLANK   = 6
GLASS   = 7

#a list of all game resources.
resources = [DIRT,GRASS,WATER,BRICK,WOOD,SAND,PLANK,GLASS]

#the names of the resources.
names = {
  DIRT    : 'dirt',
  GRASS   : 'grass',
  WATER   : 'water',
  BRICK   : 'brick',
  WOOD    : 'wood',
  SAND    : 'sand',
  PLANK   : 'plank',
  GLASS   : 'glass'
}

#a dictionary linking resources to images.
textures = {
  DIRT    : 'dirt.gif',
  GRASS   : 'grass.gif',
  WATER   : 'water.gif',
  BRICK   : 'brick.gif',
  WOOD    : 'wood.gif',
  SAND    : 'sand.gif',
  PLANK   : 'plank.gif',
  GLASS   : 'glass.gif'
}

#the player image.
playerImg = 'player.gif'

#the player position.
playerX = 1
playerY = 1

goal = False

#game instructions that are displayed.
instructions =  [
  'Instructions:',
  'Use WASD to move',
  'Escape the maze!',
  'Press E to escape automatically'
]
