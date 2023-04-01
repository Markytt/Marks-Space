#!/bin/python3

#############
# CodeCraft # 
#############

#---
#Game functions
#---

#moves the player left 1 tile.
def moveLeft():
  global playerX, playerY
  if(drawing == False and playerX > 0):
    for row in range(playerY, playerY+1):
      for column in range(playerX-1,playerX):
        if(world[column][row] != GLASS):
          oldX = playerX
          playerX -= 1
          drawResource(oldX, playerY)
          drawResource(playerX, playerY)
          
#moves the player right 1 tile.
def moveRight():
  global playerX, MAPWIDTH, playerY, goal
  if(drawing == False and playerX < MAPWIDTH - 1):
    for row in range(playerY, playerY+1):
      for column in range(playerX+1,playerX+2):
        if(world[column][row] != GLASS):
          oldX = playerX
          playerX += 1
          drawResource(oldX, playerY)
          drawResource(playerX, playerY)
          return True 
        else:
          return False
  else:
    rendererT.goto( MAPWIDTH*TILESIZE + 40, height - 100)
    rendererT.write('Congraduations! You escaped.')
    goal = True
    
#moves the player up 1 tile.
def moveUp():
  global playerY, playerX
  if(drawing == False and playerY > 0):
    for row in range(playerY-1, playerY):
      for column in range(playerX,playerX+1):
        if(world[column][row] != GLASS):
          oldY = playerY
          playerY -= 1
          drawResource(playerX, oldY)
          drawResource(playerX, playerY)
    
#moves the player down 1 tile.
def moveDown():
  global playerY, MAPHEIGHT, playerX
  if(drawing == False and playerY < MAPHEIGHT - 1):
    for row in range(playerY+1, playerY+2):
      for column in range(playerX,playerX+1):
        if(world[column][row] != GLASS):
          oldY = playerY
          playerY += 1
          drawResource(playerX, oldY)
          drawResource(playerX, playerY)
          return True
        else:
          return False

#draws a resource at the position (y,x)
def drawResource(y, x):
  #this variable stops other stuff being drawn
  global drawing
  #only draw if nothing else is being drawn
  if drawing == False:
    #something is now being drawn
    drawing = True
    #draw the resource at that position in the tilemap, using the correct image
    rendererT.goto( (y * TILESIZE) + 20, height - (x * TILESIZE) - 20 )
    #draw tile with correct texture
    texture = textures[world[y][x]]
    rendererT.shape(texture)
    rendererT.stamp()
    if playerX == y and playerY == x:
      rendererT.shape(playerImg)
      rendererT.stamp()
    screen.update()
    #nothing is now being drawn
    drawing = False
    
#draws the world map
def drawWorld():
  #loop through each row
  for row in range(MAPHEIGHT):
    #loop through each column in the row
    for column in range(MAPWIDTH):
      #draw the tile at the current position
      drawResource(column, row)

#generate the instructions, including crafting rules
def generateInstructions():
  #display the instructions
  yPos = height - 20
  for item in instructions:
    rendererT.goto( MAPWIDTH*TILESIZE + 40, yPos)
    rendererT.write(item)
    yPos-=20

def travel(move,j):
  i = 0
  if move == 'down':
    while i < j:
      moveDown()
      i = i + 1
  if move == 'up':
    while i < j:
      moveUp()
      i = i + 1
  if move == 'right':
    while i < j:
      moveRight()
      i = i + 1
  if move == 'left':
    while i < j:
      moveLeft()
      i = i + 1
  
def automatic():
  travel('down',6)
  travel('right',2)
  travel('up',6)
  travel('right',6)
  travel('down',5)
  travel('left',2)
  travel('up',3)
  travel('left',2)
  travel('down',5)
  travel('right',6)
  travel('up',7)
  travel('right',5)
  travel('down',3)
  travel('left',2)
  travel('down',2)
  travel('right',4)
  travel('up',5)
  travel('right',2)

def generate(start, end, here, there, object):
  for row in range(start, end):
    for column in range(here, there):
      tile = object
      world[column][row] = tile
  
