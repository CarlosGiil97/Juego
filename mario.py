#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame
from pygame.locals import *
 
# Constantes
WIDTH = 640
HEIGHT = 480
 
# Clases
# ---------------------------------------------------------------------
class Mario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("imagenes/yoshi.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speed = [0.5, -0.5] 
    def actualizar(self, time):
	 keys = pygame.key.get_pressed() 
	 if keys[K_DOWN]: 
                self.rect.y += 6 
         if self.rect.y>=480: 
                self.rect.y -= 6 
         if keys[K_UP]: 
                self.rect.y -= 6 
         if self.rect.y <=18: 
                self.rect.y += 6 
         if keys[K_RIGHT]: 
                self.rect.x += 6 
	 if self.rect.x>=522: 
                self.rect.x -= 6 
         if keys[K_LEFT]: 
            self.rect.x -= 6 
         if self.rect.x<=47:     
            self.rect.x += 6 
# ---------------------------------------------------------------------
 
# Funciones
# ---------------------------------------------------------------------
 
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
    pygame.display.set_caption("Juego Carlos Gil")
 
    background_image = load_image('imagenes/mario3.jpg')
    mario = Mario()
    clock = pygame.time.Clock()
    while True:
	time = clock.tick(60)
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
 
        mario.actualizar(time)
	screen.blit(background_image, (0, 0))
	screen.blit(mario.image, mario.rect)
        pygame.display.flip()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()
