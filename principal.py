

import sys, pygame
from pygame.locals import *
from Tkconstants import TOP
 
import time
from time import sleep
WIDTH = 1000
HEIGHT = 100


theClock = pygame.time.Clock()

class Dragon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/dragon.png", False)
        self.rect = self.image.get_rect()
        self.rect.centerx = 60
        self.rect.centery = 60
        self.speed = [0.5]

       
    def actualizar(self, time):
        print self.rect.centerx
        self.rect.centerx += self.speed[0] * time
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        if self.rect.right <= 0 or self.rect.bottom >= HEIGHT:
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time
    def moverArriba(selfs,time):
        self.rect.centery = 0
        
def load_image(filename, transparent=True):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image
 
# ---------------------------------------------------------------------
 
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pruebas Pygame")
    dragon = Dragon()
    
    clock = pygame.time.Clock()
     

    while True:
       
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
       
        time = clock.tick(62)
        screen.blit(dragon.image, dragon.rect)
        dragon.actualizar(time)
        pygame.display.flip()
        pygame.display.update()
        theClock.tick(10)
        pygame.display.flip()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()