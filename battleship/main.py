import pygame, os, sys, random, time
pygame.init()
from Setup import *
random.seed()

def htp():
    running = True
    gameScreen.fill(BLACK)
    text1 = font.render('This is a classic game of battleship, where you aim to sink your opponent\'s ', True, WHITE)
    text2 = font.render('ships by specifying a grid location to fire on. First, place your own ships ', True, WHITE)
    text3 = font.render('on the right grid with the ARROW keys, and ENTER when satisfied. Then, use ', True, WHITE)
    text4 = font.render('the ARROW keys to choose a location to hit on the left grid. A RED result ', True, WHITE)
    text5 = font.render('means a hit, and a BLUE means a miss. Play until all ships have been sunk!', True, WHITE)
    text6 = font.render('PRESS TAB TO GO BACK', True, WHITE)
    gameScreen.blit(text1, (10, 10))
    gameScreen.blit(text2, (10, 50))
    gameScreen.blit(text3, (10, 90))
    gameScreen.blit(text4, (10, 130))
    gameScreen.blit(text5, (10, 170))
    gameScreen.blit(text6, (10, 450))
    gameScreen.blit(sub_sprite, (500, 300))
    gameScreen.blit(destroyer_sprite, (600, 275))
    gameScreen.blit(carrier_sprite, (700, 200))
    pygame.display.update()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.display.quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    running = False
                    intro()
                    break
def intro():
    running = True
    gameScreen.blit(titleScreen, (0,0))
    text1 = font.render('Welcome to BATTLESHIP!', True, WHITE)
    text2 = font.render('(PRESS 1 FOR EASY, 2 FOR NORMAL)', True, WHITE)
    text3 = font.render('(PRESS TAB FOR INSTRUCTIONS)', True, WHITE)
    gameScreen.blit(text1, (525, 100))
    gameScreen.blit(text2, (525, 150))
    gameScreen.blit(text3, (525, 200))
    pygame.display.update()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.display.quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    difficulty = 1
                    running = False
                    return difficulty
                if event.key == pygame.K_2:
                    difficulty = 2
                    running = False
                    return difficulty
                if event.key == pygame.K_TAB:
                    htp()

def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def initializeBoard():
    gameScreen.fill(WHITE)
    for x in range(0, 550, 50):
        pygame.draw.line(gameScreen, BLACK, (x,0), (x,500))
    for y in range(0, 500, 50):
        pygame.draw.line(gameScreen, BLACK, (0,y), (500,y))
    for x in range(550, 1050, 50):
        pygame.draw.line(gameScreen, BLACK, (x,0), (x,500))
    for y in range(0, 500, 50):
        pygame.draw.line(gameScreen, BLACK, (550,y), (1050,y))

def updateBoardLeft():
    initializeBoard()
    gameScreen.blit(sub_sprite, rect_sub)
    gameScreen.blit(battleship_sprite, rect_battleship)
    gameScreen.blit(destroyer_sprite, rect_destroyer)
    gameScreen.blit(cruiser_sprite, rect_cruiser)
    gameScreen.blit(carrier_sprite, rect_carrier)

def moveShip(ship):
    if event.key == pygame.K_LEFT:
        ship.move_ip(-50,0)
    if event.key == pygame.K_RIGHT:
        ship.move_ip(50,0)
    if event.key == pygame.K_UP:
        ship.move_ip(0,-50)
    if event.key == pygame.K_DOWN:
        ship.move_ip(0,50)

def boundaryRight(ship):
    if ship.left < 550:
        ship.left = 550
    if ship.top < 0:
        ship.top = 0
    if ship.right > 1050:
        ship.right = 1050
    if ship.bottom > 500:
        ship.bottom = 500

def boundaryLeft(plane):
    if plane.left < 0:
        plane.left = 0
    if plane.top < 0:
        plane.top = 0
    if plane.right > 500:
        plane.right = 500
    if plane.bottom > 500:
        plane.bottom = 500

