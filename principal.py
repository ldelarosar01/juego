

import sys, pygame
from pygame.locals import *
from Tkconstants import TOP
 
import time
from time import sleep
WIDTH = 1000
HEIGHT = 500
gravity = 50

theClock = pygame.time.Clock()
pygame.mixer.init()
sonido = pygame.mixer.Sound("background.mp3")

def hasPerdido ():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Juegecito Pygame")
    background_image = load_image('images/gameOver.png', True)

    clock = pygame.time.Clock()
   

    while True:
        time = clock.tick(26)
        keys = pygame.key.get_pressed()
        for eventos in pygame.event.get():
            if keys[K_SPACE]:
                main()
            if eventos.type == QUIT:
                sys.exit(0)
       
        
        screen.blit(background_image,(0,0))
  
        pygame.display.flip()
        pygame.display.update()
      
        
        
    return 0

class Nubes(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/nubes.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = 1000
        self.rect.centery = 200
        self.speed = [0.5]
        
    def actualizarNubes(self, time):
        print self.rect.centerx
        self.rect.centerx += self.speed[0] * 21
        if self.rect.centerx >= WIDTH :
            self.rect.centerx = -1900
        self.rect.centerx += self.speed[0] * 30
    

class Dragon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/dragon.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.centery = 400
        self.speed = [0.5]
    
    def actualizarDragon(self,time):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/dragon.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = 800
        self.rect.centery = 390
        self.speed = [0.5, 0.5]

    def saltar(self, time, keys):
              if keys[K_SPACE]:
                     self.rect.centery += 400
                     self.rect.centery -= 400
                     self.rect.centery -= gravity 
                     
                
class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/cactus.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = 1900
        self.rect.centery = 400
        self.speed = [0.5]

       
    def actualizar(self, time,dragon):
        print self.rect.centerx
        self.rect.centerx += self.speed[0] * 21
        if self.rect.centerx >= WIDTH :
            self.rect.centerx = -1500
        self.rect.centerx += self.speed[0] * 30
        if pygame.sprite.collide_rect(self,dragon):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
            hasPerdido()
            
     
                
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
    sonido.play()

    while True:
        time = clock.tick(26)
        keys = pygame.key.get_pressed()
        
        for eventos in pygame.event.get():

            if eventos.type == QUIT:
                sys.exit(0)

       #Frecuencia para actualizar los sprites en el fondo indicado
        dragon.actualizarDragon(time)
        dragon.saltar(time,keys)
        nubes.actualizarNubes(time)
        cactus.actualizar(time,dragon)
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