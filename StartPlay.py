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

#global yourPiece
global g_pieceToPlay

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
	
	window = instance.parent.parent
	window.clear_widgets()
	
	# --Menu Button
	menuBtnLayout = AnchorLayout(anchor_x='right', anchor_y='top', padding=5)
	menuBtn = Button(text='Main Menu', background_color=(0.2,0.32,1.8,1))
	menuBtn.size_hint=(0.1,0.1)
	menuBtn.bind(on_release=MainMenu)
	menuBtnLayout.add_widget(menuBtn)
	window.add_widget(menuBtnLayout)
	
	#topPlayerLabel = Label(text='Player1', anchor_x='left')
	#menuBtnLayout.add_widget(topPlayerLabel)
	
	#bottomPlayerLabel = Label(text='Player2', anchor_x='left', anchor_y='bottom')
	#menuBtnLayout.add_widget(bottomPlayerLabel)
	
	# -- Create Holders for PieceToPlay, GameBoard, AvaliablePieces
	pieceToPlayLayout = AnchorLayout(anchor_x='left', anchor_y='center', padding=(160,0,-120,0))
	playBoardLayout = AnchorLayout(anchor_x='center', anchor_y='center', padding=(0,0,100,0))
	piecesAvailableLayout = AnchorLayout(anchor_x='right', anchor_y='center', padding=(80,0,40,0))
	
	# -- PieceToPlay Button	
	toPlayBtn = Button(text='PieceToPlay', background_color=(.2,.8,.2,1))
	toPlayBtn.size_hint=(0.1,0.1)
	toPlayBtn.name = 'hello' # What do you want?
	pieceToPlayLayout.add_widget(toPlayBtn)
	window.add_widget(pieceToPlayLayout)
	# -- SETTING GLOBAL VAR HERE
	g_pieceToPlay = toPlayBtn

	# -- Create Board
	boardLayout = GridLayout(cols=4, size_hint=(0.45,0.45))
	space1 = Button(text='1')  #row 1
	space1.size_hint=(0.1,0.1)
	space2 = Button(text='2')
	space2.size_hint=(0.1,0.1)
	space3 = Button(text='3')
	space3.size_hint=(0.1,0.1)
	space4 = Button(text='4')
	space4.size_hint=(0.1,0.1)
	space5 = Button(text='5')  #row 2
	space5.size_hint=(0.1,0.1)
	space6 = Button(text='6')
	space6.size_hint=(0.1,0.1)
	space7 = Button(text='7')
	space7.size_hint=(0.1,0.1)
	space8 = Button(text='8')
	space8.size_hint=(0.1,0.1)
	space9 = Button(text='9')  #row 3
	space9.size_hint=(0.1,0.1)
	space10 = Button(text='10')
	space10.size_hint=(0.1,0.1)
	space11 = Button(text='11')
	space11.size_hint=(0.1,0.1)
	space12 = Button(text='12')
	space12.size_hint=(0.1,0.1)
	space13 = Button(text='13')  #row 4
	space13.size_hint=(0.1,0.1)
	space14 = Button(text='14')
	space14.size_hint=(0.1,0.1)
	space15 = Button(text='15')
	space15.size_hint=(0.1,0.1)
	space16 = Button(text='16')
	space16.size_hint=(0.1,0.1)

	boardLayout.add_widget(space1)
	boardLayout.add_widget(space2)
	boardLayout.add_widget(space3)
	boardLayout.add_widget(space4)
	boardLayout.add_widget(space5)
	boardLayout.add_widget(space6)
	boardLayout.add_widget(space7)
	boardLayout.add_widget(space8)
	boardLayout.add_widget(space9)
	boardLayout.add_widget(space10)
	boardLayout.add_widget(space11)
	boardLayout.add_widget(space12)
	boardLayout.add_widget(space13)
	boardLayout.add_widget(space14)
	boardLayout.add_widget(space15)
	boardLayout.add_widget(space16)

	# -- Bind Event Listener on all board pieces
	#print('<(*_*<)')
	for b in boardLayout.children[:]:
		b.bind(on_release = selectBoardLocation)
	
	playBoardLayout.add_widget(boardLayout)
	window.add_widget(playBoardLayout)   #end of middle board
	
	# -- Create piecesToPlay
	#availablePiecesToPlay
	smallBoardLayout = GridLayout(cols=4, size_hint=(0.3,0.4))
	# -- Init pieces
	#row 1
	piece1 = Button(background_color=(.88,.6,.3,1), size_hint=(0.05,0.05), background_normal = 'pieces/piece1.jpg', background_disabled_down='piece1_disabled.jpg')
	piece2 = Button(background_color=(.88,.6,.3,1), size_hint=(0.05,0.05), background_normal = 'pieces/piece2.jpg', background_disabled_down='piece2_disabled.jpg')
	piece3 = Button(background_color=(.88,.6,.3,1), size_hint=(0.05,0.05), background_normal = 'pieces/piece3.jpg', background_disabled_down='piece3_disabled.jpg')
	piece4 = Button(background_color=(.88,.6,.3,1), size_hint=(0.05,0.05), background_normal = 'pieces/piece4.jpg', background_disabled_down='piece4_disabled.jpg')
	#row 2
	piece5 = Button(background_color=(.88,.6,.3,1), size_hint=(0.05,0.05), background_normal = 'pieces/piece5.jpg', background_disabled_down='piece5_disabled.jpg')  
	piece6 = Button(background_color=(.88,.6,.3,1), size_hint=(0.05,0.05), background_normal = 'pieces/piece6.jpg', background_disabled_down='piece6_disabled.jpg')
	piece7 = Button(background_color=(.88,.6,.3,1), size_hint=(0.05,0.05), background_normal = 'pieces/piece7.jpg', background_disabled_down='piece7_disabled.jpg')
	piece8 = Button(background_color=(.88,.6,.3,1), size_hint=(0.05,0.05), background_normal = 'pieces/piece8.jpg', background_disabled_down='piece8_disabled.jpg')
	#row 3
	piece9 = Button(background_color=(.88,.6,.3,1), size_hint=(0.05,0.05), background_normal = 'pieces/piece9.jpg', background_disabled_down='piece9_disabled.jpg')
	piece10 = Button(background_color=(.88,.6,.3,1), size_hint=(0.05,0.05), background_normal = 'pieces/piece10.jpg', background_disabled_down='piece10_disabled.jpg')
	piece11 = Button(background_color=(.88,.6,.3,1), size_hint=(0.05,0.05), background_normal = 'pieces/piece11.jpg', background_disabled_down='piece11_disabled.jpg')
	piece12 = Button(background_color=(.88,.6,.3,1), size_hint=(0.05,0.05), background_normal = 'pieces/piece12.jpg', background_disabled_down='piece12_disabled.jpg')
	#row 4
	piece13 = Button(background_color=(.88,.6,.3,1), size_hint=(0.05,0.05), background_normal = 'pieces/piece13.jpg', background_disabled_down='piece13_disabled.jpg') 
	piece14 = Button(background_color=(.88,.6,.3,1), size_hint=(0.05,0.05), background_normal = 'pieces/piece14.jpg', background_disabled_down='piece14_disabled.jpg')
	piece15 = Button(background_color=(.88,.6,.3,1), size_hint=(0.05,0.05), background_normal = 'pieces/piece15.jpg', background_disabled_down='piece15_disabled.jpg')
	piece16 = Button(background_color=(.88,.6,.3,1), size_hint=(0.05,0.05), background_normal = 'pieces/piece16.jpg', background_disabled_down='piece16_disabled.jpg')
	# -- Setup Event Listeners
	piece1.bind(on_release = selectPiece)
	piece1.name='1'
	piece2.bind(on_release = selectPiece)
	piece2.name='2'
	piece3.bind(on_release = selectPiece)
	piece3.name='3'
	piece4.bind(on_release = selectPiece)
	piece4.name='4'
	piece5.bind(on_release = selectPiece)
	piece5.name='5'
	piece6.bind(on_release = selectPiece)
	piece6.name='6'
	piece7.bind(on_release = selectPiece)
	piece7.name='7'
	piece8.bind(on_release = selectPiece)
	piece8.name='8'
	piece9.bind(on_release = selectPiece)
	piece9.name='9'
	piece10.bind(on_release = selectPiece)
	piece10.name='10'
	piece11.bind(on_release = selectPiece)
	piece11.name='11'
	piece12.bind(on_release = selectPiece)
	piece12.name='12'
	piece13.bind(on_release = selectPiece)
	piece13.name='13'
	piece14.bind(on_release = selectPiece)
	piece14.name='14'
	piece15.bind(on_release = selectPiece)
	piece15.name='15'
	piece16.bind(on_release = selectPiece)
	piece16.name='16'
	# -- Add to Layout
	smallBoardLayout.add_widget(piece1)
	smallBoardLayout.add_widget(piece2)
	smallBoardLayout.add_widget(piece3)
	smallBoardLayout.add_widget(piece4)
	smallBoardLayout.add_widget(piece5)
	smallBoardLayout.add_widget(piece6)
	smallBoardLayout.add_widget(piece7)
	smallBoardLayout.add_widget(piece8)
	smallBoardLayout.add_widget(piece9)
	smallBoardLayout.add_widget(piece10)
	smallBoardLayout.add_widget(piece11)
	smallBoardLayout.add_widget(piece12)
	smallBoardLayout.add_widget(piece13)
	smallBoardLayout.add_widget(piece14)
	smallBoardLayout.add_widget(piece15)
	smallBoardLayout.add_widget(piece16)
	# -- Add to main view
	piecesAvailableLayout.add_widget(smallBoardLayout)
	window.add_widget(piecesAvailableLayout)
	
	# -- Ask User: 'Single or Two Player?'
	# -- Create popup - StackLayout()
	popUP()
	# -- Show it
	popup.open()



# -- Mike Code
#####################################
# This is a callback function that has
# been registered/binded with the gamePiece Buttons
# See: http://kivy.org/docs/api-kivy.uix.button.html
# Kivy auto populates 'instance' for us
def selectPiece(instance):
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
	instance.disabled = True;

	### Set the 'Piece To Play' Button image to the selected piece
	global g_pieceToPlay
	g_pieceToPlay.background_normal = instance.background_normal

# Now that a piece has been selected
# We can update the board to reflect it.
# I binded this function using a for loop on line 120 ctr+f '<(*_*<)'
def selectBoardLocation(instance):
	global g_pieceToPlay
	try:
		instance.background_normal = g_pieceToPlay.background_normal
	except:
		print('You have to select a piece to play first!')



###############################  having trouble here!!!
######### SELECT PIECE ########
# def selectPiece(piece):
# 	# -- ORLY?
# 	# -- Please, think of the children!
# 	window = piece.parent.parent.parent
	
# 	toPlayBtn.name = piece.name
# 	print('this window: ', window.anchor_x, ' ', window.anchor_y)
	
##################################
##################################
	
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
	else:
		if gameMode == 2:
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
	#print('The button <%s> is being pressed' % instance.text)
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
