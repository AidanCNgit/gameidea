import sys, pygame
from pygame.locals import *
import random
import os
import math
from runnas import fight_script, file0, file1, textbox
import json
os.environ['SDL_AUDIODRIVER'] = 'dsp'

#init
pygame.init()
fps = pygame.time.Clock()
screen = pygame.display.set_mode((480, 320))

#get vars
tiles = []
tiless = []
room_collides = []
offset = 0
yoffset = 0
free = 0
topen = 0
tover = 0
cut = 0
direction = "up"
fade = 0
fight = 0
d_id = -1
frm = 1
anim_ticks = 4

sprites = pygame.sprite.Group()

scr_black = file1.othersprites[0]["fade"]


#annoyingly has 2 stay, plus cutscene >:(
def anim(dir):

    global frm
    global anim_ticks

    if dir == "up":

        if frm == 1:
            p.image = pygame.transform.scale(pygame.image.load
        (file1.psprites["pup1"]), (32, 32))
            anim_ticks -= 1
        
        elif frm == 2 or frm == 4:
            p.image = pygame.transform.scale(pygame.image.load
        (file1.psprites["pupidle"]), (32, 32))
            anim_ticks -= 1
        
        elif frm == 3:
            p.image = pygame.transform.scale(pygame.image.load
        (file1.psprites["pup2"]), (32, 32))
            anim_ticks -= 1


    if dir == "down":

        if frm == 1:
            p.image = pygame.transform.scale(pygame.image.load
        (file1.psprites["pdown1"]), (32, 32))
            anim_ticks -= 1
        
        elif frm == 2 or frm == 4:
            p.image = pygame.transform.scale(pygame.image.load
        (file1.psprites["pdownidle"]), (32, 32))
            anim_ticks -= 1
        
        elif frm == 3:
            p.image = pygame.transform.scale(pygame.image.load
        (file1.psprites["pdown2"]), (32, 32))
            anim_ticks -= 1
    
    if dir == "right":

        if frm == 1:
            p.image = pygame.transform.scale(pygame.image.load
        (file1.psprites["pright1"]), (32, 32))
            anim_ticks -= 1
        
        elif frm == 2 or frm == 4:
            p.image = pygame.transform.scale(pygame.image.load
        (file1.psprites["prightidle"]), (32, 32))
            anim_ticks -= 1
        
        elif frm == 3:
            p.image = pygame.transform.scale(pygame.image.load
        (file1.psprites["pright2"]), (32, 32))
            anim_ticks -= 1
        
    if dir == "left":

        if frm == 1:
            p.image = pygame.transform.scale(pygame.image.load
        (file1.psprites["pleft1"]), (32, 32))
            anim_ticks -= 1
        
        elif frm == 2 or frm == 4:
            p.image = pygame.transform.scale(pygame.image.load
        (file1.psprites["pleftidle"]), (32, 32))
            anim_ticks -= 1
        
        elif frm == 3:
            p.image = pygame.transform.scale(pygame.image.load
        (file1.psprites["pleft2"]), (32, 32))
            anim_ticks -= 1

    if anim_ticks == 0:

        if frm <= 3:
            frm += 1 
        else:
            frm = 1

        anim_ticks = 7
           
        


#stuff

class player(pygame.sprite.Sprite):
    
    def __init__(self):
        
        super().__init__()
        self.px = 240
        self.py = 190
        self.col = True
        
        self.image = pygame.transform.scale(pygame.image.load
        (file1.psprites["pupidle"]), (32, 32))
        self.rect = self.image.get_rect()
    
    def draw(self):
        

        self.rect.center = (self.px - 15, self.py)
        if pygame.sprite.spritecollideany(self, sprites):
            self.col = True
        else:
            self.col = False
        screen.blit(self.image, self.rect)

#other stuff

class sprite(pygame.sprite.Sprite):
    
    def __init__(self, id=0):
        
        super().__init__()
        self.id = id
        self.sprx = curroom.tileind["locations"][1]["sprites"][self.id][0]
        self.spry = curroom.tileind["locations"][1]["sprites"][self.id][1]
        
        self.image = pygame.transform.scale(pygame.image.load
        (file1.psprites["pupidle"]), (40, 40))
        self.rect = self.image.get_rect()
        
    def draw(self):

        self.sprx = curroom.tileind["locations"][1]["sprites"][self.id][0]
        self.spry = curroom.tileind["locations"][1]["sprites"][self.id][1]
        self.rect.center = (self.sprx + offset, self.spry + yoffset)
        room_collides.append((self.sprx + offset, self.spry + yoffset))
        room_collides.append((self.sprx + offset, self.spry + yoffset))
        if pygame.sprite.collide_rect(self, p):
            global d_id
            d_id = self.id
        screen.blit(self.image, self.rect)
        
    
    
        
#more stuff

class tile(pygame.sprite.Sprite):
    
    tiles = 0
    
    def __init__(self, tt, tx=120, ty=90):
        
        super().__init__()
        tile.tiles += 1
        
        self.tx = tx
        self.ty = ty
        self.image = file1.tsprites["grass"]
        self.rect = self.image.get_rect()
        
    def draw(self, tt, tx=120, ty=90):
        
        self.image = file1.tsprites[tt[0]]
        self.rect.center = (tx + offset, ty + yoffset)
        if tt[1] == 1:
            room_collides.append((tx + offset - 4, ty + yoffset))
            room_collides.append((tx + offset + 4, ty + yoffset))
        screen.blit(self.image, self.rect)
        
        


p = player()