def checkOverlap():
    if shipIndex == 0:
        return False
    if shipIndex == 1 and rect_battleship.colliderect(rect_destroyer):
        return True
    if shipIndex == 2:
        if int(rect_sub.collidelist(collideList)) != -1:
            return True
        else:
            collideList.append(rect_sub)
    if shipIndex == 3:
        if int(rect_cruiser.collidelist(collideList)) != -1:
            return True
        else:
            collideList.append(rect_cruiser)
    if shipIndex == 4:
        if int(rect_carrier.collidelist(collideList)) != -1:
            return True

def checkOverlap2():
    if shipIndex2 == 0:
        return False
    if shipIndex2 == 1 and rect_battleship2.colliderect(rect_destroyer2):
        return True
    if shipIndex2 == 2:
        if int(rect_sub2.collidelist(collideList2)) != -1:
            return True
        else:
            collideList2.append(rect_sub2)
    if shipIndex2 == 3:
        if int(rect_cruiser2.collidelist(collideList2)) != -1:
            return True
        else:
            collideList2.append(rect_cruiser2)
    if shipIndex2 == 4:
        if int(rect_carrier2.collidelist(collideList2)) != -1:
            return True

def compshipPlace(compship):
  compship.move_ip(50 * random.randint(0, 10), 50 * random.randint(0, 10))

def moveCursor(plane):
    if event.key == pygame.K_LEFT:
        plane.move_ip(-50,0)
    if event.key == pygame.K_RIGHT:
        plane.move_ip(50,0)
    if event.key == pygame.K_UP:
        plane.move_ip(0,-50)
    if event.key == pygame.K_DOWN:
        plane.move_ip(0,50)

def coordFinder():
    for x in range (550,1050,50):
        for y in range (0,500,50):
            rect.topleft = (x,y)
            if int(rect.collidelist(shipList)) != -1:
                coordList.append((x,y))
    return coordList

def computerShoot(alreadyShot, difficulty):
    global computerShotx
    global computerShoty
    global referencex
    global referencey
    global hitShipNorth
    global hitShipSouth
    if difficulty == 1:
        x = 550 + random.randint(0,9)*50
        y = random.randint(0,9)*50
        while (x,y) in alreadyShot:
            x,y = 550 + random.randint(0,9)*50, random.randint(0,9)*50
        alreadyShot.append((x,y))
        return x, y, alreadyShot
    if difficulty == 2:
        if hitShipNorth == True:
            x, y = computerShotx, computerShoty - 50
            if (x,y) in alreadyShot:
                x, y = 550+random.randint(0,9)*50, random.randint(0,9)*50
                while (x,y) in alreadyShot:
                    x,y = 550 + random.randint(0,9)*50, random.randint(0,9)*50
            if y < 0:
                hitShipNorth = False
                hitShipSouth = True
                computerShotx, computerShoty = referencex, referencey
                if (x,y) in alreadyShot or computerShoty > 500:
                    x, y = 550+random.randint(0,9)*50, random.randint(0,9)*50
                    while (x,y) in alreadyShot:
                        x,y = 550 + random.randint(0,9)*50, random.randint(0,9)*50
                alreadyShot.append((x,y))
                return computerShotx, computerShoty + 50, alreadyShot
            alreadyShot.append((x,y))
            return x, y, alreadyShot
        elif hitShipSouth == True:
            x, y = computerShotx, computerShoty + 50
            if (x,y) in alreadyShot or y > 450:
                hitShipSouth = False
                x, y = 550+random.randint(0,9)*50, random.randint(0,9)*50
                while (x,y) in alreadyShot:
                    x, y = 550 + random.randint(0,9)*50, random.randint(0,9)*50
            alreadyShot.append((x,y))
            return x, y, alreadyShot
        else:
            x, y = 550+random.randint(0,9)*50, random.randint(0,9)*50
            while (x,y) in alreadyShot:
                x,y = 550 + random.randint(0,9)*50, random.randint(0,9)*50
            alreadyShot.append((x,y))
            return x, y, alreadyShot

def playerShoot(alreadyShot):
    attackCoord = rect_plane.topleft
    alreadyShot.append(attackCoord)
    return attackCoord, alreadyShot

# def rotateShip(image, rectangle):
#   if event.key == pygame.K_r:
#     image = pygame.transform.rotate(image, 90)
#     rectangle = rotated_image.get_rect

