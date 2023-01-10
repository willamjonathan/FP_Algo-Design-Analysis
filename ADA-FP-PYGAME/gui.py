import pygame
from pygame.locals import *
#---------------------------------------------------------------------------------------

# from hard import mainhard
# from medium import mainmedium
#--------------------------------------------------------------------------------------
from screen import myFPS
from screen import screen_size
from screen import MyColor
from screen import myFont

# INSERTION SORT
# IMPORT MODULES

import pandas as pd
import numpy as np
import itertools

from print import printed
from bubblesort import bubbleSort
from insertsort import insertionSort
from mergesort import mergeSort
from randoms import randoms
from bogosort import bogoSort
from selectionsort import selectionSort

from searchStorage import searchStorage

# Reading the files--------------------------------------------------------------------------------------------------------------------------------
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
# Initializing-----------------------------------------------------------------------------------------------------------------------
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

# FUNCTION --------------------------------------------------------------------------------------------------------------------------------
def oneDArray(x):
    return list(itertools.chain(*x))

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

# -------------------------------------------------------------------------------------------------------------------------------------------
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
        elif button == 0: #page2
            mainpage()

        
    running = True
    while running:
        clock.tick(Fps.getFPS())
        # GARA GARA FOR INI DIA MULTIPLE CALL FUNCTION
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    printed(arr)
                elif event.key == pygame.K_RIGHT:
                    randoms(arr)
                elif event.key == pygame.K_UP:
                    insertionSort(arr)
                elif event.key == pygame.K_DOWN:
                    searchStorage(arr)
                elif event.key == pygame.K_F6:
                    button = 0#bye
            else:
                button = 1
        myscreen.fill(warna)

        TTL_text(myscreen)
        myButton(myscreen)
        pygame.display.update()

# -------------------------------------------------------------------------------------------------------------------------------------------

def mainBUBBLE():
    #title text
    arr = oneDArray(array)
    titlefont = pygame.font.SysFont(font2.getMyFont(),50)
    def TTL_text(myscreen):
        TTL_text = titlefont.render("BUBBLE SORT", True, (0,0,0))
        myscreen.blit(TTL_text, (100,100))

    #my button
    button = 2
    playFont = pygame.font.SysFont(font2.getMyFont(),22)
    subtitleFont  = pygame.font.SysFont(font2.getMyFont(),24)
    theFont = pygame.font.SysFont(font2.getMyFont(),60)
    def myButton(myscreen):
        if button == 2:  
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
            do = playFont.render("> Do Bubble sort(press up_arrow) !", 1, (0,0,0))
            myscreen.blit(do, (130, 270))
            search = playFont.render("> Search item (storage) (press down_arrow) !", 1, (0,0,0))
            myscreen.blit(search, (130, 300))
            bye = playFont.render("> Back to the main menu (press F6)", 1, (0,0,0))
            myscreen.blit(bye, (130, 330))
        elif button == 0: #page2
            mainpage()

        
    running = True
    while running:
        clock.tick(Fps.getFPS())
        # GARA GARA FOR INI DIA MULTIPLE CALL FUNCTION
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    printed(arr)
                elif event.key == pygame.K_RIGHT:
                    randoms(arr)
                elif event.key == pygame.K_UP:
                    bubbleSort(arr)
                elif event.key == pygame.K_DOWN:
                    searchStorage(arr)
                elif event.key == pygame.K_F6:
                    button = 0#bye
            else:
                button = 2
        myscreen.fill(warna)

        TTL_text(myscreen)
        myButton(myscreen)
        pygame.display.update()    
# -------------------------------------------------------------------------------------------------------------------------------------------

