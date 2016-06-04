import pygame, os

class Player():
    dictDirection = {0: 'Up', 1: 'Right', 2: 'Down', 3: 'Left'}

    def __init__(self):
        self.name = "Player"
        self.switch = 0

    def setStartPosition(self, posX, posY):
        self.playerX = posX
        self.playerY = posY
        self.oldPlayerX = posX
        self.oldPlayerY = posY

    def setStartDirection(self, direction):
        self.direction = direction

    def setPosition(self, posX, posY):
        self.playerX = posX
        self.playerY = posY
        self.oldPlayerX = posX
        self.oldPlayerY = posY

    def setDirection(self, direction):
        self.direction = direction
        self.oldPlayerX = self.playerX
        self.oldPlayerY = self.playerY

    def switchPositions(self):
        self.switch = self.playerX
        self.oldswitch = self.oldPlayerX

        self.playerX = self.playerY
        self.oldPlayerX = self.oldPlayerY

        self.playerY = self.switch
        self.oldPlayerY = self.oldswitch

    def printDirection(self):
        print("You are looking %s" % Player.dictDirection[self.direction])

    def printPosition(self):
        print("New X %s,Y %s:   Old X %s,Y %s" % (self.playerX, self.playerY, self.oldPlayerX, self.oldPlayerY))

    def moveUp(self):
        self.oldPlayerY = self.playerY
        self.playerY -= 1

    def moveDown(self):
        self.oldPlayerY = self.playerY
        self.playerY += 1

    def moveRight(self):
        self.oldPlayerX = self.playerX
        self.playerX += 1

    def moveLeft(self):
        self.oldPlayerX = self.playerX
        self.playerX -= 1


class Block(pygame.sprite.Sprite):
    def __init__(self, size, x, y, color):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((size))
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y


class Wall(pygame.sprite.Sprite):
    def __init__(self, wallNum, wallNum2):
        pygame.sprite.Sprite.__init__(self)

        self.string = str(wallNum)
        self.string2 = str(wallNum2)
        self.filename = 'data/blocks/wall800_' + self.string + '_' + self.string2 + '.png'
        # print(self.filename)

        self.image = pygame.image.load(os.path.join(self.filename)).convert()
        self.rect = self.image.get_rect()

        self.color = self.image.get_at((0, 0))
        self.image.set_colorkey((self.color))
