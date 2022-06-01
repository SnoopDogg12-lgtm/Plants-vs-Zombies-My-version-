import pygame
from Sprites import GreenDefenderCard, GreenDefender
from Sprites import Bullet, Mob

#https://stackoverflow.com/questions/29640685/how-do-i-detect-collision-in-pygame

SCREENWIDTH=800
SCREENHEIGHT=700
#BACKGROUND_IMG = pygame.image.load("background.png")

WHITE = ((255,255,255))
RED = ((255,0,0))

pygame.init() 
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tower Defence")

# Storing the amount of columns and rows we multiply by
y_values = [1,2,3,4,5]
x_values = [1,2,3,4,5,6,7,8]

# here we store the squares we render on the screen
reactangles = []
#used to store all the taken squares on the map
taken_reactangles = []

#images
grass_tile = pygame.image.load("grass_tile.png").convert()
#defender = pygame.image.load("greenDefender.png")
bg = pygame.image.load("background.jpeg")


#Initiliazing the sprites we render
green_defender_card = GreenDefenderCard()

#sprite groups
defenders_cards_sprite_list = pygame.sprite.Group()
defenders_cards_sprite_list.add(green_defender_card)
green_defenders_group = pygame.sprite.Group()

bullets_group = pygame.sprite.Group()
zombies_group = pygame.sprite.Group()


#sprite arrays
green_defender_list = []
bullets = []
zombies = []

#rect object that we wanna move
#rect_left, rect_top, rect_width, rect_height

#this var keeps track of when we should shoot another bullet
timing = 0

def draw_grid():
    reactangles.append(pygame.draw.rect(screen,RED,(0,0,100,100)))
    #drawing squares on each tile
    #left,top,width,height
    for i in range(len(x_values)):
        reactangles.append(pygame.draw.rect(screen,RED,(100*x_values[i],0,100,100)))
        for j in range(len(y_values)):
            reactangles.append(pygame.draw.rect(screen,RED,(100*x_values[i],100*y_values[j],100,100)))
    for x in range(len(y_values)):
        reactangles.append(pygame.draw.rect(screen,RED,(0,100*y_values[x],100,100)))

    print(f"Lenght of reactangles {len(reactangles)}")         

    #x,y
    #this is for the y axis 
    for i in range(len(y_values)):
        pygame.draw.line(screen, WHITE, (0,100*y_values[i]), (800,100*y_values[i]), 4)

    #this is for the x axis
    for i in range(len(x_values)):
        pygame.draw.line(screen, WHITE, (100*x_values[i],0), (100*x_values[i],600), 4)


def draw_tiles():
    #drawing squares on each tile
    #left,top,width,height
    for i in range(len(x_values)):
        for j in range(len(y_values)):
            screen.blit(grass_tile, (0, 0))
            screen.blit(grass_tile, (0,100*y_values[j]))
            screen.blit(grass_tile, (100*x_values[i],0))
            screen.blit(grass_tile, (100*x_values[i],100*y_values[j]))

def draw_hero_cards():
    pass


def check_for_collison(sprite1, sprite2):
    pass


is_green_card_selected = False
is_button_pressed = False

running = True
clock=pygame.time.Clock()

draw_grid()
defenders_cards_sprite_list.draw(screen)
draw_tiles()

zombie = Mob(600,500,scr=screen)

while running:
    #screen.blit(grass_tile, (0, 0))
    #grass_block_rect = grass_tile.get_rect()

    clock.tick(27)
    timing += 1
    #print(timing)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type == pygame.MOUSEBUTTONDOWN: # is some button clicked
            if event.button == 1: # is left button clicked
                if green_defender_card.rect.collidepoint(event.pos):
                    print("collided with card")
                    is_green_card_selected = True
                                        
        if is_green_card_selected:
            if event.type == pygame.MOUSEBUTTONDOWN: # is some button clicked
                if event.button == 1: # is left button clicked

                    for rect in reactangles:
                        if rect.collidepoint(event.pos): # is mouse over button
                            print("collided")
                            print(rect.x)
                            print(rect.y)

                            green_defender = GreenDefender()
                            green_defender.rect.x = rect.x
                            green_defender.rect.y = rect.y

                            screen.blit(green_defender.image, (green_defender.rect))
                            green_defender_list.append(green_defender)
                            taken_reactangles.append((rect.x,rect.y))

                            is_green_card_selected = False

                            for i in range(len(green_defender_list)):
                                print(f"Defender {i} x pos {green_defender_list[i].rect.x}")
                                print(f"Defender {i} y pos {green_defender_list[i].rect.y}")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                #bullets.append(GreenDefenderBullet(green_defender_list[0].rect.x+100//2,green_defender_list[0].rect.y,screen))
                is_button_pressed = True
        
    if timing == 100 and len(green_defender_list) > 0:
        for green_def in green_defender_list:
            bullets.append(Bullet(green_def.rect.x+60,green_def.rect.y,screen))
            timing = 0
    elif timing == 100:
       timing = 0

    for b in bullets:
        b.update()
        if b.y < 5:
            bullets.remove(b)

    #screen.fill((98, 98, 98))#
    screen.blit(bg, (0, 0))
    for defender in  green_defender_list:
        screen.blit(defender.image, (defender.rect.x,defender.rect.y))

    for b in bullets:
        b.draw()

    zombie.draw()

    #collsion 
    for bullet in bullets:
        if bullet.x == zombie.x and bullet.y == zombie.y:
            bullets.remove(bullet)
            zombie.health -= 5
            print("collided")
            print(f"Zombie health {zombie.health}")

    if zombie.health == 0:
        #removing the zombie off the screen as I couldn't figure out
        #how to properly remove the sprire itself
       zombie.y = 1000 

    pygame.display.update()