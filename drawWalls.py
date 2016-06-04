from functions import *

testList = []

def drawWallsfunction(player,userMap2):
    try:
        if checkTile(player, userMap2, 0, -1) == 2:
            testList.append(0)
        if checkTile(player, userMap2, 0, 1) == 2:
            testList.append(1)
    except IndexError:
        pass
        #print("Can't access left and right")
    # Left, Right then Front Wall - LEVEL 1                 LEVEL ONE
    try:
        if checkTile(player, userMap2, 1, -1) == 2:
            testList.append(2)
        if checkTile(player, userMap2, 1, 1) == 2:
            testList.append(4)
        if checkTile(player, userMap2, 1, 0) == 2:
            testList.append(3)
    except IndexError:
        print("Level 1 - Trying to reach too far out")

    # Check FAR LEFT - LEVEL 2                              LEVEL TWO
    try:
        if checkTile(player, userMap2, 2, -2) == 2:
            testList.append(5)
            print(checkTile(player, userMap2, 3, -2, 1))
    except IndexError:
        print("Level 2 - Far Left wall out of bounds")
    # Check ahead LEVEL 2
    try:
        if checkTile(player, userMap2, 2, -1) == 2:
            testList.append(6)
    except IndexError:
        print("Level 2 - Trying too far out ahead")
        # FAR RIGHT - LEVEL 2
    try:
        if checkTile(player, userMap2, 2, 2) == 2:
            testList.append(9)
    except IndexError:
        print("Level 2 - Far Right Side out of bounds")
    # Check ahead LEVEL 2
    try:
        if checkTile(player, userMap2, 2, 1) == 2:
            testList.append(8)
        if checkTile(player, userMap2, 2, 0) == 2:
            testList.append(7)
    except IndexError:
        print("Level 2 - Trying too far out")

    # Check FAR LEFT - LEVEL 3                               LEVEL THREE
    try:
        if checkTile(player, userMap2, 3, -2) == 2:
            testList.append(10)
            print(checkTile(player, userMap2, 3, -2, 1))
    except IndexError:
        print("Level 3 - Far Left wall out of bounds")
    # Check ahead LEVEL 3
    try:
        if checkTile(player, userMap2, 3, -1) == 2:
            testList.append(11)
    except IndexError:
        print("Level 3 - Trying too far out")
    # Check FAR RIGHT - LEVEL 3
    try:
        if checkTile(player, userMap2, 3, 2) == 2:
            testList.append(14)
    except IndexError:
        print("Level 3 - Far Right Side out of bounds")
    # Check ahead LEVEL 3
    try:
        if checkTile(player, userMap2, 3, 1) == 2:
            testList.append(13)
        if checkTile(player, userMap2, 3, 0) == 2:
            testList.append(12)
    except IndexError:
        print("Level 3 - Trying too far out")

    # Check FAR LEFT - LEVEL 4                               LEVEL FOUR
    try:
        if checkTile(player, userMap2, 4, -3) == 2:
            testList.append(15)
    except IndexError:
        print("Level 4 - Wall 13 out of bounds")
    try:
        if checkTile(player, userMap2, 4, -2) == 2:
            testList.append(16)
    except IndexError:
        print("Level 4 - Wall 14 out of bounds")
    try:
        if checkTile(player, userMap2, 4, -1) == 2:
            testList.append(17)
    except IndexError:
        print("Level 4 - Trying too far out")

    # Check FAR RIGHT - LEVEL 4
    try:
        if checkTile(player, userMap2, 4, 3) == 2:
            testList.append(21)
    except IndexError:
        print("Level 4 - Wall 19 out of bounds")
    try:
        if checkTile(player, userMap2, 4, 2) == 2:
            testList.append(20)
    except IndexError:
        print("Level 4 - Wall 18 out of bounds")

    # Check ahead LEVEL 4
    try:
        if checkTile(player, userMap2, 4, 1) == 2:
            testList.append(19)
        if checkTile(player, userMap2, 4, 0) == 2:
            testList.append(18)
    except IndexError:
        print("Level 4 - Trying too far out")

    # Check ahead LEVEL 5
    try:
        if checkTile(player, userMap2, 5, -4) == 2:
            testList.append(22)
    except IndexError:
        print("Level 5 - Wall 20 far out")
    try:
        if checkTile(player, userMap2, 5, -3) == 2:
            testList.append(23)
    except IndexError:
        print("Level 5 - Wall 21 far out")
    try:
        if checkTile(player, userMap2, 5, -2) == 2:
            testList.append(24)
    except IndexError:
        print("Level 5 - Wall 22 far out")
    try:
        if checkTile(player, userMap2, 5, 4) == 2:
            testList.append(30)
    except IndexError:
        print("Level 5 - Far Right wall out of bounds")
    try:
        if checkTile(player, userMap2, 5, 3) == 2:
            testList.append(29)
    except IndexError:
        print("Level 5 - Wall 27 out")
    try:
        if checkTile(player, userMap2, 5, 2) == 2:
            testList.append(28)
    except IndexError:
        print("Level 5 - Wall 26 out")
    try:
        if checkTile(player, userMap2, 5, -1) == 2:
            testList.append(25)
        if checkTile(player, userMap2, 5, 0) == 2:
            testList.append(26)
        if checkTile(player, userMap2, 5, 1) == 2:
            testList.append(27)
    except IndexError:
        print("Level 5 - Too far forward")

    return testList