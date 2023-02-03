import pygame as pg
from pygame.locals import (K_UP, K_LEFT, K_RIGHT, K_DOWN)
from math import asin
from math import sqrt
from math import sin
from math import cos

pg.init()

colors = [
(255,255,255),
(40, 40, 218),
(204, 41, 54),
(40, 40, 218),
(0, 0, 0),
(40, 40, 218),
(204, 41, 54),
(40, 40, 218),
(204, 41, 54),
(40, 40, 218),
(204, 41, 54),
(204, 41, 54),
(40, 40, 218),
(40, 40, 218),
(204, 41, 54),
(204, 41, 54),
]
team = [True, True, False, True, True, True, False, True, False, True, False, False, True, True, False, False]

VINDU_BREDDE = 380
VINDU_HOYDE  = 762
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

class Hole:
    def __init__(self, x, y, vindusobjekt):
        self.vindusobjekt = vindusobjekt
        self.x = x
        self.y = y
        
    def draw(self):
        pg.draw.circle(self.vindusobjekt, (0,0,0), (self.x, self.y), 30)

class Lin:
    def __init__(self, x, y, x_fart, y_fart, vindusobjekt):
        self.x = x
        self.y = y
        self.x_fart = x_fart
        self.y_fart = y_fart
        self.vindusobjekt = vindusobjekt

    def draw(self):
        pg.draw.line(self.vindusobjekt, (140, 0, 0), (self.x, self.y), (self.x_fart,self.y_fart), 3) 
        
        
        
class Ball:
    i = 0
    def __init__(self, x, y, x_fart, y_fart, radius, vindusobjekt):
        self.x = x
        self.y = y
        self.x_fart = x_fart
        self.y_fart = y_fart
        self.radius = radius
        self.vindusobjekt = vindusobjekt
        self.color = colors[Ball.i]
        self.team = team[Ball.i]
        self.scratched = False
        Ball.i += 1
  
    def draw(self):
        if not self.scratched:
            pg.draw.circle(self.vindusobjekt, self.color, (self.x, self.y), self.radius) 

    def move(self):
        if (abs(self.x_fart) <= 0.003): self.x_fart = 0
        if (abs(self.y_fart) <= 0.003): self.y_fart = 0
        if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= self.vindusobjekt.get_width()):
            self.x_fart = -self.x_fart
              
        if ((self.y - self.radius) <= 0) or ((self.y + self.radius) >= self.vindusobjekt.get_height()):
            self.y_fart = -self.y_fart
    
        self.x += self.x_fart
        self.y += self.y_fart
        
        self.x_fart = self.x_fart * 9995 / 10000
        self.y_fart = self.y_fart * 9995 / 10000
    

def dist(ball1, ball2):
    x_dist = ball1.x - ball2.x
    y_dist = ball1.y - ball2.y
    d = sqrt(x_dist**2 + y_dist**2)
    return d

def ang(ball1,ball2):
    r = (ball1.y - ball2.y) / (dist(ball1,ball2))
    ans = asin(r)
    return ans

def col(ball1,ball2):
    theta = ang(ball1,ball2)
    perpVel1 = cos(theta) * ball1.x_fart - sin(theta) * ball1.y_fart
    vel1 = sin(theta) * ball1.x_fart + cos(theta) * ball1.y_fart
    perpVel2 = cos(theta) * ball2.x_fart - sin(theta) * ball2.y_fart
    vel2 = sin(theta) * ball2.x_fart + cos(theta) * ball2.y_fart
    save = perpVel1
    perpVel1 = perpVel2
    perpVel2 = save
    newX1 = cos(theta) * perpVel1 + sin(theta) * vel1
    newY1 = - sin(theta) * perpVel1 + cos(theta) * vel1
    newX2 = cos(theta) * perpVel2 + sin(theta) * vel2
    newY2 = - sin(theta) * perpVel2 + cos(theta) * vel2
    ball1.x_fart = newX1
    ball1.y_fart = newY1
    ball2.x_fart = newX2
    ball2.y_fart = newY2
    
    ball1.x += 2 * ball1.x_fart
    ball1.y += 2 * ball1.y_fart
    ball2.x += 2 * ball2.x_fart
    ball2.y += 2 * ball2.y_fart

