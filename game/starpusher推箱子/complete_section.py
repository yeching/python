#coding=utf-8
import random, sys, copy, os, pygame
from pygame.locals import *

#constants
FPS = 30	# frames per second to update the screen
WINWIDTH = 800
WINHEIGHT = 600
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)

TILEWIDTH = 50
TILEHEIGHT = 85
TILEFLOORHEIGHT = 45

CAM_MOVE_SPEED = 5

OUTSIDE_DECORATION_PCT = 20

BRIGHTBLUE = ( 0, 170, 255)
WHITE = (255, 255, 255)
BGCOLOR = BRIGHTBLUE
TEXTCOLOR = WHITE

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
def main():
  global FPSCLOCK, DISPLAYSURF, IMAGESDICT, TILEMAPPING, OUTSIDEDECOMAPPING, BASICFONT, PLAYERIMAGES, currentImage
  pygame.init()
  FPSCLOCK = pygame.time.Clock()
  
  DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
  pygame.display.set_caption('推箱子')
  BASICFONT = pygame.font.Font(None,18)


  #一个全局字典包含所有图片
  IMAGESDICT = {'uncovered goal': pygame.image.load('RedSelector.png'),
               "covered goal": pygame.image.load('Selector.png'),
               'star': pygame.image.load('Star.png'),
               'corner': pygame.image.load('Wall_Block_Tall.png'),
               'wall': pygame.image.load('Wood_Block_Tall.png'),
               'inside floor': pygame.image.load('Plain_Block.png'),
               'outside floor': pygame.image.load('Grass_Block.png'),
               'title': pygame.image.load('star_title.png'),
               'solved': pygame.image.load('star_solved.png'),
               'princess': pygame.image.load('princess.png'),
               'boy': pygame.image.load('boy.png'),
               'catgirl': pygame.image.load('catgirl.png'),
               'horngirl': pygame.image.load('horngirl.png'),
               'pinkgirl': pygame.image.load('pinkgirl.png'),
               'rock': pygame.image.load('Rock.png'),
               'short tree': pygame.image.load('Tree_Short.png'),
               'tall tree': pygame.image.load('Tree_Tall.png'),
               'ugly tree': pygame.image.load('Tree_Ugly.png') }

  TILEMAPPING = {'x': IMAGESDICT['corner'],
                 '#': IMAGESDICT['wall'],
                 'o': IMAGESDICT['inside floor'],
                 ' ': IMAGESDICT['outside floor']}

  OUTSIDEDECOMAPPING = {'1': IMAGESDICT['rock'],
                        '2': IMAGESDICT['short tree'],
                        '3': IMAGESDICT['tall tree'],
                        '4': IMAGESDICT['ugly tree'] }

  currentImage = 0
  PLAYERIMAGES = [IMAGESDICT['princess'],
                  IMAGESDICT['boy'],
                  IMAGESDICT['catgirl'],
                  IMAGESDICT['horngirl'],
                  IMAGESDICT['pinkgirl']]
  DISPLAYSURF.fill(BGCOLOR)
  while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT: 
          sys.exit()
      pygame.display.flip()
if __name__ == "__main__":
  main()


----------------------------------------------
#coding=utf-8
import random, sys, copy, os, pygame
from pygame.locals import *

#constants
FPS = 30	# frames per second to update the screen
WINWIDTH = 800
WINHEIGHT = 600
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)

TILEWIDTH = 50
TILEHEIGHT = 85
TILEFLOORHEIGHT = 45

CAM_MOVE_SPEED = 5

OUTSIDE_DECORATION_PCT = 20

