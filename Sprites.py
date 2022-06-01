import pygame

class GreenDefender(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("greenDefender.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
    
    def shoot(self):
        return

class GreenDefenderCard(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("greenDefenderCard.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 600

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, scr):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.x = x
        self.y = y
        self.scr = scr
        self.image = pygame.Surface((20,20))
        self.rect = self.image.get_rect()
        self.png_img = None 

    def update(self):
        self.x += self.speed#

    def draw(self):
        pygame.draw.rect(self.scr, ((255,0,0)), (self.x, self.y, 30, 30))

class Mob(pygame.sprite.Sprite):
    def __init__(self, x, y, scr):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.x = x
        self.y = y
        self.scr = scr
        self.image = pygame.Surface((20,20))
        self.rect = self.image.get_rect() 
        self.health = 20

    def draw(self):
       pygame.draw.rect(self.scr, ((255,0,0)), (self.x, self.y, 30,50))
    