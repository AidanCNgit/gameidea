import sys, pygame
from pygame.locals import *
import random
from runnas import file1
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

pygame.init()
screen = pygame.display.set_mode((480, 360))
pygame.font.init()
fps = pygame.time.Clock()
font = pygame.font.Font(r"warty\Pixeled.ttf")
text = font.render('Welcome to PyGame', False, (255, 255, 255))
stupid = file1.othersprites[0]["txbox"]
topen = 0
done = False

class dialogue():
    
    i = 0
    ttext = ""
    
    def __init__(self):
        
        pass
    
    def display(self, text, x, y):
        
        if dialogue.i < len(text) - 1:
            dialogue.ttext = dialogue.ttext + text[dialogue.i]
        else:
            global done
            done = True
        distext = font.render(dialogue.ttext, False, (255, 255, 255))
        screen.blit(distext, (x, y))
        if dialogue.i < len(text) - 1:
            dialogue.i += 1
    
    def instadisplay(self, text, position):
        
        screen.blit(font.render(text, False, (255, 255, 255)), (position))

txbox = dialogue()
        
def open(tdisplay, fight, x=30, y=20):
    
    if fight == 0:
        screen.blit(stupid, (x - 15, y - 10))
    txbox.display(tdisplay, x, y)

def basicopen(text, position):
    
    txbox.instadisplay(text, position)
    
def close():
    
    global done
    done = False
    dialogue.ttext = ""
    dialogue.i = 0