import pygame
import random 
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Test Window")
clock = pygame.time.Clock()

BLUE=(0,0,255)
start_pos=(0,0)
end_pos=(640,480)
start_pos1=(0,480)
end_pos1=(640,0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
#gestão do input
for event in pygame.event.get():
 if event.type == pygame.QUIT:
    running = False
 elif event.type == pygame.KEYDOWN:
       if event.key == pygame.K_LEFT:
        print("left arrow key pressed")
       elif event.key == pygame.RIGHT:
        print("right arrow key pressed")
screen.fill((0, 0, 0))
pygame.draw.line(screen,BLUE,start_pos,end_pos,5)
pygame.display.flip()
clock.tick(60)



pygame.quit()
