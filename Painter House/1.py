import pygame
import numpy as np
import sys
import random
import time
import math

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
p = random.randrange (n-m)
q = random.randrange (n-m) #(p,q) the position of colored square
R = np.matrix(np.random.permutation(m*m).reshape(m,m)) # A random colored!
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
display_surface = pygame.display.set_mode((X, Y ))
  
TABLE_SIZE = (400,400)

image_table = pygame.image.load(
    r'F:\Maedeh\Work00\Codes - Jangooler\Games\Painter House\TableHouse.png')
image_table.set_colorkey(WHITE)
image_table = pygame.transform.scale(image_table, TABLE_SIZE)
#image_table = pygame.transform.rotate(image_table, 0)

display_surface.fill(WHITE)


hourse_image = pygame.image.load(
    r'F:\Maedeh\Work00\Codes - Jangooler\Games\Painter House\horse1.png')
hourse_image.set_colorkey(WHITE)
hourse_image = pygame.transform.scale(hourse_image, (70,70))
display_surface.fill(WHITE)


display_surface.fill(WHITE)

display_surface.blit(image_table , (100,100))
display_surface.blit(hourse_image , (0,215))
pygame.display.update()

##################### Make a text
import tkinter as tk
root = tk.Tk()
root.title('مسير ربات را مشخص کن')
root.geometry("200x200+500+300")

def getTextInput():
    result=textExample.get("1.0","end")
    print(result)
    root.destroy()
    
textExample=tk.Text(root, height=2)
textExample.pack()
btnRead=tk.Button(root, height=1, width=10, text="Read", 
                    command=getTextInput)

btnRead.pack()

root.mainloop()
#################### Movement of horse



#################### color the element of table
#pygame.draw.rect(screen, BLACK, pygame.Rect(100,100,20,20))

# pygame.draw.rect(screen, C[A[i,j]], pygame.Rect(94*i + 116, 95*j + 115 ,85,85))



pygame.display.update()
