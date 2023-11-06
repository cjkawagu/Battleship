import pygame, os, sys
dim_field = (1050,500)

gameScreen = pygame.display.set_mode(dim_field)
clock = pygame.time.Clock()
titleScreen = pygame.image.load('TitleScreen.png').convert()
titleScreen = pygame.transform.scale(titleScreen, dim_field)
winScreen = pygame.image.load('winscreen.jpg').convert()
winScreen = pygame.transform.scale(winScreen, dim_field)
loseScreen = pygame.image.load('losescreen.jpg').convert()
loseScreen = pygame.transform.scale(loseScreen, dim_field)


WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
rect = pygame.Rect(550,0,50,50)

rect_sub = pygame.Rect(550,0,50,150)
sub_sprite = pygame.image.load('sub.png').convert()
sub_sprite = pygame.transform.scale(sub_sprite, (50, 150))
sub_sprite.set_colorkey((0,0,0))

rect_battleship = pygame.Rect(550,0,50,150)
battleship_sprite = pygame.image.load('battleship.png').convert()
battleship_sprite = pygame.transform.scale(battleship_sprite, (50, 150))
battleship_sprite.set_colorkey((0,0,0))

rect_destroyer = pygame.Rect(550,0,50,100)
destroyer_sprite = pygame.image.load('destroyer.png').convert()
destroyer_sprite = pygame.transform.scale(destroyer_sprite, (50, 100))
destroyer_sprite.set_colorkey((0,0,0))

rect_cruiser = pygame.Rect(550,0,50,200)
cruiser_sprite = pygame.image.load('cruiser.png').convert()
cruiser_sprite = pygame.transform.scale(cruiser_sprite, (50, 200))
cruiser_sprite.set_colorkey((0,0,0))

rect_carrier = pygame.Rect(550,0,50,250)
carrier_sprite = pygame.image.load('carrier.png').convert()
carrier_sprite = pygame.transform.scale(carrier_sprite, (50, 250))
carrier_sprite.set_colorkey((0,0,0))

rect_plane = pygame.Rect(0,0,50,50)
plane_sprite = pygame.image.load('plane.png').convert()
plane_sprite = pygame.transform.scale(plane_sprite, (50, 50))
plane_sprite.set_colorkey((0,0,0))

shipList = [rect_destroyer, rect_battleship, rect_sub, rect_cruiser, rect_carrier]
coordList = []
collideList = [rect_destroyer, rect_battleship]
computerAlreadyShot = []
playerAlreadyShot = []
colorRed = []
colorBlue = []
rect_red = pygame.Rect(0,0,50,50)
rect_blue = pygame.Rect(0,0,50,50)

rect_sub2 = pygame.Rect(0,0,50,150)
rect_battleship2 = pygame.Rect(0,0,50,150)
rect_destroyer2 = pygame.Rect(0,0,50,100)
rect_cruiser2 = pygame.Rect(0,0,50,200)
rect_carrier2 = pygame.Rect(0,0,50,250)

shipList2 = [rect_destroyer2, rect_battleship2, rect_sub2, rect_cruiser2, rect_carrier2]
collideList2 = [rect_destroyer2, rect_battleship2]

shipimgList = [destroyer_sprite, battleship_sprite, sub_sprite, cruiser_sprite, carrier_sprite]

computerHit = 0
playerHit = 0
difficulty = 0
hitShip = False
hitShipNorth = False
hitShipSouth = False
computerShotx = 0
computerShoty = 0
referencex = 0
referencey = 0
pygame.font.init()
font = pygame.font.SysFont('raleway', 40)