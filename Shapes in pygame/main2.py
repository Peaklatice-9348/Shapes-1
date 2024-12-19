import pygame
from random import randint
pygame.init()
screen=pygame.display.set_mode((600,600))
screen.fill('white')

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

circle1 = Circle(50,300,300,'red',0)
circle2 = Circle(40,300,300,'yellow',0)
circle3 = Circle(30,300,300,'green',0)
circle4 = Circle(20,300,300,'blue',0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            circle1.draw()
            circle2.draw()
            circle3.draw()
            circle4.draw()
        elif event.type == pygame.MOUSEBUTTONUP:
            circle1.radius += 40
            circle2.radius += 30
            circle3.radius += 20
            circle4.radius += 10
        elif event.type == pygame.MOUSEMOTION:
            x,y = pygame.mouse.get_pos()
            circle = Circle(10,x,y,'black',0)
            circle.draw()
    pygame.display.update()
pygame.quit()