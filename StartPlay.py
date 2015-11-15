import kivy
kivy.require("1.9.0")  #kivy version check

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Color
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton

popup = Popup(title='Game Type?', size_hint=(None,None), size=(600, 600), auto_dismiss=False)

global g_pieceToPlay
global g_player1
global g_player2
global g_playBoard

g_playBoard = [0]*17

# -- create tuple of tuples characterizing each individual piece
# -- each value is either a 0 or 1 (height, color, shape, top)
# -- short = 0;   tall = 1
# -- light = 0;   dark = 1
# -- square = 0;  circle = 1
# -- flat = 0;    hollow = 1
# -- i.e. a short, dark, square, flat piece would be (0, 1, 0, 0)
global pieceFeatures
pieceFeatures = [(1,1,1,1),(1,1,1,0),(0,1,1,1),(0,1,1,0),
						(1,1,0,1),(1,1,0,0),(0,1,0,1),(0,1,0,0),
						(1,0,1,1),(1,0,1,0),(0,0,1,1),(0,0,1,0),
						(1,0,0,1),(1,0,0,0),(0,0,0,1),(0,0,0,0)]

########################MAIN MENU#######################################
def MainMenu(instance):
	#print('The button <%s> is being pressed' % instance.text)
	window = instance.parent.parent
	window.clear_widgets()
	StartPlay().run()

#######################START GAME#######################################
def StartGame(instance):
	#print('inside StartGame with gameType= ', gameType)
	global gameMode
	# -- Holds reff to the pieceToPlay button
	# -- Used when a piece is selected
	global g_pieceToPlay
	global g_player1
	global g_player2
	global g_moveTrack
	g_moveTrack = 1
	global categories
	
	
	window = instance.parent.parent
	window.clear_widgets()
	
	# -- Make Player 1 Label
	player1Layout = AnchorLayout(anchor_x='left', anchor_y='bottom', padding=5)
	player1 = Label(text='Player 1: Selecting piece for Player 2', size_hint=(0.24,0.1))
	player1Layout.add_widget(player1)
	window.add_widget(player1Layout)
	g_player1 = player1		#set player1 global var
	
	# -- Make Player 2 Label
	player2Layout = AnchorLayout(anchor_x='left', anchor_y='top', padding=5)
	player2 = Label(text='Player 2: Waiting...', size_hint=(0.14,0.1))
	player2Layout.add_widget(player2)
	window.add_widget(player2Layout)
	g_player2 = player2		#set player2 global var
	
	# --Menu Button
	menuBtnLayout = AnchorLayout(anchor_x='right', anchor_y='top', padding=5)
	menuBtn = Button(text='Main Menu', background_color=(0.2,0.32,1.8,1), size_hint=(0.1,0.1))
	menuBtn.bind(on_release=MainMenu)
	menuBtnLayout.add_widget(menuBtn)
	window.add_widget(menuBtnLayout)
	
	# -- Create Holders for PieceToPlay, GameBoard, AvaliablePieces
	pieceToPlayLayout = AnchorLayout(anchor_x='left', anchor_y='center', padding=(160,0,-120,0))
	playBoardLayout = AnchorLayout(anchor_x='center', anchor_y='center', padding=(0,0,100,0))
	piecesAvailableLayout = AnchorLayout(anchor_x='right', anchor_y='center', padding=(80,0,40,0))
	
	# -- PieceToPlay Button	
	toPlayBtn = Button(background_color=(.2,1,.2,1), size_hint=(0.1,0.1))
	pieceToPlayLayout.add_widget(toPlayBtn)
	window.add_widget(pieceToPlayLayout)
	
	# -- SETTING pieceToPlay GLOBAL VAR
	g_pieceToPlay = toPlayBtn

	# -- Create Board
	boardLayout = GridLayout(cols=4, size_hint=(0.3,0.4))

	# add buttons to main board
	for i in range(1,17):
		# Create our piece graphic buttons
		b = Button(size_hint=(0.1,0.1), id=str(i))
		# Add event listern
		b.bind(on_release = selectBoardLocation)
		# Add to layout
		boardLayout.add_widget(b)

	playBoardLayout.add_widget(boardLayout)
	window.add_widget(playBoardLayout)   #end of middle board
	
	# -- Create piecesToPlay
	#availablePiecesToPlay
	smallBoardLayout = GridLayout(cols=4, size_hint=(0.3,0.4))
	
	# -- Init pieces
	for i in range(1,17):
		# Create our piece graphic buttons using 'i' to grab appropriate images
		b = Button(background_color=(.88,.6,.3,1), size_hint=(0.05,0.05), background_normal = 'pieces/piece' + str(i) + '.jpg')
		# Add the event listener
		b.bind(on_release = selectPiece)
		# add them to our layout
		smallBoardLayout.add_widget(b)

	# -- Add to main view
	piecesAvailableLayout.add_widget(smallBoardLayout)
	window.add_widget(piecesAvailableLayout)
	
	# -- Ask User: 'Single or Two Player?'
	# -- Create popup - StackLayout()
	popUP()
	# -- Show it
	popup.open()


