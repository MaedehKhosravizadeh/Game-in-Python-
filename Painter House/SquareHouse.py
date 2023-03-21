import pygame
import numpy as np
import sys
import random
import time
import math
import re
import tkinter as tk

SCREEN_SIZE = WIDTH, HEIGHT = (640, 480)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLUE = (50, 50, 255)
CLR = [RED,BLUE,GREEN]
CIRCLE_RADIUS = 50


############################ Make Table
n = 4 #Number of Square
m = 2  #Number of Squares of colored

A = np.matrix([[-1]*n]*n)
C = np.array(m*m*[(0,0,0)])

g = math.ceil((m*m)**(1/3))
B = list(np.random.permutation(np.arange(1,g**3-1)))

p = random.randrange (n-m)
q = random.randrange (n-m) #(p,q) the position of colored square
R = np.matrix(np.random.permutation(m*m).reshape(m,m)) # A random colored!

############################ Choose Color for Table

def RGBfirst():
    global B
    ix = B.index(1)
    B[ix] = B[0]
    B[0]= 1
    ix = B.index(g)
    B[ix] = B[1]
    B[1]= g
    ix = B.index(g*g)
    B[ix] = B[2]
    B[2]= g*g
def BtoC():
    global B
    global C
    global g
    for i in range(len(C)):
        z = B[i]
        a= z // (g*g)
        z -= a*g*g
        b= z // g
        z -= b*g
        a = int((a>0)*(g+1-a)/g*255)
        b = int((b>0)*(g+1-b)/g*255)
        z = int((z>0)*(g+1-z)/g*255)
        C[i] = (a,b,z)

def Coloring():
    #global A,p,q,R
    for i in range(m):
        for j in range(m):
            A[(p+i)%n,(q+j)%n] = R[i,j]
    for j in range(m,n):
        A[p,(q+j)%n] = random.choice(list(range(m*m))+ [A[p,(q+j-1)%n]]*2)
    for i in range(m,n):
        A[(p+i)%n,q] = random.choice(list(range(m*m))+ [A[(p+i-1)%n,q]]*2)
    for i in range(1,m):
        for j in range(m,n):
            A[(p+i)%n,(q+j)%n] = random.choice(list(range(m*m))+[A[(p+i-1)%n,(q+j)%n],A[(p+i)%n,(q+j-1)%n],A[(p+i-1)%n,(q+j-1)%n]]*5)
    for i in range(m,n):
        for j in range(1,n):
            A[(p+i)%n,(q+j)%n] = random.choice(list(range(m*m))+[A[(p+i-1)%n,(q+j)%n],A[(p+i)%n,(q+j-1)%n],A[(p+i-1)%n,(q+j-1)%n]]*5) 
    
############################

RGBfirst()
BtoC()
Coloring()


# make C as a table of COLOR and A has the number of color
# and We should paint i,j of table by C[A[i,j]] as (R,B,G)

#################### table and horse
# Initialization
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Circles')
fps = pygame.time.Clock()
X = 600
Y = 600
x = 30
y = 215
horse_image = pygame.image.load(r'F:\Maedeh\Work00\Codes - Jangooler\Games\Painter House\horse1.png')
horse_image.set_colorkey(WHITE)
horse_image = pygame.transform.scale(horse_image, (70,70))


#image_table = pygame.image.load(
#    r'F:\Maedeh\Work00\Codes - Jangooler\Games\Painter House\TableHouse.png')
#image_table.set_colorkey(WHITE)
#image_table = pygame.transform.scale(image_table, TABLE_SIZE)
#image_table = pygame.transform.rotate(image_table, 0)

def table(w):
    pnt = int(400/w)
    for i in range(w+1):
        pygame.draw.line(screen, GREEN, [100+i*pnt, 100], [100+i*pnt,500], 5)
        pygame.draw.line(screen, GREEN, [100, 100+i*pnt], [500,100+i*pnt], 5)
    


def show(tble,colrs,hrs,clr):
    global X, Y, horse_image, screen
    display_surface = pygame.display.set_mode((X, Y ))
    display_surface.fill(WHITE)   
    if(tble):
        table(n)
    if(hrs):
        display_surface.blit(horse_image , (x,y))
        screen.blit(horse_image,(x,y))
    if colrs:
        pygame.draw.rect(screen, C[0], pygame.Rect(100,30,20,20))
        pygame.draw.rect(screen, C[1], pygame.Rect(200,30,20,20))
        pygame.draw.rect(screen, C[2], pygame.Rect(300,30,20,20))
        pygame.draw.rect(screen, C[3], pygame.Rect(400,30,20,20))
    
    if clr:
        pygame.draw.rect(screen, C[A[b,a]], pygame.Rect(100*b + 100,100*a + 100 ,100,100)) 
        
    pygame.display.update()
    
