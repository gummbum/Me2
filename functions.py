def printPlayer(player):
    print(player.name)

def printMap(mapList):
    height = len(mapList)
    for i in range(0, height):
        print(mapList[i])


def print_X_Line(mapList, Xpos):
    print("X LINE")
    print(mapList[Xpos])


def print_Y_Line(mapList, Ypos):
    print("Y LINE")
    for i in range(len(mapList)):
        print(mapList[i][Ypos])


def printSlot(player, mapList, Xpos, Ypos, slot=0):
    print("SPOT")
    # subscriptable -  at the moment the list spot only contains a '1'
    #              -  and not [2,0] at the moment
    print(mapList[player.playerX][player.playerY - 1][slot])


def checkTile(player, mapping, amount, section=0, slot=0):
    """ Check any tile relative to the player's position

        player, map, how far ahead, how far left/right, slot(?)"""
    player.front = None
    if player.direction == 0:
        # When close to left map edge, checkTile (-2) will check the very RIGHT edge i.e. L=[1]; L[-1] = 1
        if player.playerX < 2 and section < -1:
            print("checkTile will hit out of left map")
        else:
            player.front = mapping[player.playerY - amount][player.playerX + section][slot]
    elif player.direction == 1:
        if player.playerY < 2 and section < -1:
            print("checkTile will hit out of top map")
        else:
            player.front = mapping[player.playerY + section][player.playerX + amount][slot]
    elif player.direction == 2:
        player.front = mapping[player.playerY + amount][player.playerX + (section*-1)][slot]
        #print("First Details %s, %s" % (section, player.playerX + (section*-1)))
    elif player.direction == 3:
        player.front = mapping[player.playerY + (section*-1)][player.playerX - amount][slot]
    return player.front