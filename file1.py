import sys, pygame
import os
import json



psprites = {
    
    "pupidle" : r"warty\othersprites\pupidle1.png",
    "pup1" : r"warty\othersprites\pup1.png",
    "pup2" : r"warty\othersprites\pup2.png",

    "pdownidle" : r"warty\othersprites\pdownidle.png",
    "pdown1" : r"warty\othersprites\pdown1.png",
    "pdown2" : r"warty\othersprites\pdown2.png",

    "prightidle" : r"warty\othersprites\prightidle.png",
    "pright1" : r"warty\othersprites\pright1.png",
    "pright2" : r"warty\othersprites\pright2.png",

    "pleftidle" : r"warty\othersprites\pleftidle.png",
    "pleft1" : r"warty\othersprites\pleft1.png",
    "pleft2" : r"warty\othersprites\pleft2.png"
}
tsprites = {
    
    "tile1" : pygame.transform.scale(pygame.image.load(r"warty\tiles\tile.png"), (32, 32)),
    "grass" : pygame.transform.scale(pygame.image.load(r"warty\tiles\grass.png"), (32, 32)),
    "wall1" : pygame.transform.scale(pygame.image.load(r"warty\tiles\wall1.png"), (32, 32)),
    "path1" : pygame.transform.scale(pygame.image.load(r"warty\tiles\path1.png"), (32, 32)),
    "path2" : pygame.transform.scale(pygame.image.load(r"warty\tiles\path2.png"), (32, 32))

}
othersprites = {

    "fade" : pygame.transform.scale(pygame.image.load(r"warty\othersprites\blackscreen.png"), (480, 320)),
    "txbox" : pygame.transform.scale(pygame.image.load(r"warty\othersprites\stupid.png"), (200, 96))
},
rooms = {

    "room0" : json.load(open(r"warty\rooms\r_0.json")),
    "room1" : json.load(open(r"warty\rooms\r_1.json")),
    "room2" : json.load(open(r"warty\rooms\r_2.json")),
    "room3" : json.load(open(r"warty\rooms\r_3.json"))
},
fighting = {

    "pointer" : pygame.transform.scale(pygame.image.load(r"warty\othersprites\fight1.png"), (16, 16)),
    "bbox" : pygame.transform.scale(pygame.image.load(r"warty\othersprites\fight2.png"), (160, 160)),
    "slash" : pygame.transform.scale(pygame.image.load(r"warty\othersprites\slash.png"), (64, 64)),

},
zoneind = {

      "ul" : 0,
      "u" : 1,
      "ur" : 2,
      "ml" : 3,
      "m" : 4,
      "mr" : 5,
      "dl" : 6,
      "d" : 7,
      "dr" : 8
}