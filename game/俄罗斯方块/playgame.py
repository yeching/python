#coding=utf-8
import pygame
from pygame.locals import *
import sys
import random
import time
from  constant import *#note that
def main():
	global FPSCLOCK, DISPLAYSURF, BASICFONT, BIGFONT#注意变量范围
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
	BIGFONT = pygame.font.Font('freesansbold.ttf', 100)
	pygame.display.set_caption('Tetromino')
	showTextScreen('Tetromino')
	while 1:
		if random.randint(0, 1) == 0:
			pygame.mixer.music.load('tetrisb.mid')
		else:
			pygame.mixer.music.load('tetrisc.mid')
		pygame.mixer.music.play(-1, 0.0)
		DISPLAYSURF.fill(BGCOLOR)
		pygame.display.update()
		
		runGame()
		showTextScreen('Game Over')
def runGame():
	# setup variables for the start of the game
	board = getBlankBoard()
	score = 0
	level, fallFreq = calculateLevelAndFallFreq(score)#fallFreq表示piece每移动一下的时间
	lastFallTime = time.time() #方块自由落下时，前后落下相间隔的时间
	lastMoveDownTime = time.time()#前后两次按下向下键的时间间隔
	lastMoveSidewaysTime = time.time()#前后两次按下向两边的时间间隔
	movingDown = False # note: there is no movingUp variable
	movingLeft = False
	movingRight = False
	fallingPiece = getNewPiece()
	nextPiece = getNewPiece()
	while 1:
		checkForQuit()
		if fallingPiece==None:
			fallingPiece=nextPiece
			nextPiece=getNewPiece()
			lastFallTime=time.time()# reset lastFallTime  
			if not isValidPosition(board,fallingPiece):
				return # can't fit a new piece on the board, so game over
		for event in pygame.event.get(): # event handling loop
			if event.type==KEYUP:
				if (event.key==K_p):
					#pause the game防止游戏者停下思考，所以画上背景
					DISPLAYSURF.fill(BGCOLOR)
					showTextScreen('Don\'t Cheat !')# pause until a key press  
					lastFallTime=time.time()
					lastMoveDownTime=time.time()
					lastMoveSidewaysTime=time.time()
				#停止按下方向键或ASD键会把moveLeft,moveRight,movingDown变量设置为False.,表明游戏者不再想要在此方向上移动方块
				elif (event.key==K_LEFT or event.key==K_a):
					movingLeft=False
				elif (event.key==K_RIGHT or event.key==K_d):
					movingRight=False
				elif (event.key==K_DOWN or event.key==K_s):
					movingDown=False
			elif event.type==KEYDOWN:
				# moving the piece sideways
				if (event.key==K_LEFT  or event.key==K_a) and isValidPosition(board,fallingPiece,adjX=-1):
					fallingPiece['x']-=1
					movingLeft=True
					movingRight=False
					lastMoveSidewaysTime=time.time()
				elif (event.key == K_RIGHT or event.key == K_d) and isValidPosition(board, fallingPiece, adjX=1):
					fallingPiece['x'] += 1
					movingRight = True
					movingLeft = False
					lastMoveSidewaysTime = time.time()
				# rotating the piece (if there is room to rotate)
				elif (event.key==K_UP or event.key==K_w) :
					fallingPiece['rotation']=(fallingPiece['rotation']+1)%len(PIECES[fallingPiece['shape']])
					if not isValidPosition(board,fallingPiece):
						fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(PIECES[fallingPiece['shape']])
				elif (event.key == K_q): # rotate the other direction
					fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(PIECES[fallingPiece['shape']])
					if not isValidPosition(board, fallingPiece):
						fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(PIECES[fallingPiece['shape']])
				# making the piece fall faster with the down key
				elif (event.key == K_DOWN or event.key == K_s):
					movingDown = True
					if isValidPosition(board, fallingPiece, adjY=1):
						fallingPiece['y'] += 1
					lastMoveDownTime = time.time()
				# move the current piece all the way down
				elif event.key == K_SPACE:
					movingDown = False
					movingLeft = False
					movingRight = False
					for i in range(1, BOARDHEIGHT):
						if not isValidPosition(board, fallingPiece, adjY=i):
							break
					fallingPiece['y'] += i - 1
		# handle moving the piece because of user input
		#下面是处理用户一直按下某个键的程序
		if (movingLeft or movingRight) and time.time() - lastMoveSidewaysTime > MOVESIDEWAYSFREQ:
			if movingLeft and isValidPosition(board, fallingPiece, adjX=-1):
				fallingPiece['x'] -= 1
			elif movingRight and isValidPosition(board, fallingPiece, adjX=1):
				fallingPiece['x'] += 1
			lastMoveSidewaysTime = time.time()

		if movingDown and time.time() - lastMoveDownTime > MOVEDOWNFREQ and isValidPosition(board, fallingPiece, adjY=1):
			fallingPiece['y'] += 1
			lastMoveDownTime = time.time()
		# let the piece fall if it is time to fall
		if time.time() - lastFallTime > fallFreq:
			#print int(time.time()-lastFallTime)
			# see if the piece has landed
			if not isValidPosition(board, fallingPiece, adjY=1):
				# falling piece has landed, set it on the board
				addToBoard(board, fallingPiece)#landed时固定到board上面,
				score += removeCompleteLines(board)
				level, fallFreq = calculateLevelAndFallFreq(score)
				fallingPiece = None
			else:
				# piece did not land, just move the piece down
				fallingPiece['y'] += 1
				lastFallTime = time.time()
		# drawing everything on the screen
		DISPLAYSURF.fill(BGCOLOR)
		drawBoard(board)
		drawStatus(score, level)
		drawNextPiece(nextPiece)
		if fallingPiece!=None:
			drawPiece(fallingPiece)
		pygame.display.update()
		FPSCLOCK.tick(FPS)
