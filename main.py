# Main
#
# Not Working! Ordered updates displaying walls incorrectly
# Walls are changing order with each run time
# Messing with testList for multiple files (only Return a list from other files)
#
# L = [1]
# L[-1]
#
# Also adding Walls on the FAR LEFT and RIGHT LEVEL 2

import pygame, sys, os
from basic import *
from classes import *
from functions import *
from drawWalls import *
import gumm

pygame.init()

screenSize = (800, 600)
screen = pygame.display.set_mode(screenSize)

running = True

upKey, downKey, leftKey, rightKey = 0, 0, 0, 0
upHold, downHold, leftHold, rightHold = 0, 0, 0, 0
# N,S,E,W
direction = 0

clock = pygame.time.Clock()

wall0 = Wall(0,'a', 0)
wall1 = Wall(0,'b', 0)

wall2 = Wall(0,0, 2)
wall3 = Wall(0,1, 2)
wall4 = Wall(0,2, 2)

wall5 = Wall(1,0, 3)
wall6 = Wall(1,1, 3)
wall7 = Wall(1,2, 3)
wall8 = Wall(1,3, 3)
wall9 = Wall(1,4, 3)

wall10 = Wall(2,0, 4)
wall11 = Wall(2,1, 4)
wall12= Wall(2,2, 4)
wall13= Wall(2,3, 4)
wall14= Wall(2,4, 4)

wall98 = Wall(9,8, 9)

wall15 = Wall(3,0, 6)
wall16 = Wall(3,1, 6)
wall17 = Wall(3,2, 6)
wall18 = Wall(3,3, 6)
wall19 = Wall(3,4, 6)
wall20 = Wall(3,5, 6)
wall21 = Wall(3,6, 6)

wall22 = Wall(4,0, 7)
wall23 = Wall(4,1, 7)
wall24 = Wall(4,2, 7)
wall25 = Wall(4,3, 7)
wall26 = Wall(4,4, 7)
wall27 = Wall(4,5, 7)
wall28 = Wall(4,6, 7)
wall29 = Wall(4,7, 7)
wall30 = Wall(4,8, 7)



wallList = [wall0, wall1, wall2, \
            wall3, wall4, wall5, wall6, wall7, \
            wall8, wall9, wall10, wall11, wall12, \
            wall13, wall14, wall15, wall16, wall17, wall18, wall19, \
            wall20, wall21, wall22, wall23, wall24, wall25, wall26, wall27, wall28, wall29, wall30]

wallDict = {29: wall29, 30: wall30, \
            0: wall0, 1: wall1, 2: wall2, \
            3: wall3, 4: wall4, 5: wall5, 6: wall6, 7: wall7, \
            8: wall8, 9: wall9, 10: wall10, 11: wall11, 12: wall12, \
            13: wall13, 14: wall14, 15: wall15, 16: wall16, 17: wall17, 18: wall18, 19: wall19, \
            20: wall20, 21: wall21, 22: wall22, 23: wall23, 24: wall24, 25: wall25, 26: wall26, 27: wall27, 28: wall28}

redBlock = Block((40, 40), 0, 300, RED)
blackBlock = Block((800, 600), 0, 0, BLACK)

# Order to draw below
backGroup = pygame.sprite.Group()
monsterGroup = pygame.sprite.Group()

# Wall Depths each have their own layer
wallVisL0Group = pygame.sprite.Group()
wallVisL1Group = pygame.sprite.Group()
wallVisL2Group = pygame.sprite.Group()
wallVisL3Group = pygame.sprite.Group()
wallVisL4Group = pygame.sprite.Group()
wallVisL5Group = pygame.sprite.Group()
wallVisL6Group = pygame.sprite.Group()
wallGroup = pygame.sprite.Group()

def emptyVisGroups():
    wallVisL0Group.empty()
    wallVisL1Group.empty()
    wallVisL2Group.empty()
    wallVisL3Group.empty()
    wallVisL4Group.empty()
    wallVisL5Group.empty()
    wallVisL6Group.empty()


def sortkey(wall):
    return wall.name


backGroup.add(blackBlock)
monsterGroup.add(redBlock)

#4 x 12 map
userMap2 = [[[2, 0], [2, 0], [2, 0], [2, 0], [2, 0]],
            [[2, 0], [0, 0], [0, 0], [0, 0], [2, 5]],
            [[2, 0], [0, 0], [0, 0], [0, 0], [2, 0]],
            [[2, 0], [2, 0], [0, 0], [2, 0], [2, 0]],
            [[2, 0], [2, 0], [0, 0], [2, 0], [2, 0]],
            [[2, 0], [0, 0], [0, 0], [0, 0], [2, 0]],
            [[2, 0], [0, 0], [0, 0], [0, 0], [2, 0]],
            [[2, 0], [0, 0], [0, 0], [0, 0], [2, 0]],
            [[2, 0], [0, 0], [0, 0], [0, 0], [2, 0]],
            [[2, 0], [0, 0], [0, 0], [0, 0], [2, 0]],
            [[2, 0], [0, 0], [0, 0], [0, 0], [2, 0]],
            [[2, 0], [0, 0], [0, 0], [0, 0], [2, 0]],
            [[2, 0], [2, 0], [2, 0], [2, 0], [2, 0]]]

