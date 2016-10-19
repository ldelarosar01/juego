

import sys, pygame
from pygame.locals import *
from Tkconstants import TOP
 

WIDTH = 640
HEIGHT = 480

class Dragon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/dragon2.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speed = [0.5, -0.5]
         
    def actualizar(self, time):
        self.rect.centerx += self.speed[0] * time
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed[0] = +self.speed[0]
            self.rect.centerx += self.speed[0] * time
        if self.rect.right <= 0 or self.rect.bottom >= HEIGHT:
            self.speed[1] = +self.speed[0]
            self.rect.centery += self.speed[0] * time
 
def load_image(filename, transparent=False):
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
 
    background_image = load_image('images/fondo.jpg')
    dragon = Dragon();
    
    clock = pygame.time.Clock()
   
    while True:
       
        for eventos in pygame.event.get():
            
            if eventos.type == QUIT:
                sys.exit(0)
        time = clock.tick(600)
        dragon.actualizar(time)
        screen.blit(background_image, (0, 0))
        screen.blit(dragon.image, dragon.rect)
        pygame.display.flip()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()