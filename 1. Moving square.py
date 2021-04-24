import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Moving square")

x = 50
y = 50
width = 4
height = 4
vel = 7



print("\n**Use arrow keys to move.**\n ")

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
        if x < 0:
            x = 500
            

    if keys[pygame.K_RIGHT]:
        x += vel
        if x > 500:
            x = 0
            

    if keys[pygame.K_UP]:
        y -= vel
        if y < 0:
            y = 500
            

    if keys[pygame.K_DOWN]:
        y += vel
        if y > 500:
            y = 0
            

            
    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
    


pygame.quit()