#ROOM CREATION:
#max x + y is 50
#one door per zone max:
# ul   |    u     |   ur
# ml   |    m     |   mr
# dl   |    d     |   dr
#Not every zone needs a door.
#FOR DOORS: 10 IS BEST Y, IF U YOU ONLY NEED X 240  
#tile placer is warty room creator on scratch
#but I recommend turbowarp cuz infinite clones = infinite tiles

class room():
    

    def __init__(self, xlen, ylen, tileind):
        
        self.xlen = xlen
        self.ylen = ylen
        self.tileind = tileind
        
    def load(self):
        
        room_collides.clear()
        tile_loadin = self.tileind["locations"][0]["tiles"]
        t = tile(tile_loadin[0])
        
        screen.fill((0, 0, 0))
        
        for i in range(self.ylen):
            for b in range(self.xlen):
                t.draw((tile_loadin[(i * self.xlen) + b]), (b * 32), 
                16 + (i * 32))
        
        tiless.append(1)
        tiles.append(t)
        
        if len(tiles) > 3:
            
            del tiles[0]
            del tiless[0]
                
    def unload(self):
        
        screen.fill((0, 0, 0))

roomind = file1.rooms[0]["room0"]
curroom = room(26, 20, roomind)
curroom.load()

henry = sprite(0)
sprites.add(henry)


while True and fight == 0:
    
    load = 0
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    
    #key presses
    keys = pygame.key.get_pressed()
    
    if keys[K_RIGHT] and cut == 0:

                
        if not(file0.check_collision("right", roomind["locations"][2][file0.findzone(p.px, p.py) + "doors"], cut, p)):

            cut = 1
            fade = 1

        if offset < -((curroom.xlen - 3) * 32 - 504) or p.px < 240:
            if file0.check_collision("right", room_collides, cut, p):
                p.px += 4
                anim("right")
        else:
            if file0.check_collision("right", room_collides, cut, p):
                offset -= 4
                anim("right")

        direction = "right"

    if keys[K_LEFT] and cut == 0:

                
        if not(file0.check_collision("left", roomind["locations"][2][file0.findzone(p.px, p.py) + "doors"], cut, p)):

            cut = 1
            fade = 1
        
        if offset > 14 or p.px > 240:
            if file0.check_collision("left", room_collides, cut, p):
                p.px -= 4
                anim("left")
        else:
            if file0.check_collision("left", room_collides, cut, p):
                offset += 4
                anim("left")

        direction = "left"

        
        
    if keys[K_UP] and cut == 0:
        
        if not(file0.check_collision("up", roomind["locations"][2][file0.findzone(p.px, p.py) + "doors"], cut, p)):

            cut = 1
            fade = 1

        if yoffset > -4 or p.py > 160:
            if file0.check_collision("up", room_collides, cut, p):
                p.py -= 4
                anim("up")
        else:
            if file0.check_collision("up", room_collides, cut, p):
                yoffset += 4
                anim("up")
        
        direction = "up"
        
            
    if keys[K_DOWN] and cut == 0:

        if not(file0.check_collision("down", roomind["locations"][2][file0.findzone(p.px, p.py) + "doors"], cut, p)):

            cut = 1
            fade = 1
        
        if yoffset < -308 or p.py < 160:
            if file0.check_collision("down", room_collides, cut, p):
                p.py += 4
                anim("down")
        else:
            if file0.check_collision("down", room_collides, cut, p):
                yoffset -= 4
                anim("down")
        
        direction = "down"
    

    curroom.load()
    henry.draw()
    p.draw()
    
    
    if keys[K_z] and p.col == True:
        
        if topen == 0:
            cut = 1
            topen = 1
            tover = 0
            
        pygame.time.delay(200)
        
    if topen == 1:
        textbox.open(curroom.tileind["otherdata"][0]["dialogue"][d_id][tover], 0)
        if textbox.done == True and tover < len(curroom.tileind["otherdata"][0]["dialogue"][d_id]):
            if keys[K_z]:
                textbox.close()
                tover += 1
        if tover >= len(curroom.tileind["otherdata"][0]["dialogue"][d_id]):
            tover = -1
            topen = 0
            cut = 0
    else:
        textbox.close()
    
    #this suks but i gotta hav it
    if fade > 0 and fade <= 350 and cut == 1:
        scr_black.set_alpha(fade)
        fade += 15
        screen.blit(scr_black, (0, 0))
    elif fade >= 350 and fade <= 700 and cut == 1:
        if fade == 361:
            roomind = file1.rooms[0][roomind["locations"][2]["leadsto"][file1.zoneind[file0.findzone(p.px, p.py)]]]
            curroom = room(roomind["otherdata"][0]["length"], roomind["otherdata"][0]["height"], roomind)
        if direction == "up":
            p.py = 250
            yoffset = -320
        if direction == "right":
            p.px = 64
            offset = 0
        if direction == "left":
            p.px = 420
            offset = -((curroom.xlen - 3) * 32 - 488)
        if direction == "down":
            p.py = 32
            yoffset = 0
        scr_black.set_alpha(abs(fade - 700))
        fade += 15
        screen.blit(scr_black, (0, 0))
    elif fade > 700:
        fade = 0
        cut = 0
    
    if keys[K_l]:
        print(p.px, p.py)
        print(file0.findzone(p.px, p.py))

    if keys[K_g]:
        fight = 1
    
    if direction == "up" and not(keys[K_UP]):
        p.image = pygame.transform.scale(pygame.image.load
        (file1.psprites["pupidle"]), (32, 32))


    

    pygame.display.update()
    fps.tick(30)

while True and fight == 1:
    
    fight_script.fight()