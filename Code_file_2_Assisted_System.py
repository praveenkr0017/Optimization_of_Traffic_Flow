import pygame
import time
import math
import random

eff = 0
black = (0, 0, 0)
white = (255, 255, 255)
red = (128, 0, 0)
green = (0, 128, 0)
gexit = False
flag = 0
to0 = to = time.time()

def t():
    """ universal time """
    return time.time() - to

class car:
    global l
    
    def __init__(self, n, d):
        self.n = n
        self.delt = random.uniform(0, 0.85)
        self.d = d
        global x
        self.x = 800 - self.n * self.d
        self.y = 300
        
    def stim(self):
        if self.n > 1:
            return l[self.n - 1].x - l[self.n].x - 20
        else:
            return 0
            
    def v(self):
        if self.n == 0:
            if signal() == red:
                return 0
            return 80 * (1 - math.exp(-2 * t()))
        else:
            if t() - sum(lags[1:self.n]) < lags[self.n]:
                return 0
            else:
                return l[-1 + self.n].v() * (1 - math.exp(-t()))

def signal():
    global flag
    global to
    if t() < 5 and flag == 0:
        return red
    flag = 1
    if to == to0:
        to += 5
    return green

l = []
for i in range(65):
    l.append(car(i, 20))
lags = [c.delt for c in l]

pygame.init()
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()
currt = t()
dt = 0

while not gexit:
    currt = t()
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            gexit = True
            
    screen.fill(white)
    
    for c in l:
        pygame.draw.rect(screen, black, [c.x, c.y, 10, 10])
        c.x += (c.v() + c.stim() * 0.27) * dt
        if c.x >= 820:
            eff += 1
    
    # road
    pygame.draw.rect(screen, black, [0, 250, 1200, 5])
    pygame.draw.rect(screen, black, [0, 350, 1200, 5])
    
    # sign
    pygame.draw.rect(screen, signal(), [820, 250, 5, 100])
    dt = t() - currt
    
    if t() > 40:
        print(eff / 10000)
        print(2 * math.atan(eff / 10000) / math.pi)
        break
    
    pygame.display.update()
    clock.tick(5000)

pygame.quit()
quit()