#generate a random world
def generateWorld():
  global goal, playerX, playerY
   #loop through each row
  for row in range(MAPHEIGHT):
    #loop through each column in that row
    for column in range(MAPWIDTH):
      tile = GLASS
      world[column][row] = tile
  for row in range(1,2):
    for column in range(1,2):
      tile = SAND
      world[column][row] = tile
  
  for row in range(1,MAPHEIGHT-2):
    for column in range(1,2):
      tile = SAND
      world[column][row] = tile
  for row in range(MAPHEIGHT-3, MAPHEIGHT -2):
    for column in range(2,4):
      tile = SAND
      world[column][row] = tile
  for row in range(1, MAPHEIGHT -3):
    for column in range(3,4):
      tile = SAND
      world[column][row] = tile
  for row in range(1,2):
    for column in range(4,10):
      tile = SAND
      world[column][row] = tile
  for row in range(2,7):
    for column in range(9,10):
      tile = SAND
      world[column][row] = tile
  for row in range(6,7):
    for column in range(7,9):
      tile = SAND
      world[column][row] = tile
  for row in range(3,6):
    for column in range(7,8):
      tile = SAND
      world[column][row] = tile
  for row in range(3,4):
    for column in range(5,7):
      tile = SAND
      world[column][row] = tile
  for row in range(4,MAPHEIGHT-1):
    for column in range(5,6):
      tile = SAND
      world[column][row] = tile
  for row in range(MAPHEIGHT-2, MAPHEIGHT-1):
    for column in range(5,12):
      tile = SAND
      world[column][row] = tile
  for row in range(1, MAPHEIGHT-2):
    for column in range(11,12):
      tile = SAND
      world[column][row] = tile
  for row in range(1,2):
    for column in range(12,17):
      tile = SAND
      world[column][row] = tile
  for row in range(2,5):
    for column in range(16,17):
      tile = SAND
      world[column][row] = tile
  for row in range(4,5):
    for column in range(14,16):
      tile = SAND
      world[column][row] = tile
  for row in range(5,7):
    for column in range(14,15):
      tile = SAND
      world[column][row] = tile
  for row in range(6,7):
    for column in range(15,19):
      tile = SAND
      world[column][row] = tile
  for row in range(1,6):
    for column in range(18,19):
      tile = SAND
      world[column][row] = tile
  for row in range(1,2):
    for column in range(19,20):
      tile = SAND
      world[column][row] = tile
  
  
  
  

#---
#Code starts running here
#---

#import the modules and variables needed
import turtle
import random
from variables import *
from math import ceil

TILESIZE = 20
#the number of inventory resources per row
INVWIDTH = 8
drawing = False

#create a new 'screen' object
screen = turtle.Screen()
#calculate the width and height
width = (TILESIZE * MAPWIDTH) + max(200,INVWIDTH * 50)
num_rows = int(ceil((len(resources) / INVWIDTH)))
inventory_height =  num_rows * 120 + 40
height = (TILESIZE * MAPHEIGHT) + inventory_height

screen.setup(width, height)
screen.setworldcoordinates(0,0,width,height)
screen.bgcolor(BACKGROUNDCOLOUR)
screen.listen()

#register the player image  
screen.register_shape(playerImg)
#register each of the resource images
for texture in textures.values():
  screen.register_shape(texture)

#create another turtle to do the graphics drawing
rendererT = turtle.Turtle()
rendererT.hideturtle()
rendererT.penup()
rendererT.speed(0)
rendererT.setheading(90)

#create a world of random resources.
world = [ [DIRT for w in range(MAPHEIGHT)] for h in range(MAPWIDTH) ]

#map the keys for moving and picking up to the correct functions.
screen.onkey(moveUp, 'w')
screen.onkey(moveDown, 's')
screen.onkey(moveLeft, 'a')
screen.onkey(moveRight, 'd')
screen.onkey(automatic, 'e')
# screen.onkey(pickUp, 'space')

#set up the keys for placing and crafting each resource
# bindPlacingKeys()
# bindCraftingKeys()

#these functions are defined above
generateWorld()
drawWorld()
generateInstructions()


