import random
import time
import pygame, sys

pygame.init()
img=pygame.image.load('hero.game.png')
img2=pygame.image.load('game.sprite.png')
bg=pygame.image.load('background.sprite.png')

class Human:
	
	def __init__(self,name):
		self.name=name
		self.creaturelist=[]
		
	def addcreature(self,creature):
		self.creaturelist.append(creature)
		
	def battle(self,other):			
		try:
			while len(self.creaturelist)>0 or len(other.creaturelist)>0:	
				for i in range(len(self.creaturelist)):
					print "Press",i,"to select",self.creaturelist[i].name
				creature_choose=input("Please choose a creature in your Creature List:")	
				#while creature_choose>len(self.creaturelist) or creature_choose<0:
					#creature_choose=input("Please choose a creature in your Creature List:")	

				active_creature=self.creaturelist[creature_choose]
				rand_creature_number=random.randrange(0,len(other.creaturelist))
				rand_creature=other.creaturelist[rand_creature_number]
				if active_creature.creatureBattle(rand_creature)==True:
					del other.creaturelist[rand_creature_number]
				else:
					del self.creaturelist[creature_choose]
		except:					
			if len(self.creaturelist)<=0:
				print "You are out of creatures! Return to the Pygame window"
				winner=False
			elif len(other.creaturelist)<=0:
				print "You have won! Good job! Return to the Pygame window"		
				winner=True
		return winner
class bodypart:
	
	def __init__(self,name):
		self.part=0
		self.health=0
		int(self.health)
		self.strength=0
		int(self.strength)
		self.name=name
		
		
		
		
					
class Creature:
	
	def __init__(self,name):
		self.name=name
		self.bodylist=[]
		self.health=0
		self.strength=0
		
	def addbodypart(self,bodypart):
		self.bodylist.append(bodypart)
		self.health=self.health+bodypart.health

		
	
	
	def updatehealthandstrength(self):
		self.health=0
		for i in range(len(self.bodylist)):
			self.health+=int(self.bodylist[i].health)
			self.strength+=int(self.bodylist[i].strength)
			
		
	def creatureBattle(self,creature):
		battle=True
		while battle:	
			self.attack=(self.strength)/2+random.randrange(0,20)
			creature.attack=(creature.strength)/5+random.randrange(0,5)
			print "Your enemy has chosen",creature.name	
			for i in range(len(creature.bodylist)):
				print "Press",i,"for",creature.bodylist[i].name,",with health of ",creature.bodylist[i].health
			
			target1=input("Which body part would you like to attack?")
			#while True: 
			#	try:
			#		target1>len(creature.bodylist) or target1<0
			#		break
			#	except:
			#		print("Please choose a number listed")
					
			creature.bodylist[target1].health-=self.attack
					
			
			if creature.bodylist[target1].health>0:
				print "That body part,",creature.bodylist[target1].name, ",now has a health of:" ,creature.bodylist[target1].health	
			
			elif creature.bodylist[target1].health<=0:
				print creature.name,"has lost their",creature.bodylist[target1].name
				del creature.bodylist[target1]
			
			creature.health=0
			creature.strength=0
			for i in range(len(creature.bodylist)):
				creature.health+=(creature.bodylist[i].health)
				creature.strength+=(creature.bodylist[i].strength)
	
				
			target2=random.randrange(0,len(self.bodylist))			
			self.bodylist[target2].health=self.bodylist[target2].health-creature.attack
			if self.bodylist[target2].health<=0:
				print self.name,"has lost their",self.bodylist[target2].name	
				del self.bodylist[target2]
				print "Your health is",self.health
			self.health=0
			self.strength=0
			for i in range(len(self.bodylist)):
				self.health+=int(self.bodylist[i].health)
				self.strength+=int(self.bodylist[i].strength)

			
						
			if self.health<=0 or creature.health<=0:
				battle=False
			
		if self.health<=0:
			Winner=False
			print self.name,"has died!"
		else:
			Winner=True
			print creature.name,"has died!"
			
		return Winner		
		
	

	
	


			
