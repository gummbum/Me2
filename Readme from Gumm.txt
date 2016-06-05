I fixed the rendering order.

Still it appears that drawWalls is returning values for walls that are not in
line of sight. I'm sure you can figure this out. :)

You can add monsters and other objects into allSprites if you can manage the
layering. This is not hard. You just need to space out the layer number so
you can insert the objects in a reliable rendering sequence. I like to name
my layers to make them more mnemonic.

You can have:

floor = 0
wayfar = 100
far = 200
far_monster = 250
short = 300
short_monster = 350
shorter = 400
shorter_monster = 450
near = 500
near_monster = 550

These relate to the groupings in the code.

In the code you can have:

wall22 = Wall(4, 0, wayfar)
wall30 = Wall(4, 8, wayfar + 1)
wall23 = Wall(4, 1, wayfar + 1)
wall29 = Wall(4, 7, wayfar + 2)
wall24 = Wall(4, 2, wayfar + 2)
etc...

Hope that helps.