def checkForKeyPress():
	# Go through event queue looking for a KEYUP event.
	# Grab KEYDOWN events to remove them from the event queue.
	checkForQuit()

	for event in pygame.event.get([KEYDOWN, KEYUP]):#KEYDOWN要不要都行
		if event.type == KEYDOWN:                    #note that KEYUP KEYDOWN events
			continue
		return event.key
	return None
def makeTextObjs(text, font, color):
	surf = font.render(text, True, color)
	return surf, surf.get_rect()

def showTextScreen(text):
	# This function displays large text in the
	# center of the screen until a key is pressed.
	# Draw the text drop shadow
	titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTSHADOWCOLOR)
	titleRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))#代表字体显示位置
	DISPLAYSURF.blit(titleSurf, titleRect)#titleRect换成坐标也行

	# Draw the text
	#在不同位置画同一个字体界面，看上去好像有阴影存在，形成立体的感觉
	titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTCOLOR)
	titleRect.center = (int(WINDOWWIDTH / 2) - 3, int(WINDOWHEIGHT / 2) - 3)
	DISPLAYSURF.blit(titleSurf, titleRect)

	#Draw the additional "Press a key to play." text.
	pressKeySurf, pressKeyRect = makeTextObjs('Press a key to play.', BASICFONT, TEXTCOLOR)
	pressKeyRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2) + 100)
	DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

	while checkForKeyPress() == None:
		pygame.display.update()
		FPSCLOCK.tick()
def terminate():
	pygame.quit()
	sys.exit()
def checkForQuit():
	for event in pygame.event.get(QUIT): # get all the QUIT events
		terminate() # terminate if any QUIT events are present
	for event in pygame.event.get(KEYUP): # get all the KEYUP events
		if event.key == K_ESCAPE:
			terminate() # terminate if the KEYUP event was for the Esc key
		pygame.event.post(event) # put the other KEYUP event objects back
def isOnBoard(x, y):
	return x >= 0 and x < BOARDWIDTH and y < BOARDHEIGHT
def isValidPosition(board, piece, adjX=0, adjY=0):#adjX表示偏离当前方向的位置，比如adjX=-1，则表示向左移动一个格子后方块的位置
	# Return True if the piece is within the board and not colliding
	for x in range(TEMPLATEWIDTH):
		for y in range(TEMPLATEHEIGHT):
			isAboveBoard = y + piece['y'] + adjY < 0
			if isAboveBoard or PIECES[piece['shape']][piece['rotation']][y][x] == BLANK:
				continue
			if not isOnBoard(x + piece['x'] + adjX, y + piece['y'] + adjY):
				return False
			if board[x + piece['x'] + adjX][y + piece['y'] + adjY] != BLANK:
				return False
	return True
#上面有关于return。continue 的用法
def isCompleteLine(board, y):
	# Return True if the line filled with boxes with no gaps.
	for x in range(BOARDWIDTH):
		if board[x][y] == BLANK:
			return False
	return True


def removeCompleteLines(board):
	# Remove any completed lines on the board, move everything above them down, and return the number of complete lines.
	numLinesRemoved = 0
	y = BOARDHEIGHT - 1 # start y at the bottom of the board
	while y >= 0:
		if isCompleteLine(board, y):
			# Remove the line and pull boxes down by one line.
			for pullDownY in range(y, 0, -1):#pullDownY=[y,y-1,y-2,...,1]
				for x in range(BOARDWIDTH):
					board[x][pullDownY] = board[x][pullDownY-1]
			# Set very top line to blank.
			for x in range(BOARDWIDTH):
				board[x][0] = BLANK
			numLinesRemoved += 1
			# Note on the next iteration of the loop, y is the same.
			# This is so that if the line that was pulled down is also
			# complete, it will be removed.
		else:
			y -= 1 # move on to check next row up
	return numLinesRemoved
def getBlankBoard():
	# create and return a new blank board data structure
	board = []
	for i in range(BOARDWIDTH):
		board.append([BLANK] * BOARDHEIGHT)#=[[['.']*20]*10]得到一个board[10][20]二维列表
	return board