##Global Variables

black = (0,0,0)
white = (255,255,255)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)
display_width=800
display_height=600
GameDisplay=pygame.display.set_mode((display_width,display_height))	
font=pygame.font.SysFont(None,25)
clock=pygame.time.Clock()


def define_bodypart(bodypartN,attack_catalog):
		stats=attack_catalog[(bodypartN)]
		bodypartN=bodypart(bodypartN)
		bodypartN.health=int(stats[0])
		bodypartN.strength=int(stats[1])
		return bodypartN
		

def define_creature(creature,creature_catalog,attack_catalog):
		creature=Creature(creature.name)
		creature.bodylist=(creature_catalog[(creature.name)])
		for i in range(len(creature.bodylist)):
			creature.bodylist[i]=bodypart(creature.bodylist[i])
			creature.bodylist[i]=define_bodypart(creature.bodylist[i].name,attack_catalog)
			creature.health+=(creature.bodylist[i].health)
			creature.strength+=(creature.bodylist[i].strength)
		return creature
			




def creature_catalog(filein):
		datafile=open(filein,'r')
		creature_catalog={}
		limbs=[]
		for data in datafile:
			(key,val)=data.split(',')
			val=val.strip()
			limbs=list(val.split(':'))
			creature_catalog[(key)]=limbs
		
		datafile.close()
		
		return creature_catalog


def attack_catalog(filein):
		datafile=open(filein,'r')
		attack_catalog={}
		stats=[]
		for data in datafile:
			(key,val)=data.split(',')
			val=val.strip()
			stats=list(val.split(':'))
			attack_catalog[(key)]=stats
			
		datafile.close()
		return attack_catalog





def battleScreen(hman,hman2):
	GameDisplay.fill(white)
	message_to_screen("Yo! It's time to battle my homie",red,-50)
	message_to_screen("Press C to return to screen",black,-30)
	message_to_screen("Press Q to quit",black,-10)
	message_to_screen("Press B to enter Battle!",black,20)
	pygame.display.update()
	battleScreen=True
	while battleScreen:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
			if event.type==pygame.KEYDOWN:	
				if event.key==pygame.K_c:
					battleScreen=False
					
				elif event.key==pygame.K_q:
					pygame.quit()
					quit()
				elif event.key==pygame.K_b:
					if hman.battle(hman2)==True:
						GameDisplay.fill(green)
						message_to_screen(("You have proven victorious!Excellent work!"),white,0)
						message_to_screen("Press C to return to screen",white,-50)
						message_to_screen("Press Q to quit",white,20)
						pygame.display.update()
					else:
						GameDisplay.fill(red)
						message_to_screen(("You're a loser!"),black,0)
						message_to_screen("Press C to return to screen",black,-50)
						message_to_screen("Press Q to quit",black,20)
						pygame.display.update()
			
						
		
		clock.tick(5)

def intro():
	intro=True
	while intro:
		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_q:
					pygame.quit()
					quit()
				if event.key==pygame.K_c:
					intro=False
		
		
		
		GameDisplay.fill(white)
		message_to_screen("Welcome to YO!",black,-100)
		message_to_screen("The Objective of the game is to fight the evil power!",black,-60)
		message_to_screen("Use your arrow keys to go to the ugly dude with the white background.",black,-30)
		message_to_screen("Make sure you stay on the screen!",black,40)
		message_to_screen("Press C to play or Q to quit",green,-10)
		pygame.display.update()
		clock.tick(5)		


def text_objects(text,color):
	textSurface=font.render(text,True,color)
	return textSurface, textSurface.get_rect()

def message_to_screen(msg,color,y_displace=0):
	textSurf, textRect=text_objects(msg,color)
	textRect.center=(display_width/2),(display_height/2)+y_displace
	GameDisplay.blit(textSurf,textRect)

