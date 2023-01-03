import pygame
window = pygame.display.set_mode((1500, 800), pygame.RESIZABLE)



def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac, action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(window, ac, (x, y, w, h))
        if click[0] == 1:
            action()
    else:
        pygame.draw.rect(window, ic, (x, y, w, h))
        smallText = pygame.font.SysFont(None, 20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ((x+(w/2)), (y+(h/2)))
        window.blit(textSurf, textRect)

def home():
    global game_state
    game_state = "home" 

def common_screen():
    button("Home", 1400, 0, 100, 50, (0,200,0), (255,255,210), home)
def home_intro():
    global game_state

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                 
        window.blit(image, (0,0))
        pygame.display.set_caption("PROGRAM")
        button("Start", 150, 450, 100, 50, (0,200,0), (255,255,210), start)
        button("Screen 1", 150, 450, 100, 50, (0,200,0), (255,255,210), screen1)
        button("Screen 2", 150, 450, 100, 50, (0,200,0), (255,255,210), screen2)
        button("Stop", 550, 450, 100, 50, (0,200,0), (255,255,210), stop)
        if game_state == 'screen1':
            common_screen()

        pygame.display.flip()

home_intro()
pygame.quit()
quit()