def mainMERGE():
    #title text
    arr = oneDArray(array)
    titlefont = pygame.font.SysFont(font2.getMyFont(),50)
    def TTL_text(myscreen):
        TTL_text = titlefont.render("MERGE SORT", True, (0,0,0))
        myscreen.blit(TTL_text, (100,100))

    #my button
    button = 3
    playFont = pygame.font.SysFont(font2.getMyFont(),22)
    subtitleFont  = pygame.font.SysFont(font2.getMyFont(),24)
    theFont = pygame.font.SysFont(font2.getMyFont(),60)
    def myButton(myscreen):
        if button == 3:  
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
            do = playFont.render("> Do Merge sort(press up_arrow) !", 1, (0,0,0))
            myscreen.blit(do, (130, 270))
            search = playFont.render("> Search item (storage) (press down_arrow) !", 1, (0,0,0))
            myscreen.blit(search, (130, 300))
            bye = playFont.render("> Back to the main menu (press F6)", 1, (0,0,0))
            myscreen.blit(bye, (130, 330))
        elif button == 0: #page2
            mainpage()

        
    running = True
    while running:
        clock.tick(Fps.getFPS())
        # GARA GARA FOR INI DIA MULTIPLE CALL FUNCTION
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    printed(arr)
                elif event.key == pygame.K_RIGHT:
                    randoms(arr)
                elif event.key == pygame.K_UP:
                    mergeSort(arr)
                elif event.key == pygame.K_DOWN:
                    searchStorage(arr)
                elif event.key == pygame.K_F6:
                    button = 0#bye
            else:
                button = 3
        myscreen.fill(warna)

        TTL_text(myscreen)
        myButton(myscreen)
        pygame.display.update()    
# -------------------------------------------------------------------------------------------------------------------------------------------

def mainBOGO():
    #title text
    arr = oneDArray(array)
    titlefont = pygame.font.SysFont(font2.getMyFont(),50)
    def TTL_text(myscreen):
        TTL_text = titlefont.render("BOGO SORT", True, (0,0,0))
        myscreen.blit(TTL_text, (100,100))

    #my button
    button = 4
    playFont = pygame.font.SysFont(font2.getMyFont(),22)
    subtitleFont  = pygame.font.SysFont(font2.getMyFont(),24)
    theFont = pygame.font.SysFont(font2.getMyFont(),60)
    def myButton(myscreen):
        if button == 4:  
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
            do = playFont.render("> Do Bogo sort(press up_arrow) !", 1, (0,0,0))
            myscreen.blit(do, (130, 270))
            search = playFont.render("> Search item (storage) (press down_arrow) !", 1, (0,0,0))
            myscreen.blit(search, (130, 300))
            bye = playFont.render("> Back to the main menu (press F6)", 1, (0,0,0))
            myscreen.blit(bye, (130, 330))
        elif button == 0: #page2
            mainpage()

        
    running = True
    while running:
        clock.tick(Fps.getFPS())
        # GARA GARA FOR INI DIA MULTIPLE CALL FUNCTION
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    printed(arr)
                elif event.key == pygame.K_RIGHT:
                    randoms(arr)
                elif event.key == pygame.K_UP:
                    bogoSort(arr)
                elif event.key == pygame.K_DOWN:
                    searchStorage(arr)
                elif event.key == pygame.K_F6:
                    button = 0#bye
            else:
                button = 4
        myscreen.fill(warna)

        TTL_text(myscreen)
        myButton(myscreen)
        pygame.display.update()    
# -------------------------------------------------------------------------------------------------------------------------------------------

