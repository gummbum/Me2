import pygame


class Stuff:
    ticks_per_cycle = 20
    tick = 0


def update_caption(player):
    Stuff.tick += 1
    if Stuff.tick % Stuff.ticks_per_cycle == 0:
        pygame.display.set_caption('Facing {} | Position {}'.format(player.direction, (player.playerY, player.playerX)))
