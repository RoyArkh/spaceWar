import pygame
import time
import random

import pygame.pypm
pygame.font.init()

#we need a window for the pygame
WIDTH, HEIGHT = 864, 540
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("space war")

BG = pygame.transform.scale(pygame.image.load("spacebg.jpg"), (WIDTH, HEIGHT))
FONT = pygame.font.SysFont("comicsans", 20)

PLAYER_WIDTH, PLAYER_HEIGHT = 40, 40
PLAYER_VEL = 10

STAR_WIDTH, STAR_HEIGHT = 10, 10
STAR_VEL = 5

def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, "white", player)

    for star in stars:
        pygame.draw.rect(WIN, "red", star)

    pygame.display.update()



#now we need to set up the while loop which will keep the game alive
def main():
    run = True

    #here I am creating the rectangle that is going to be my player 
    # and which we will pass to draw func
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0
    stars = []
    hit = False

    #the main loop
    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and (player.x - PLAYER_VEL >= 0):
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and (player.x + PLAYER_VEL + player.width <= WIDTH):
            player.x += PLAYER_VEL

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        if hit:
            lost_text = FONT.render("YOU LOST LOOL", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

 
        draw(player, elapsed_time, stars)

    pygame.quit()

if __name__ == "__main__":
    main()