def mainSELECTION():
    #title text
    arr = oneDArray(array)
    titlefont = pygame.font.SysFont(font2.getMyFont(),50)
    def TTL_text(myscreen):
        TTL_text = titlefont.render("Selection SORT", True, (0,0,0))
        myscreen.blit(TTL_text, (100,100))

    #my button
    button = 5
    playFont = pygame.font.SysFont(font2.getMyFont(),22)
    subtitleFont  = pygame.font.SysFont(font2.getMyFont(),24)
    theFont = pygame.font.SysFont(font2.getMyFont(),60)
    def myButton(myscreen):
        if button == 5:  
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
            do = playFont.render("> Do Selection sort(press up_arrow) !", 1, (0,0,0))
            myscreen.blit(do, (130, 270))
            search = playFont.render("> Search item (storage) (press down_arrow) !", 1, (0,0,0))
            myscreen.blit(search, (130, 300))
            bye = playFont.render("> Back to the main menu (press F6)", 1, (0,0,0))
            myscreen.blit(bye, (130, 330))
        elif button == 0: #page2
            mainpage()

        
    running = True
    while running:
        clock.tick(Fps.getFPS())
        # GARA GARA FOR INI DIA MULTIPLE CALL FUNCTION
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    printed(arr)
                elif event.key == pygame.K_RIGHT:
                    randoms(arr)
                elif event.key == pygame.K_UP:
                    selectionSort(arr)
                elif event.key == pygame.K_DOWN:
                    searchStorage(arr)
                elif event.key == pygame.K_F6:
                    button = 0#bye
            else:
                button = 5
        myscreen.fill(warna)

        TTL_text(myscreen)
        myButton(myscreen)
        pygame.display.update()    
# -------------------------------------------------------------------------------------------------------------------------------------------

def mainpage():
    #title text
    titlefont = pygame.font.SysFont(font2.getMyFont(),50)
    def TTL_text(myscreen):
        TTL_text = titlefont.render("STORAGE MANAGEMENT SYSTEM", True, (0,0,0))
        myscreen.blit(TTL_text, (100,100))

    #my button
    button = 0
    playFont = pygame.font.SysFont(font2.getMyFont(),22)
    subtitleFont  = pygame.font.SysFont(font2.getMyFont(),28)
    theFont = pygame.font.SysFont(font2.getMyFont(),60)
    def myButton(myscreen):
        if button == 0:  
            header = theFont.render("                                                                                                                                                              ",1,
            (cl.getColor()),(67, 66, 66))
            myscreen.blit(header, (0,0))
            footer = theFont.render("                                                                                                                                                              ",1,
            (cl.getColor()),(67, 66, 66))
            myscreen.blit(footer, (0,410))
            ins = playFont.render("> Insertion sort(press F1)", 1, (0,0,0))
            myscreen.blit(ins, (130, 210))
            bubbl = playFont.render("> Bubble sort (press F2)", 1, (0,0,0))
            myscreen.blit(bubbl, (130, 240))
            merg = playFont.render("> Merge sort(press F3)", 1, (0,0,0))
            myscreen.blit(merg, (130, 270))
            bog = playFont.render("> Bogo sort (press F4)", 1, (0,0,0))
            myscreen.blit(bog, (130, 300))
            selec = playFont.render("> Selection sort(press F5)", 1, (0,0,0))
            myscreen.blit(selec, (130, 330))

        elif button == 1:  #page1
            ins = playFont.render(mainINSERTION(),1,(0,0,0))
        elif button == 2: #page2
            bubbl = playFont.render(mainBUBBLE(),1,(0,0,0)) 
        elif button == 3: #page3
            merg = playFont.render(mainMERGE(),1,(0,0,0))
        elif button == 4:  #page1
            bog = playFont.render(mainBOGO(),1,(0,0,0))
        elif button == 5: #page2
            selec = playFont.render(mainSELECTION(),1,(0,0,0)) 

        
    running = True
    while running:
        clock.tick(Fps.getFPS())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    button = 1#insertion
                    
                elif event.key == pygame.K_F2:
                    button = 2#bubble
                elif event.key == pygame.K_F3:
                    button = 3#merge
                elif event.key == pygame.K_F4:
                    button = 4#bogo
                elif event.key == pygame.K_F5:
                    button = 5#selection

            else:
                button = 0
        myscreen.fill(warna)

        TTL_text(myscreen)
        myButton(myscreen)
        pygame.display.update()

    pygame.quit()

