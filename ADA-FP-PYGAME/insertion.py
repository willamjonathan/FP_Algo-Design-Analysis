# INSERTION SORT
# IMPORT MODULES

import pandas as pd
import numpy as np
import itertools

import pygame
import pygame
from pygame.locals import *
#---------------------------------------------------------------------------------------
from screen import myFPS
from screen import screen_size
from screen import MyColor
from screen import myFont


from insertsort import insertionSort
from randoms import randoms
from print import printed
from searchStorage import searchStorage

# Reading the files
df = pd.read_csv('EXCELadaFP.csv')
df.iloc[0:1,:]

# DATA PROCESSING AND CLEANING
df['LIST'] = df['LIST'].astype('string') 
#CHANGING THE ALPHABET INTO LOWER CASE
df['LIST'] = df['LIST'].str.lower()
# df.head()
# df.info()

# CHANGING THE DATAFRAME TO ARRAY
array = df.to_numpy()



# Initializing
pygame.init()
pygame.font.init()
#calling function
font1 = myFont('Arial')
font2 = myFont( )
ss = screen_size(760,450)
Fps = myFPS(60)
cl = MyColor()
warna = (255,255,255)

myscreen = pygame.display.set_mode((ss.getWidth(),ss.getHeight()))

# bg = pygame.image.load("menubg.jpg")
# myscreen.blit(bg,(0,0))
clock = pygame.time.Clock()

# FUNCTION ----------------------------------------------------------------
def oneDArray(x):
    return list(itertools.chain(*x))

def mainINSERTION():
    #title text
    arr = oneDArray(array)
    titlefont = pygame.font.SysFont(font2.getMyFont(),50)
    def TTL_text(myscreen):
        TTL_text = titlefont.render("INSERTION SORT", True, (0,0,0))
        myscreen.blit(TTL_text, (100,100))

    #my button
    button = 1
    playFont = pygame.font.SysFont(font2.getMyFont(),22)
    subtitleFont  = pygame.font.SysFont(font2.getMyFont(),24)
    theFont = pygame.font.SysFont(font2.getMyFont(),60)
    def myButton(myscreen):
        if button == 1:  
            sub = subtitleFont.render("Please check your IDE terminal! ",1,(0,0,0))
            myscreen.blit(sub, (100,140))
            header = theFont.render("                                                                                                                                                              ",1,
            (cl.getColor()),(67, 66, 66))
            myscreen.blit(header, (0,0))
            footer = theFont.render("                                                                                                                                                              ",1,
             (cl.getColor()),(67, 66, 66))
            myscreen.blit(footer, (0,410))
            prin = playFont.render("> Print the array(press left_arrow) !", 1, (0,0,0))
            myscreen.blit(prin, (130, 210))
            rndom = playFont.render("> Randomize the array(press right_arrow) !", 1, (0,0,0))
            myscreen.blit(rndom, (130, 240))
            do = playFont.render("> Do insertion sort(press up_arrow) !", 1, (0,0,0))
            myscreen.blit(do, (130, 270))
            search = playFont.render("> Search item (storage) (press down_arrow) !", 1, (0,0,0))
            myscreen.blit(search, (130, 300))
            bye = playFont.render("> Exit (press F6)", 1, (0,0,0))
            myscreen.blit(bye, (130, 330))

        elif button == 11:  #page1
            # prin = playFont.render(printed(arr),1,(0,0,0))
            print(arr)
        elif button == 12: #page2
            # rndom = playFont.render(randoms(arr),1,(0,0,0)) 
            randoms(arr)
        elif button == 13: #page3
            # do = playFont.render(insertionSort(arr),1,(0,0,0))
            insertionSort(arr)
        elif button == 14:  #page1
            # search = playFont.render(searchStorage(arr),1,(0,0,0))
            searchStorage(arr)
        elif button == 0: #page2
            bye = playFont.render("bye",1,(0,0,0)) 

        
    running = True
    while running:
        clock.tick(Fps.getFPS())
        # GARA GARA FOR INI DIA MULTIPLE CALL FUNCTION
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    button = 11#print
                elif event.key == pygame.K_RIGHT:
                    button = 12#random
                elif event.key == pygame.K_UP:
                    button = 13#sorting
                elif event.key == pygame.K_DOWN:
                    button = 14#search
                elif event.key == pygame.K_F6:
                    button = 0#bye
            else:
                button = 1
        myscreen.fill(warna)

        TTL_text(myscreen)
        myButton(myscreen)
        pygame.display.update()

    pygame.quit()
