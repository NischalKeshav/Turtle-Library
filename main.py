import turtle 
import time
t = turtle.Pen()
for x in range (1,9) :
  t.forward(105)
  t.right(225)
t.clear()
print ("Get ready for Our next performance by turtle ")
for i in range (1,19):
  t.forward(100)
  if x % 2 == 0:
    t.left(175)
  else :
    t.right(225) 
t.clear()
def colorc(r,g,b,radius): #color circle
  t.color(r,g,b)
  t.begin_fill()
  t.circle (radius)
  t.end_fill()
colorc(1,0,0,50)
def square (side): # makes a square 
  for i in range (1,5):
    t.forward(side)
    t.left(90)
def squarec (r,g,b,side):# makes a colored square 
  t.color(r,g,b)
  t.begin_fill()
  for i in range (1,5):
    t.forward(side)
    t.left(90)
  t.end_fill()
squarec(1,0,0,20)
t.clear()
def star (side): # makes a star
  for x in range (1,19):
    t.forward(side)
    if x % 2 == 0:
      t.left(175)
    else:
      t.left(225)
def starc (r,g,b,side):#makes a colored star
  t.color(r,g,b)
  t.begin_fill()
  for x in range (1,19):
    t.forward(side)
    if x % 2 == 0:
      t.left(175)
    else:
      t.left(225)
  t.end_fill()
starc(1,0,0,50)
t.clear
def octagon (side): # makes a octagon
  for i in range(9):
    t.forward(side)
    t.right(45)

def octagonc (r,g,b,side):#colored octagon
  t.left(90)
  t.color (r,g,b)
  t.begin_fill()
  for i in range(9):
    t.forward(side)
    t.right(45)
  t.end_fill()
octagonc(0,1,0,50)
def starout(fill,side):
  if fill == True:
    t.begin_fill()
  for x in range (1,19):
    t.forward(side)
    if x % 2 == 0:
      t.left(175)
    else:
      t.left(225)
  if fill == True :
    t.end_fill()
t.clear()
t.color(0,0,0)
starout(False ,120)
    
  