show(1,1,1,0)

def end(u,v):
    pygame.draw.rect(screen, C[A[u-1,v-1]], pygame.Rect(100*u ,100*v ,100,100)) 
    pygame.draw.rect(screen, C[A[u,v-1]], pygame.Rect(100*u+100 ,100*v  ,100,100)) 
    pygame.draw.rect(screen, C[A[u-1,v]], pygame.Rect(100*u,100*v + 100 ,100,100)) 
    pygame.draw.rect(screen, C[A[u,v]], pygame.Rect(100*u + 100,100*v + 100 ,100,100)) 
    pygame.display.update()
    c1 = C[A[u-1,v-1]]
    c2 = C[A[u,v-1]]
    c3 = C[A[u-1,v]]
    c4 = C[A[u,v]]
    
    if(len(set([c1,c2,c3,c4])) == 4):
        lb12=tk.Label(root, text=" درسته. آفرين!" ,height=4, width=30)
        lb2.pack()
        root.mainloop()
    else:
        lb12=tk.Label(root, text=" درست نيست" ,height=4, width=30)
        lb2.pack()
        root.mainloop()


##################### Make a text
result =""
'''
def get_move():
    root = tk.Tk()
    root.title()
    root.geometry("300x300+150+300")
    
    textExample=tk.Text(root, height=2)
    textExample.pack()
    lb1=tk.Label(root, text=" U2L1 يا d1R2 مسير اسب را مشخص کن! مثلا" ,height=4, width=30,bg='#A940A3')
    lb1.pack()
    btnRead=tk.Button(root, height=1, width=10, text="Read", 
                        command=getTextInput(textExample))
    btnRead.pack()
    root.mainloop()
    return(result)
'''
def getTextInput():
        global result
        result=textExample.get("1.0","end")
        if(re.match("^(l|L|R|r)(1|2)(u|U|d|D)(1|2)$",result) or re.match("^(S|s)\d \d$",result)):
            if(result[0] != 'S' and result[0] != 's'):                    
                if(result[1]!=result[3]):
                    root.destroy()
            else:
                end(int(result[1]),int(result[3]))


#################### Movement of horse


a = 1
b = -1
result = random.choice(["r2u1","r2d1","r1d2"])
t =0 
while t<20:
    print(result)
    move = result
    if(move[2] == 'u' or move[2] == 'U'):
        f = -int(move[3])
    if(move[2] == 'd' or move[2] == 'D'):
        f = int(move[3])
    if(move[0] == 'r' or move[0] == 'R'):
        g = int(move[1])
    if(move[0] == 'l' or move[0] == 'L'):
        g = -int(move[1])
    #print(f,g)
    #print(a+f,b+g)
    if(not(a+f in range(n) and b+g in range(n))):
        pass
    else:
        show(1,1,1,0)
        print("pas chi?")
        for j in np.arange(0,int(g*14),g):
            x = x + j
            time.sleep(0.1)
            show(1,1,1,0)
            fps.tick(60)
        for i in np.arange(0,int(f*14),f):
            time.sleep(0.1)
            y = y + i
            show(1,1,1,0)
            fps.tick(60)
        time.sleep(0.3)
        a = a + f
        b = b + g
        print(a,b)
        pygame.draw.rect(screen, C[A[b,a]], pygame.Rect(100*b + 100,100*a + 100 ,100,100))
        screen.blit(horse_image,(x,y))
        pygame.display.update()
        
    time.sleep(1)
    show(1,1,1,1)
    
    time.sleep(1)
    #########
    
    time.sleep(1)
    show(1,1,1,0)
    root = tk.Tk()
    root.title()
    root.geometry("300x300+150+300")
    textExample=tk.Text(root, height=1)
    textExample.pack()
    lb1=tk.Label(root, text=" L1U2 يا R2d1 مسير اسب را مشخص کن! مثلا" ,height=4, width=30,bg='#A940A3')
    lb1.pack()
    btnRead=tk.Button(root, height=1, width=10, text="Read",command=getTextInput)
    btnRead.pack()
    root.mainloop()
    t += 1




#################### color the element of table
#pygame.draw.rect(screen, BLACK, pygame.Rect(100,100,20,20))
'''
for i in range(n):
    for j in range(n):
        pygame.draw.rect(screen, C[A[i,j]], pygame.Rect(94*i + 116, 95*j + 115 ,85,85))
'''