#####################################
# SELECT PIECE FUNCTION
# This is a callback function that has
# been registered/binded with the gamePiece Buttons
# Kivy auto populates 'instance'
#####################################
def selectPiece(instance):
	global pieceFeatures
	
	if g_pieceToPlay.background_normal == 'atlas://data/images/defaulttheme/button':
		# 'instance' is a 'pointer' to the button location in memory
		# Thus we are able to access its properties...
		print('Selected Button MemAddress: <%s>' % (instance))
		print('Selected Button Image: <%s>' %(instance.background_normal))

		### Set peice to disabled graphic
		# Contruct the dissabled graphic location string
		disabledGraphic = instance.background_normal[:-4] + '_disabled.jpg'
		#print (disabledGraphic)
		# Set the dissabled graphic
		instance.background_disabled_normal = disabledGraphic
		# Dissable the button so the disabled graphic shows
		instance.disabled = True

		### Set the 'Piece To Play' Button image to the selected piece
		global g_pieceToPlay
		g_pieceToPlay.background_color=(1,1,1,1)
		g_pieceToPlay.background_normal = instance.background_normal
		
	else:		#Must Play Piece Once It's Picked!
		err_popup = Popup(title='Oops!', content=Label(text='You must play the piece once it has been chosen...'
		' Like chess,\nthis version of Quarto is touch a piece, move a piece.'), size_hint=(0.5,0.5))
		err_popup.open()
	
	#Game Flow Updater 1
	global g_moveTrack
	if g_moveTrack == 1:
		g_player1.text='Player 1: Waiting...'
		g_player1.size_hint=(0.14,0.1)
		g_player2.text='Player 2: Making Move'
		g_player2.size_hint=(0.16,0.1)
		g_moveTrack = 2				#select for player 1
	elif g_moveTrack == 3:
		g_player1.text='Player 1: Making Move'
		g_player1.size_hint=(0.16,0.1)
		g_player2.text='Player 2: Waiting...'
		g_player2.size_hint=(0.14,0.1)
		g_moveTrack = 4				#select for player 2


# Now that a piece has been selected
# We can update the board to reflect it.
# bound this function using for loop on line 120
def selectBoardLocation(instance):
	global g_pieceToPlay
	global g_player1
	global g_player2
	global g_moveTrack
	global g_playBoard
	global pieceFeatures
	
	try:
		if g_pieceToPlay.background_normal != 'atlas://data/images/defaulttheme/button':
			instance.background_disabled_normal = g_pieceToPlay.background_normal
			instance.disabled = True
			g_pieceToPlay.background_normal='atlas://data/images/defaulttheme/button'
			g_pieceToPlay.background_color=(.2,1,.2,1)
			
			#save the piece that was played
			saveIndex = instance.background_disabled_normal[12:-4]
			#get the characteristics of the piece
			chars = pieceFeatures[int(saveIndex) - 1]
			g_playBoard[int(instance.id)] = chars
			print('Played piece: %s' %(g_playBoard[int(instance.id)],))
			print('Selected Position: %s' %(instance.id))
			
			
			
			#Game Flow Updater 2
			if g_moveTrack == 2:
				g_player1.text='Player 1: Waiting...'
				g_player1.size_hint=(0.14,0.1)
				g_player2.text='Player 2: Selecting piece for Player 1'
				g_player2.size_hint=(0.24,0.1)
				winLoss(instance)				#check for win
				g_moveTrack = 3			#make player 1 move
			elif g_moveTrack == 4:
				g_player1.text='Player 1: Selecting piece for Player 2'
				g_player1.size_hint=(0.24,0.1)
				g_player2.text='Player 2: Waiting...'
				g_player2.size_hint=(0.14,0.1)
				winLoss(instance)				#check for win
				g_moveTrack = 1			#make player 2 move
	except:
		print('You have to select a piece to play first!')

#win/loss function
# -- checks for win conditions on the playBoard
# -- called every time a piece is placed
# -- if 4 pieces in a row of the same characteristic
#    then win for the player who placed the last piece
def winLoss(instance):
	#print('in winLoss')
	global g_playBoard
	for i in range(1,17):
		print('playBoard: ', g_playBoard[i])
		
	
	
	
	
#popup func
# -- Constructs Dialog Window asking user to select
# -- Single or Two Player Game
# -- Var 'gameMode' is set after use selection
# -- We return and wait for event from game piece buttons
def popUP():
	popLayout = StackLayout()
	
	popup.content=popLayout
					
	popText = Label(text='What type of game would you like to play?')
	popText.size_hint=(1.0,0.9)
	
	popBtn1 = Button(text='Single Player', group='choice')
	popBtn1.bind(on_release = singlePlayer)
	popBtn2 = Button(text='Two Player', group='choice')
	popBtn2.bind(on_release = twoPlayer)

	popBtn1.size_hint=( 0.5, 0.1 )
	popBtn2.size_hint=( 0.5, 0.1 )
	
	popLayout.add_widget( popText )
	popLayout.add_widget( popBtn1 )
	popLayout.add_widget( popBtn2 )
	
	