def convertToPixelCoords(boxx, boxy):
	# Convert the given xy coordinates of the board to xy
	# coordinates of the location on the screen.
	return (XMARGIN + (boxx * BOXSIZE)), (TOPMARGIN + (boxy * BOXSIZE))
def drawBox(boxx, boxy, color, pixelx=None, pixely=None):
	# draw a single box (each tetromino piece has four boxes)
	# at xy coordinates on the board. Or, if pixelx & pixely
	# are specified, draw to the pixel coordinates stored in
	# pixelx & pixely (this is used for the "Next" piece).
	if color == BLANK:
		return
	if pixelx == None and pixely == None:
		pixelx, pixely = convertToPixelCoords(boxx, boxy)
	pygame.draw.rect(DISPLAYSURF, COLORS[color], (pixelx + 1, pixely + 1, BOXSIZE - 1, BOXSIZE - 1))
	
	pygame.draw.rect(DISPLAYSURF, LIGHTCOLORS[color], (pixelx + 1, pixely + 1, BOXSIZE - 4, BOXSIZE - 4))
	#在box周围在画一个颜色较浅的，形成一定的阴影，使其看起来有立体的感觉


def drawBoard(board):
	# draw the border around the board
	pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (XMARGIN , TOPMARGIN , (BOARDWIDTH * BOXSIZE) , (BOARDHEIGHT * BOXSIZE) ), 5)

	# fill the background of the board
	#pygame.draw.rect(DISPLAYSURF, BGCOLOR, (XMARGIN, TOPMARGIN, BOXSIZE * BOARDWIDTH, BOXSIZE * BOARDHEIGHT))
	# draw the individual boxes on the board
	for x in range(BOARDWIDTH):
		for y in range(BOARDHEIGHT):
			drawBox(x, y, board[x][y])
def calculateLevelAndFallFreq(score):
	# Based on the score, return the level the player is on and
	# how many seconds pass until a falling piece falls one space.
	level = int(score / 10) + 1
	fallFreq = 0.27 - (level * 0.02)
	return level, fallFreq
def drawStatus(score, level):
	# draw the score text
	scoreSurf = BASICFONT.render('Score: %s' % score, True, TEXTCOLOR)
	scoreRect = scoreSurf.get_rect()
	scoreRect.topleft = (WINDOWWIDTH - 150, 20)
	DISPLAYSURF.blit(scoreSurf, scoreRect)

	# draw the level text
	levelSurf = BASICFONT.render('Level: %s' % level, True, TEXTCOLOR)
	levelRect = levelSurf.get_rect()
	levelRect.topleft = (WINDOWWIDTH - 150, 50)
	DISPLAYSURF.blit(levelSurf, levelRect)
def getNewPiece():
	# return a random new piece in a random rotation and color
	shape = random.choice(list(PIECES.keys()))#获得任意一个形状
	newPiece = {'shape': shape,
				'rotation': random.randint(0, len(PIECES[shape]) - 1),#获得任意形状的任意旋转图形，除去本身的一个
				'x': int(BOARDWIDTH / 2) - int(TEMPLATEWIDTH / 2),    #randint(x,y)代表取其范围内的一个值
				'y': -3, # start it above the board (i.e. less than 0)
				'color': random.randint(0, len(COLORS)-1)}
	return newPiece


def addToBoard(board, piece):
	# fill in the board based on piece's location, shape, and rotation
	for x in range(TEMPLATEWIDTH):
		for y in range(TEMPLATEHEIGHT):
			if PIECES[piece['shape']][piece['rotation']][y][x] != BLANK:
				#给piece中的小块上色，+piece是为了获得快的确切位置
				board[x + piece['x']][y + piece['y']] = piece['color']
def drawPiece(piece, pixelx=None, pixely=None):
	shapeToDraw = PIECES[piece['shape']][piece['rotation']]
	if pixelx == None and pixely == None:
		# if pixelx & pixely hasn't been specified, use the location stored in the piece data structure
		pixelx, pixely = convertToPixelCoords(piece['x'], piece['y'])

	# draw each of the boxes that make up the piece
	for x in range(TEMPLATEWIDTH):
		for y in range(TEMPLATEHEIGHT):
			if shapeToDraw[y][x] != BLANK:
				drawBox(None, None, piece['color'], pixelx + (x * BOXSIZE), pixely + (y * BOXSIZE))


def drawNextPiece(piece):
	# draw the "next" text
	nextSurf = BASICFONT.render('Next:', True, TEXTCOLOR)
	nextRect = nextSurf.get_rect()
	nextRect.topleft = (WINDOWWIDTH - 120, 80)
	DISPLAYSURF.blit(nextSurf, nextRect)
	# draw the "next" piece
	drawPiece(piece, pixelx=WINDOWWIDTH-120, pixely=100)

if __name__=='__main__':
	main()