player = Player()
player.setStartPosition(2,10)
player.setDirection(0)

# Print userMap at start up
movement = 1

while running:

    if redBlock.rect.x < 310:
        redBlock.rect.x += 1
    else:
        redBlock.rect.x = -40

    if movement == 1:
        # playerX must come second or old position will overwrite
        # X and Y values are swapped
        userMap2[player.oldPlayerY][player.oldPlayerX][1] = 0
        userMap2[player.playerY][player.playerX][1] = 8
        printMap(userMap2)

        # movement = 0
        # Wall visible drawing loop
        emptyVisGroups()
        drawWalls = drawWallsfunction(player, userMap2)

        printMap(userMap2)
        print("Draw walls ",drawWalls)
        #testList.reverse()

        # Change back to wallDict
        #
        #
        for i in drawWalls:
            if i < 2:
                wallVisL0Group.add(wallList[i])
            if i < 5:
                wallVisL1Group.add(wallList[i])
            elif i < 9:
                wallVisL2Group.add(wallList[i])
            elif i < 14:
                wallVisL3Group.add(wallList[i])
            elif i < 21:
                wallVisL4Group.add(wallList[i])
            elif i < 30:
                wallVisL5Group.add(wallList[i])
            else:
                print("Finding walls that are not drawn")

    del drawWalls[:]

    backGroup.draw(screen)
    monsterGroup.draw(screen)
    # allSprites = pygame.sprite.OrderedUpdates()
    allSprites = pygame.sprite.LayeredUpdates(
        wallVisL6Group, wallVisL5Group, wallVisL4Group, wallVisL3Group,
        wallVisL2Group, wallVisL1Group, wallVisL0Group)
    if movement == 1:
        for s in allSprites:
            print(s.name)

    wallVisL6Group.add(wall98)

    allSprites.draw(screen)
    pygame.display.flip()

    movement = 0

    # KEYBOARD

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Closing...")
            running = False
        key_in = pygame.key.get_pressed()
        mouse_in = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        if key_in[pygame.K_ESCAPE]:
            print("Escaping...")
            running = False

        if key_in[pygame.K_UP] and upHold == 0:
            upHold = 1
        if upHold == 1 and key_in[pygame.K_UP] == 0:
            upHold = 0

            # Facing North ----------------------------
            if player.direction == 0:
                if player.playerY > 0:
                    player.moveUp()
                    movement = 1
                else:
                    print("Top Bounds")
            # Facing East -----------------------------
            elif player.direction == 1:
                if player.playerX < len(userMap2[player.playerY]) - 1:
                    player.moveRight()
                    movement = 1
                else:
                    print("Right Bounds")
            # Facing South ----------------------------
            elif player.direction == 2:
                if player.playerY < len(userMap2) - 1:
                    player.moveDown()
                    movement = 1
                else:
                    print("Bottom Bounds")
            # Facing West -----------------------------
            elif player.direction == 3:
                if player.playerX > 0:
                    player.moveLeft()
                    movement = 1
                else:
                    print("Left Bounds")

            else:
                print("UNKNOWN DIRECTION ERROR")

        if key_in[pygame.K_DOWN]:

            if player.direction == 0:
                if player.playerY < len(userMap2) - 1:
                    player.moveDown()
                    movement = 1
                else:
                    print("Backwards Bottom Bounds")
            elif player.direction == 1:
                if player.playerX > 0:
                    player.moveLeft()
                    movement = 1
                else:
                    print("Backwards Left Bounds")

            elif player.direction == 2:
                if player.playerY > 0:
                    player.moveUp()
                    movement = 1
                else:
                    print("Backwards Top Bounds")

            elif player.direction == 3:
                if player.playerX < len(userMap2[player.playerY]) - 1:
                    player.moveRight()
                    movement = 1
                else:
                    print("Backwards Right Bounds")
            else:
                print("UNKNOWN DIRECTION ERROR")

        if key_in[pygame.K_LEFT]:
            player.direction -= 1
            if player.direction < 0: player.direction = 3
            player.setDirection(player.direction)
            player.printDirection()
            movement = 1

        if key_in[pygame.K_RIGHT]:
            player.direction += 1
            if player.direction > 3: player.direction = 0
            player.setDirection(player.direction)
            player.printDirection()
            movement = 1

        if key_in[pygame.K_a]:
            #print(player.playerX,player.playerY)
            #print("Front Value: %s" % checkTile(player,userMap2, 1,slot=1))
            # player.printDirection()
            # print(userMap.__len__())
            checkBounds(player,userMap2,3)

    gumm.update_caption(player)
    clock.tick(60)

pygame.quit()
sys.exit()
