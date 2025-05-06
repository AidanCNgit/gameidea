import sys, pygame
from pygame.locals import *
import os
from runnas import textbox, file1

os.environ['SDL_AUDIODRIVER'] = 'dsp'

sys.path.insert(0, r"\runnas")

pygame.init()
fps = pygame.time.Clock()
screen = pygame.display.set_mode((480, 320))

button = 0 

#POINTER==================================================
class pointer(pygame.sprite.Sprite):
    
    def __init__(self, x=28, y=260):
        
        self.x = x
        self.y = y
        
        self.image = file1.fighting[0]["pointer"]
        self.rect = self.image.get_rect()
        
    def move(self, direction):
        
        if direction == "r" and button == 0:
            self.x += 64
        elif direction == "l" and button == 1:
            self.x -= 64
        elif direction == "d" and button == 0:
            self.y += 32
        elif direction == "u" and button == 2:
            self.y -= 32
        
        if (self.x, self.y) == (28, 260):
            return 0
        elif (self.x, self.y) == (28, 292):
            return 2
        elif (self.x, self.y) == (92, 260):
            return 1
        
        
    def draw(self):
            
        self.rect.center = (self.x, self.y)
        screen.blit(self.image, self.rect)


fightpointer = pointer()
#POINTER=====================================================================

#ENEMY=============================================================
class enemy():
    def __init__(self, hp=500, sprite=file1.psprites["pupidle"]):
        
        self.image = pygame.transform.scale(pygame.image.load(sprite), (64, 64))
        self.rect = self.image.get_rect()
        self.hp = hp
        
    def draw(self):
        
        self.rect.center = (300, 120)
        screen.blit(self.image, self.rect)

enemie = enemy()
#ENEMY===========================================================

#ATTACK===========================================================
class attack():
    
    def __init__(self, id=0):
        
        self.id = id
        self.image = file1.fighting[0]["slash"]
        self.rect = self.image.get_rect()
        
    def strike(self):
        
        self.rect.center = (300, 120)
        enemie.hp -= 100
        screen.blit(self.image, self.rect)
        
#ATTACK=============================================================
atk = attack()
def fight():
    global button
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            
    keys = pygame.key.get_pressed()
    
    screen.fill((0, 0, 0))
    
    textbox.open("dog._", 0, 175, 230)
    textbox.basicopen("yo", (0, 120))
    
    if keys[K_UP]:
        button = fightpointer.move("u")
        fightpointer.draw()
        pygame.time.delay(20)

    if keys[K_DOWN]:
        button = fightpointer.move("d")
        fightpointer.draw()
        pygame.time.delay(20)
        
    if keys[K_RIGHT]:
        button = fightpointer.move("r")
        fightpointer.draw()
        pygame.time.delay(20)
    
    if keys[K_LEFT]:
        button = fightpointer.move("l")
        fightpointer.draw()
        pygame.time.delay(20)
    
    screen.blit(file1.fighting[0]["bbox"], (0, 190))
    fightpointer.draw()
    enemie.draw()
    if keys[K_r]:
        atk.strike()
        pygame.display.update()
        pygame.time.delay(300)
        print(enemie.hp)
    pygame.display.update()
    fps.tick(30)