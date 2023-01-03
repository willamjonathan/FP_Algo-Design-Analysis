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