balls = []
whiteBall = Ball(190, 550, 0, 0, 20, vindu)
balls.append(whiteBall)

balls.append(Ball(190, 300, 0, 0, 20, vindu))
balls.append(Ball(165, 260, 0, 0, 20, vindu))
balls.append(Ball(215, 260, 0, 0, 20, vindu))

blackBall = Ball(190, 220, 0, 0, 20, vindu)
balls.append((blackBall))

balls.append(Ball(140, 220, 0, 0, 20, vindu))
balls.append(Ball(240, 220, 0, 0, 20, vindu))
balls.append(Ball(165, 180, 0, 0, 20, vindu))
balls.append(Ball(215, 180, 0, 0, 20, vindu))
balls.append(Ball(265, 180, 0, 0, 20, vindu))
balls.append(Ball(115, 180, 0, 0, 20, vindu))
balls.append(Ball(190, 140, 0, 0, 20, vindu))
balls.append(Ball(140, 140, 0, 0, 20, vindu))
balls.append(Ball(240, 140, 0, 0, 20, vindu))
balls.append(Ball( 90, 140, 0, 0, 20, vindu))
balls.append(Ball(290, 140, 0, 0, 20, vindu))

holes = []
holes.append(Hole(5,5,vindu))
holes.append(Hole(375,757,vindu))
holes.append(Hole(375,0,vindu))
holes.append(Hole(5,757,vindu))
holes.append(Hole(0,381,vindu))
holes.append(Hole(380,381,vindu))

pg.display.set_caption("POOL")

fortsett = True
load = False
shotAng = - 1.57
power = 0
while fortsett:   
    if blackBall.scratched:
        break
    
    if whiteBall.scratched:
        whiteBall.scratched = False
        whiteBall.x = 190
        whiteBall.y = 550
        whiteBall.x_fart = 0
        whiteBall.y_fart = 0
        
    
    trykkede_taster = pg.key.get_pressed()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    vindu.fill((0, 100, 0))
    fartSum = 0
    
    for hole in holes:
        hole.draw()
    
    for ball in balls:
        ball.draw()
        ball.move()
        fartSum += abs(ball.x_fart) + abs(ball.y_fart)
    


    if load and fartSum == 0:
        power += 0.0003
        lin = Lin(whiteBall.x,whiteBall.y,whiteBall.x + power * 150 * cos(shotAng),whiteBall.y + power * 150 * sin(shotAng),vindu)
        lin.draw()
        if power >= 0.60 or not trykkede_taster[K_UP]:
            whiteBall.x_fart = cos(shotAng) * power
            whiteBall.y_fart = sin(shotAng) * power
            power = 0
    
    if load and fartSum != 0:
        load = False

    if fartSum == 0 and not load:
        if (trykkede_taster[K_LEFT]): shotAng -= 0.001
        if (trykkede_taster[K_RIGHT]): shotAng += 0.001
        lin = Lin(whiteBall.x,whiteBall.y,whiteBall.x + 150 * cos(shotAng),whiteBall.y + 150 * sin(shotAng),vindu)
        lin.draw()
        if (trykkede_taster[K_UP]) and not load:
            load = True
            
    for ball1 in balls:
        for ball2 in balls:
            if (ball1 == ball2): continue
            if (dist(ball1,ball2) <= 40 and not (ball1.scratched or ball2.scratched)):
                col(ball1,ball2)
    
    for ball in balls:
        for hole in holes:
            if (dist(hole,ball) <= 33) and ball.x_fart**2 + ball.y_fart**2 <= 0.2:
                ball.scratched = True
    
    pg.display.flip()
pg.quit()