# def rotateShip2(surf, image, rect):
#   if event.key == pygame.K_r:
#     image = pygame.transform.rotate(image, 90)
#     rect = image.get_rect

 # surf.blit(image, rect)

difficulty = intro()
settingUp = True
gameIsRunning = False
placementFinished = False
attackCoord = (0,0)
shipIndex = 0
shipIndex2 = 0

while settingUp:
    clock.tick(60)
    initializeBoard()
    #Player ship placement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            settingUp = False
        if event.type == pygame.KEYDOWN:
            moveShip(shipList[shipIndex])
            boundaryRight(shipList[shipIndex])
            if event.key == pygame.K_RETURN and not checkOverlap():
                shipIndex += 1

    if shipIndex >= 0:
        gameScreen.blit(destroyer_sprite, rect_destroyer)
    if shipIndex >=1:
        gameScreen.blit(battleship_sprite, rect_battleship)
    if shipIndex >=2:
        gameScreen.blit(sub_sprite, rect_sub)
    if shipIndex >=3:
        gameScreen.blit(cruiser_sprite, rect_cruiser)
    if shipIndex >=4:
        gameScreen.blit(carrier_sprite, rect_carrier)
    if shipIndex == 5:
        gameIsRunning = True
        coordList = coordFinder()
        break

    #Places computer ships
    if shipIndex2 != 5 and not checkOverlap2():
        compshipPlace(shipList2[shipIndex2])
        boundaryLeft(shipList2[shipIndex2])
        shipIndex2 += 1
    pygame.display.update()

turn = whoGoesFirst()

#Game loop
while gameIsRunning:
    if hitShipNorth == False and hitShipSouth == False and hitShip == True:
        referencex, referencey = computerShotx, computerShoty
    if hitShip == True and hitShipSouth == False:
        hitShipNorth = True
    if hitShip == False and hitShipNorth == True:
        hitShipNorth = False
        hitShipSouth = True
        computerShotx, computerShoty = referencex, referencey
    if turn == 'player':
        updateBoardLeft()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameIsRunning = False
            if event.type == pygame.KEYDOWN:
                moveCursor(rect_plane)
                boundaryLeft(rect_plane)
                if event.key == pygame.K_RETURN:
                    playerShot, playerAlreadyShot = playerShoot(playerAlreadyShot)
                    if playerShot not in playerAlreadyShot[:len(playerAlreadyShot)-1]:
                        if int(rect_plane.collidelist(shipList2)) == -1:
                            colorBlue.append(rect_plane.topleft)
                            turn = 'computer'
                        else:
                            colorRed.append(rect_plane.topleft)
                            playerHit += 1
                            if playerHit == 17:
                                gameIsRunning = False
                            else:
                                turn = 'computer'
    else:
        computerShotx, computerShoty, computerAlreadyShot = computerShoot(computerAlreadyShot, difficulty)
        for i in range(17):
            if (computerShotx, computerShoty) == coordList[i]:
                colorRed.append(coordList[i])
                computerHit += 1
                hitShip = True
                if computerHit == 17:
                    gameIsRunning = False
                else:
                    turn = 'player'
        if (computerShotx, computerShoty) not in coordList:
            colorBlue.append((computerShotx, computerShoty))
            hitShip = False
            if hitShipSouth == True:
                hitShipSouth = False
            turn = 'player'

    for i in range(len(colorRed)):
        copy = rect_red.copy()
        copy.topleft = (colorRed[i])
        pygame.draw.rect(gameScreen, (255,0,0), copy)

    for i in range(len(colorBlue)):
        copy = rect_blue.copy()
        copy.topleft = (colorBlue[i])
        pygame.draw.rect(gameScreen, (0,0,255), copy)
    gameScreen.blit(plane_sprite, rect_plane)
    pygame.display.update()


while playerHit == 17:
    gameScreen.blit(winScreen, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
    pygame.display.update()

while computerHit == 17:
    gameScreen.blit(loseScreen, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
    pygame.display.update()

pygame.display.quit()
pygame.quit()
