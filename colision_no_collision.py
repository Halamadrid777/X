
import pygame
pygame.init()

# display variable for pygame
dis_height = 520
dis_width = 520
win = pygame.display.set_mode((dis_width, dis_height))
# Set pygame caption on the title

#more variables
x = 250
y = 50
height = 60
width = 40
vel = 5

run = True
while run:
    pygame.time.delay(100)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if keys[pygame.K_ESCAPE]:
            pygame.time.wait(100)
            run = False
        # elif event.type == KEYDOWN:
        #     if event.key == K_ESCAPE:
        #         return
        else:
            pass

    if keys[pygame.K_LEFT]:
        x -=vel
    if keys[pygame.K_RIGHT]:
        x +=vel   
    if keys[pygame.K_UP]:
        y-=vel
    if keys[pygame.K_DOWN]:
        y+=vel
    # fills board with pitch black and prevents more and more rectangle being drawn over each
    win.fill((0,0,0))
    # here x , y is the position in pygame.window for drawing rectangle
    r1=pygame.draw.rect(win, (250, 0, 0), (x, y, width, height))
    r2=pygame.draw.rect(win, (250, 0, 0), (50, 50, 40, 50))
    if r1.colliderect(r2) == 1:
        print("collided")
        pygame.display.set_caption("collided")

    elif r1.colliderect(r2) == 0:
        print("not collided")
        pygame.display.set_caption("not_collided")

    else:
        pass
    # updates board
    pygame.display.update()

pygame.quit()
