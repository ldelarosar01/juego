

import sys, pygame
from pygame.locals import *
from Tkconstants import TOP
 
import time
from time import sleep
WIDTH = 1000
HEIGHT = 500


theClock = pygame.time.Clock()
class Nubes(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/nubes.png", False)
        self.rect = self.image.get_rect()
        self.rect.centerx = 1000
        self.rect.centery = 200
        self.speed = [0.5]
    

        
    def actualizarNubes(self, time):
        print self.rect.centerx
        self.rect.centerx += self.speed[0] * 21
        print self.rect.centerx
        if self.rect.centerx <= WIDTH:
            self.rect.centerx = 100
        if self.rect.centerx >= WIDTH :
            self.rect.centerx = -1500
         
        self.rect.centerx += self.speed[0] * 30
    

class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/cactus.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = 900
        self.rect.centery = 400
        self.speed = [0.5]
    
    def actualizarCactus(self,time):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/cactus.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = 10000
        self.rect.centery = 400
        self.speed = [0.5]

        
        
class Dragon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/dragon.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.centery = 400
        self.speed = [0.5]

       
    def actualizar(self, time):
        print self.rect.centerx
        self.rect.centerx += self.speed[0] * time
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        if self.rect.right <= 0 or self.rect.bottom >= HEIGHT:
            self.speed[1] = -self.speed[0]
            self.rect.centery += self.speed[1] * time
            
    def saltar(self, time, keys):
        if self.rect.top >= 0:
            if keys[K_UP]:
                self.rect.centery -= self.speed * time
       
                
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
    pygame.display.set_caption("Juegecito Pygame")
    background_image = load_image('images/fondo.jpg') # cargamos la imagen de fondo
    dragon = Dragon()
    cactus = Cactus()
    nubes = Nubes()
    clock = pygame.time.Clock()
     

    while True:
        time = clock.tick(26)
        keys = pygame.key.get_pressed()
        for eventos in pygame.event.get():
        
            if eventos.type == QUIT:
                sys.exit(0)
       
       #Frecuencia para actualizar los sprites en el fondo indicado
        dragon.actualizar(time)
        nubes.actualizarNubes(time)
        screen.blit(background_image,(0,0))
        screen.blit(nubes.image, nubes.rect)
        screen.blit(dragon.image, dragon.rect)
        screen.blit(cactus.image, cactus.rect)
        pygame.display.flip()
        pygame.display.update()
        theClock.tick(10)
        
        
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()