def modeCheck(gameMode):
	if gameMode == 1:
		popup.dismiss()
		print('You selected SINGLE PLAYER!')
	elif gameMode == 2:
		popup.dismiss()
		print('You selected TWO PLAYER!')
			
			
#SINGLE PLAYER FUNC
def singlePlayer(instance):
	gameMode = 1
	modeCheck(gameMode)
			
#TWO PLAYER FUNC
def twoPlayer(instance):
	gameMode = 2
	modeCheck(gameMode)
	
		
########################INSTRUCTIONS MENU###############################
def HelpMenu(instance):
	window = instance.parent.parent
	window.clear_widgets()
	
	textLayout = AnchorLayout(anchor_x='center', anchor_y='center')
			
	buttonLayout = AnchorLayout(anchor_x='right', anchor_y='top', padding=5)		
	btn = Button(text='Main Menu', background_color=(0.2,0.32,1.8,1))
	btn.size_hint=(0.1,0.1)
	btn.bind(on_release=MainMenu)
		
	DescObjLabel = Label(text='[b]Description[/b]\n\nQuarto is a game played by two players on a 4x4,' 
	'16 space board. There are 16 different pieces that can be constructed\n in any combination of ' 
	'four characteristics (Size, Color, Shape, Hole) in an attempt to win the game.\n\n[b]Objective[/b]'
	'\n\nTo win the game a line of pieces with matching characteristics (Four big pieces, four little, '
	'four dark, four light, four with a hole,\nor four without a hole) must be constructed. '
	'These pieces can be layed out horizontally, vertically, or diagonally.\n\n'
	'[b]Gameplay[/b]\n\nPlayers move alternatively, placing one piece on the board at a time. ' 
	'Note that once a piece has been placed on the board it \ncannot be moved again. '
	'Perhaps the most unique aspect of Quarto is that the choice of the piece to be placed on the board\n'
	'is not decided by the player placing the piece, but by the opponent. Each turn consists of two actions:\n\n'
	'     [b]1.[/b] Place the piece given by the opponent on the board.\n\n     [b]2.[/b] Give the opponent the '
	'piece to be played on the next move\n\nTo start the game the player needs only to select the piece for '
	'his opponent to play.', markup=True)
		
	textLayout.add_widget(DescObjLabel)
	buttonLayout.add_widget(btn)
		
	window.add_widget(textLayout)
	window.add_widget(buttonLayout)
##########################End of Instructions Menu######################
	
def ExitFunc(instance):
	exit()
	
class StartMenu(AnchorLayout):
	def __init__(self, **kwargs):
		super(StartMenu, self).__init__(**kwargs)
		
		openLayoutLabel = AnchorLayout(anchor_x='left', anchor_y='center', padding=25)
		playGameBtnLayout = AnchorLayout(anchor_x='left', anchor_y='bottom', padding=(130,30,-85,10))
		instructionLayout = AnchorLayout(anchor_x='center', anchor_y='bottom', padding=(5,30,5,10))
		exitLayout = AnchorLayout(anchor_x='right', anchor_y='bottom', padding=(-85,30,130,10))
		
		
		header = Label(text='Welcome to [b]Quarto[/b]. This program was developed\n'
					'by Cody Markham in 2015 as part of a Senior Design\n'
					'course at [i]Capitol Technology University[/i] that allowed\n' 
					'him to complete his degree in Computer Science. He hopes\n'
					'you have as much fun playing it as he did developing it.', markup=True, font_size=18)
		
		newBtn = Button(text='New Game', background_color=(0.2,0.32,1.8,1), height=225, font_size=25)
		newBtn.size_hint=(0.18,0.18)
		newBtn.bind(on_release=StartGame)
		
		helpBtn = Button(text='Instructions', background_color=(0.2,1.8,0.32,0.8), font_size=25)
		helpBtn.size_hint=(0.18,0.18)
		helpBtn.bind(on_release=HelpMenu)
		
		exitBtn = Button(text='Exit', background_color=(1.8,0.32,0.2,1), font_size=25)
		exitBtn.size_hint=(0.18,0.18)
		exitBtn.bind(on_press=ExitFunc)
		
		openLayoutLabel.add_widget(header)
		playGameBtnLayout.add_widget(newBtn)
		instructionLayout.add_widget(helpBtn)
		exitLayout.add_widget(exitBtn)
		
		self.add_widget(openLayoutLabel)
		self.add_widget(playGameBtnLayout)
		self.add_widget(instructionLayout)
		self.add_widget(exitLayout)
		
class StartPlay(App):
	title = 'Quarto'
	icon = 'quarto_icon.png'
	def build(self):
		return StartMenu()
	
if __name__ == "__main__":
	StartPlay().run()