def gameLoop():
	#global winner
	name='wing'
	a=bodypart(name)
	dic_a=attack_catalog('attack_catalog.txt')
	dic_b=creature_catalog('creature_catalog.txt')
	define_bodypart(a.name,dic_a)
	monstername='wolf'
	wolf=Creature(monstername)
	wolf=(define_creature(wolf,dic_b,dic_a))
	snake=Creature('python')
	snake=define_creature(snake,dic_b,dic_a)
	bull=Creature('bull')
	bull=define_creature(bull,dic_b,dic_a)
	raven=Creature('raven')
	raven=define_creature(raven,dic_b,dic_a)
	bee=Creature('giant bee')
	bee=define_creature(bee,dic_b,dic_a)
	beatle=Creature('giant beatle')
	beatle=define_creature(beatle,dic_b,dic_a)
	ostrich=Creature('ostrich')
	ostrich=define_creature(ostrich,dic_b,dic_a)
	Avi=Human('Avi')
	Andy=Human('Andy')
	Avi.addcreature(wolf)
	Andy.addcreature(snake)
	Avi.addcreature(bull)
	Avi.addcreature(raven)
	Andy.addcreature(bee)
	Andy.addcreature(ostrich)
	box = pygame.Rect(100,100,50,50)	
	block_size= 20
	
	AppleThickness=30
	
	randAppleX=random.randrange(0,display_width-AppleThickness)
	randAppleY=random.randrange(0,display_height-AppleThickness)
	
	#apple=pygame.Rect(randAppleX,randAppleY,block_size,block_size)	
	
	
	pygame.display.set_caption('YO!')
	
	lead_x=display_width/2
	lead_y=display_height/2
	sprite=pygame.Rect(lead_x,lead_y,block_size,block_size)
	
	
	lead_x_change=0
	lead_y_change=0
	
	#clock=pygame.time.Clock()
	
	FPS=30
	

	gameExit=False
	gameOver=False
	
	while not gameExit:
		while gameOver==True:
			GameDisplay.fill(white)
			message_to_screen("Game over",red,-50)
			message_to_screen("Press C to play again or Q to quit",green,-10)
			pygame.display.update()
			
			for event in pygame.event.get():
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_q:
						gameExit=True
						gameOver=False
					if event.key==pygame.K_c:
						gameLoop()
			
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				gameExit=True
				pygame.quit()
				quit()
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_LEFT:
					lead_x_change=-block_size
				elif event.key==pygame.K_RIGHT:
					lead_x_change=block_size
				elif event.key==pygame.K_UP:
					lead_y_change=-block_size
				elif event.key==pygame.K_DOWN:
					lead_y_change=block_size
			if event.type==pygame.KEYUP:
				if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
					lead_x_change=0
				elif event.key==pygame.K_UP or event.key==pygame.K_DOWN:
					lead_y_change=0
			
			if lead_x>=display_width or lead_x<=0 or lead_y>=display_height or lead_y<=0:
				gameOver=True
			
			if lead_x > randAppleX and lead_x<randAppleX+AppleThickness or lead_x+block_size> randAppleX and lead_x+block_size < randAppleX+AppleThickness:	
				if lead_y>randAppleY and lead_y<randAppleY+AppleThickness or lead_y+block_size >randAppleY and lead_y<randAppleY+AppleThickness:
					if len(Avi.creaturelist)>0 and  len(Andy.creaturelist)>0:
						battleScreen(Avi,Andy)
					else:
						pass
						
					
		
		lead_x+=lead_x_change
		lead_y+=lead_y_change
		
		
		pygame.display.update()
		GameDisplay.fill(green)
		GameDisplay.blit(bg,(0,0))
		pygame.draw.rect(GameDisplay,black,[lead_x,lead_y,block_size,block_size])
		pygame.draw.rect(GameDisplay,red,[randAppleX,randAppleY,AppleThickness,AppleThickness])
		GameDisplay.blit(img,(lead_x,lead_y))
		GameDisplay.blit(img2,(randAppleX,randAppleY))
		pygame.display.update()
		clock.tick(FPS)
	pygame.quit()
	quit()



	
	
#main()
intro()		
gameLoop()

	
