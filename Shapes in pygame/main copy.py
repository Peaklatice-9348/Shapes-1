import pygame
from random import randint
pygame.init()
screen=pygame.display.set_mode((600,600))
screen.fill('black')

pygame.display.update()
class Rectangle():
    def __init__(self,radius,x,y,color,width):
        self.radius = radius
        self.x = x
        self.y = y
        self.color = color
        self.width = width
    def draw(self):
        pygame.draw.rect(screen,(self.color),(self.x,self.y,self.radius*2,self.radius),border_radius=self.width)
R = randint(0,255)
G = randint(0,255)
B = randint(0,255)
RGB = (R,G,B)
circle1 = Rectangle(100,100,100,RGB,0)

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