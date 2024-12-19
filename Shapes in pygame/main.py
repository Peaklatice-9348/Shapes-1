import pygame
from random import randint
pygame.init()
screen=pygame.display.set_mode((600,600))
screen.fill('black')

pygame.display.update()
class Circle():
    def __init__(self,radius,x,y,color,width):
        self.radius = radius
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.circle_surface = screen
    def draw(self):
        self.draw_circle = pygame.draw.circle(self.circle_surface,self.color,(self.x,self.y),self.radius,self.width)
R = randint(0,255)
G = randint(0,255)
B = randint(0,255)
RGB = (R,G,B)
circle1 = Circle(50,300,300,RGB,0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            circle1.radius += 10
    circle1.draw()
    pygame.display.update()
pygame.quit()