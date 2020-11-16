import pygame as pg
import sys
import random
from colors import *




pg.init()
s_w=1000
s_h=576

screen=pg.display.set_mode((s_w,s_h))
clock=pg.time.Clock()
pg.display.set_caption('Sorting bars')

bg = pg.Surface((s_w,s_h))
bg.fill(white)

rect_list=[]
for i in range (s_w//11):
    random_height=random.randint(10,500)
    rect = pg.Surface((s_w//100,random_height))
    rect.fill(black)
    rect_list.append(rect)
    
def init_text(bars,algo,end):
    g_font=pg.font.SysFont("comicsansms",14)
    s1='Sort bars with random heights, press :' 
    s2='*\'b\' to use \'Bubble Sort\' algorithm' 
    s3='*\'i\' to use \'Isertion Sort\' algorithm' 
    s4='*\'s\' to use \'Shell Sort\' algorithm' 
    s5='*\'e\' to use \'Selection Sort\' algorithm'

    sa='Sorting using \'Bubble Sort\' ...'
    sb='Sorting using \'Isertion Sort\' ...'
    sc='Sorting using \'Shell Sort\' ...'
    sd='Sorting using \'Selection Sort\' ...'
    send='Done ! Press \'ESC\' to regenerate the bars.'

    text1 = g_font.render(s1, True, black)
    text2 = g_font.render(s2, True, black)
    text3 = g_font.render(s3, True, black)
    text4 = g_font.render(s4, True, black)
    text5 = g_font.render(s5, True, black)

    texta = g_font.render(sa, True, black)
    textb = g_font.render(sb, True, black)
    textc = g_font.render(sc, True, black)
    textd = g_font.render(sd, True, black)
    textend = g_font.render(send, True, black)
    if bars:
        screen.blit(text1,(0,0))
        screen.blit(text2,(5,15))
        screen.blit(text3,(5,30))
        screen.blit(text4,(5,45))
        screen.blit(text5,(5,60))

    elif algo ==1:
        screen.blit(texta,(0,0))
    elif algo ==2:
        screen.blit(textb,(0,0))
    elif algo ==3:
        screen.blit(textc,(0,0))
    elif algo ==4:
        screen.blit(textd,(0,0))
    
    if end :
        screen.blit(textend,(0,0))

        


bars=True
algo =0
end=False
sort_bubble=False
sort_insert=False
sort_shell=False
sort_selection=False
x=len(rect_list)
y=0
gap = len(rect_list) // 2
while True:
    #Event loop: 
    for event in pg.event.get():
        #Exit strategy
        if event.type==pg.QUIT:
            pg.quit()
            sys.exit()
        #user input
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_b:
                sort_bubble=True
            if event.key==pg.K_i:
                sort_insert=True
            if event.key==pg.K_s:
                sort_shell=True
            if event.key==pg.K_e:
                sort_selection=True
            if event.key==pg.K_ESCAPE:
                rect_list=[]
                for i in range (s_w//11):
                    random_height=random.randint(10,500)
                    rect = pg.Surface((s_w//100,random_height))
                    rect.fill(black)
                    rect_list.append(rect)
                sort_bubble=False
                sort_insert=False
                sort_shell=False
                sort_selection=False

                gap = len(rect_list) // 2
                x=len(rect_list)
                y=0
                bars=True
                algo =0
                end=False

                
                            

    screen.blit(bg,(0,0))
    init_text(bars,algo,end)
    #draw random rects
    i=0
    for rect in rect_list:
        i+=1
        screen.blit(rect,(i*11,s_h-rect.get_height()))
    
    if sort_bubble:
        algo=1
        bars=False
        x-=1
        if x==0:
            sort_bubble=False
            algo=0
            end=True
        for rect in rect_list:
            rect.fill(black)
        for idx in range(x):

            if rect_list[idx].get_height()>rect_list[idx+1].get_height():
                #highlighting the current rect
                rect_list[idx].fill(green)
                temp = rect_list[idx]
                rect_list[idx] = rect_list[idx+1]
                rect_list[idx+1] = temp    

    if sort_insert:
        algo=2
        bars=False
        y+=1
        for rect in rect_list:
            rect.fill(black)        
        j = y-1
        nxt_element = rect_list[y]
        while (rect_list[j].get_height() > nxt_element.get_height()) and (j >= 0):
            rect_list[j+1] = rect_list[j]
            j=j-1
        rect_list[j+1] = nxt_element
        rect_list[j+1].fill(green)
        rect_list[j].fill(red)
        if y==len(rect_list)-1:
            sort_insert=False
            algo=0
            end=True
            
            for rect in rect_list:
                rect.fill(black)

    if sort_shell:
        algo=3
        bars=False
        if gap==0:
            sort_shell=False
            algo=0
            end=True
            for rect in rect_list:
                rect.fill(black)        
        for rect in rect_list:
                rect.fill(black)
        if gap > 0:
            for i in range(gap, len(rect_list)):
                temp = rect_list[i]
                
                j = i
                while j >= gap and rect_list[j - gap].get_height() > temp.get_height():
                    rect_list[j] = rect_list[j - gap]
                    j = j-gap
                    rect_list[j].fill(green)                    
                rect_list[j] = temp
            gap = gap//2

    if sort_selection :
        algo=4
        bars=False
        min_idx = y
        for rect in rect_list:
            rect.fill(black)
        for j in range( y +1, len(rect_list)):
            if rect_list[min_idx].get_height() > rect_list[j].get_height():
                min_idx = j
                rect_list[j].fill(red)
            rect_list[min_idx].fill(green)
        
        
        rect_list[y], rect_list[min_idx] = rect_list[min_idx], rect_list[y]
        y+=1
        if y==len(rect_list):
            algo=0
            end=True
            sort_selection=False
        

    #updating the display
    pg.display.update()
    
    #setting the FPS (framerate)
    clock.tick(10)