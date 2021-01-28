import pygame

pygame.init()
screen = pygame.display.set_mode((960, 720))
clock = pygame.time.Clock()
pygame.display.set_caption('badapple.py')
last_frame = 7777

pygame.mixer.music.load('music.ogg')

index = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()
    if index == 1:
        pygame.mixer.music.play()
    elif index == last_frame:
        pygame.quit()
        quit()
    else:
        pass
    frame = pygame.image.load('frames/f'+str(index)+'.bmp')
    index += 1
    
    screen.fill((0,0,0))
    screen.blit(frame, (0, 0))
    pygame.display.flip()
    clock.tick(24)
    print('FRAME:', index)
    
    
            