BRIGHTBLUE = ( 0, 170, 255)
WHITE = (255, 255, 255)
BGCOLOR = BRIGHTBLUE
TEXTCOLOR = WHITE

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
def main():
  global FPSCLOCK, DISPLAYSURF, IMAGESDICT, TILEMAPPING, OUTSIDEDECOMAPPING, BASICFONT, PLAYERIMAGES, currentImage
  pygame.init()
  FPSCLOCK = pygame.time.Clock()
  
  DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
  pygame.display.set_caption('推箱子')
  BASICFONT = pygame.font.Font(None,18)


  #一个全局字典包含所有图片
  IMAGESDICT = {'uncovered goal': pygame.image.load('RedSelector.png'),
               "covered goal": pygame.image.load('Selector.png'),
               'star': pygame.image.load('Star.png'),
               'corner': pygame.image.load('Wall_Block_Tall.png'),
               'wall': pygame.image.load('Wood_Block_Tall.png'),
               'inside floor': pygame.image.load('Plain_Block.png'),
               'outside floor': pygame.image.load('Grass_Block.png'),
               'title': pygame.image.load('star_title.png'),
               'solved': pygame.image.load('star_solved.png'),
               'princess': pygame.image.load('princess.png'),
               'boy': pygame.image.load('boy.png'),
               'catgirl': pygame.image.load('catgirl.png'),
               'horngirl': pygame.image.load('horngirl.png'),
               'pinkgirl': pygame.image.load('pinkgirl.png'),
               'rock': pygame.image.load('Rock.png'),
               'short tree': pygame.image.load('Tree_Short.png'),
               'tall tree': pygame.image.load('Tree_Tall.png'),
               'ugly tree': pygame.image.load('Tree_Ugly.png') }

  TILEMAPPING = {'x': IMAGESDICT['corner'],
                 '#': IMAGESDICT['wall'],
                 'o': IMAGESDICT['inside floor'],
                 ' ': IMAGESDICT['outside floor']}

  OUTSIDEDECOMAPPING = {'1': IMAGESDICT['rock'],
                        '2': IMAGESDICT['short tree'],
                        '3': IMAGESDICT['tall tree'],
                        '4': IMAGESDICT['ugly tree'] }

  currentImage = 0
  PLAYERIMAGES = [IMAGESDICT['princess'],
                  IMAGESDICT['boy'],
                  IMAGESDICT['catgirl'],
                  IMAGESDICT['horngirl'],
                  IMAGESDICT['pinkgirl']]
  DISPLAYSURF.fill(BGCOLOR)
  level = readLevelsFile("starPusherLevels.txt")
  mp=drawMap(level[0]['mapObj'],level[0]['startState'], level[0]['goals'])

  while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT: 
          sys.exit()
      DISPLAYSURF.fill(BGCOLOR)
      DISPLAYSURF.blit(mp,(100,100))
      pygame.display.flip()

def readLevelsFile(filename):
    assert os.path.exists(filename), 'Cannot find the level file: %s' % (filename)
    mapFile = open(filename, 'r')
    # Each level must end with a blank line
    content = mapFile.readlines() + ['\r\n']
    mapFile.close()

    levels = [] # Will contain a list of level objects.
    levelNum = 0
    mapTextLines = [] # contains the lines for a single level's map.
    mapObj = [] # the map object made from the data in mapTextLines
    for lineNum in range(len(content)):
        # Process each line that was in the level file.
        line = content[lineNum].rstrip('\r\n')

        if ';' in line:
            # Ignore the ; lines, they're comments in the level file.
            line = line[:line.find(';')]

        if line != '':
            # This line is part of the map.
            mapTextLines.append(line)
        elif line == '' and len(mapTextLines) > 0:
            # A blank line indicates the end of a level's map in the file.
            # Convert the text in mapTextLines into a level object.

            # Find the longest row in the map.
            maxWidth = -1
            for i in range(len(mapTextLines)):
                if len(mapTextLines[i]) > maxWidth:
                    maxWidth = len(mapTextLines[i])
            # Add spaces to the ends of the shorter rows. This
            # ensures the map will be rectangular.
            for i in range(len(mapTextLines)):
                mapTextLines[i] += ' ' * (maxWidth - len(mapTextLines[i]))

            # Convert mapTextLines to a map object.
            for x in range(len(mapTextLines[0])):
                mapObj.append([])
            for y in range(len(mapTextLines)):
                for x in range(maxWidth):
                    mapObj[x].append(mapTextLines[y][x])
            # Loop through the spaces in the map and find the @, ., and $
            # characters for the starting game state.
            startx = None # The x and y for the player's starting position
            starty = None
            goals = [] # list of (x, y) tuples for each goal.
            stars = [] # list of (x, y) for each star's starting position.
            for x in range(maxWidth):
                for y in range(len(mapObj[x])):
                    if mapObj[x][y] in ('@', '+'):
                        # '@' is player, '+' is player & goal
                        startx = x
                        starty = y
                    if mapObj[x][y] in ('.', '+', '*'):
                        # '.' is goal, '*' is star & goal
                        goals.append((x, y))
                    if mapObj[x][y] in ('$', '*'):
                        # '$' is star
                        stars.append((x, y))

            # Basic level design sanity checks:
            assert startx != None and starty != None, 'Level %s (around line %s) in %s is missing a "@" or "+" to mark the start point.' % (levelNum+1, lineNum, filename)
            assert len(goals) > 0, 'Level %s (around line %s) in %s must have at least one goal.' % (levelNum+1, lineNum, filename)
            assert len(stars) >= len(goals), 'Level %s (around line %s) in %s is impossible to solve. It has %s goals but only %s stars.' % (levelNum+1, lineNum, filename, len(goals), len(stars))

            # Create level object and starting game state object.
            gameStateObj = {'player': (startx, starty),
                            'stepCounter': 0,
                            'stars': stars}
            levelObj = {'width': maxWidth,#本程序没用到  好像有错误
                        'height': len(mapObj),#本程序没用到
                        'mapObj': mapObj,
                        'goals': goals,
                        'startState': gameStateObj}

            levels.append(levelObj)

            # Reset the variables for reading the next map.
            mapTextLines = []
            mapObj = []
            gameStateObj = {}
            levelNum += 1
    
    return levels

