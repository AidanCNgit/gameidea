import sys, pygame
import os

#movement

def check_collision(dir, room_collides, cut, p):
    
    if dir == "right":
        for i in room_collides:
            if (p.px > i[0] - 8 and p.px < i[0] + 8) and (p.py > i[1] - 32 and p.py < i[1] + 32):
                return False
    if dir == "left":
        for i in room_collides:
            if (p.px - 32 > i[0] - 8 and p.px - 32 < i[0] + 8) and (p.py > i[1] - 32 and p.py < i[1] + 32):
                return False
    if dir == "up":
        for i in room_collides:
            if (p.px > i[0] - 4 and p.px < i[0] + 32) and (p.py < i[1] + 36 and p.py > i[1] - 32):
                return False
    if dir == "down":
        for i in room_collides:
            if (p.px > i[0] - 4 and p.px < i[0] + 32) and (p.py < i[1] and p.py > i[1] - 36):
                return False
    if cut == 0:
        return True

def findzone(x, y):

    if y < 160:
        if x < 220:
            return "ul"
        elif x < 250:
            return "u"
        else:
            return "ur"
    elif y < 210:
        if x < 220:
            return "ml"
        elif x < 250:
            return "m"
        else:
            return "mr"
    else:
        if x < 220:
            return "dl"
        elif x < 250:
            return "d"
        else:
            return "dr"


    