def drawMap(mapObj, gameStateObj, goals):
    """Draws the map to a Surface object, including the player and
    stars. This function does not call pygame.display.update(), nor
    does it draw the "Level" and "Steps" text in the corner."""

    # mapSurf will be the single Surface object that the tiles are drawn
    # on, so that it is easy to position the entire map on the DISPLAYSURF
    # Surface object. First, the width and height must be calculated.
    mapSurfWidth = len(mapObj) * TILEWIDTH
    mapSurfHeight = (len(mapObj[0]) - 1) * TILEFLOORHEIGHT + TILEHEIGHT
    mapSurf = pygame.Surface((mapSurfWidth, mapSurfHeight))
    mapSurf.fill(BGCOLOR) # start with a blank color on the surface.

    # Draw the tile sprites onto this surface.
    for x in range(len(mapObj)):
        for y in range(len(mapObj[x])):
            spaceRect = pygame.Rect((x * TILEWIDTH, y * TILEFLOORHEIGHT, TILEWIDTH, TILEHEIGHT))
            if mapObj[x][y] in TILEMAPPING:
                baseTile = TILEMAPPING[mapObj[x][y]]
            elif mapObj[x][y] in OUTSIDEDECOMAPPING:
                baseTile = TILEMAPPING[' ']

            # First draw the base ground/wall tile.
            mapSurf.blit(baseTile, spaceRect)

            if mapObj[x][y] in OUTSIDEDECOMAPPING:
                # Draw any tree/rock decorations that are on this tile.
                mapSurf.blit(OUTSIDEDECOMAPPING[mapObj[x][y]], spaceRect)
            elif (x, y) in gameStateObj['stars']:
                if (x, y) in goals:
                    # A goal AND star are on this space, draw goal first.
                    mapSurf.blit(IMAGESDICT['covered goal'], spaceRect)
                # Then draw the star sprite.
                mapSurf.blit(IMAGESDICT['star'], spaceRect)
            elif (x, y) in goals:
                # Draw a goal without a star on it.
                mapSurf.blit(IMAGESDICT['uncovered goal'], spaceRect)

            # Last draw the player on the board.
            if (x, y) == gameStateObj['player']:
                # Note: The value "currentImage" refers
                # to a key in "PLAYERIMAGES" which has the
                # specific player image we want to show.
                mapSurf.blit(PLAYERIMAGES[currentImage], spaceRect)

    return mapSurf

if __name__ == "__main__":
  main()
