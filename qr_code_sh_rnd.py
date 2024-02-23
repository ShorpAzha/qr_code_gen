from random import *
from kandinsky import *
def qr_gen_all(h=5):
  angle(26*h,3*h,h)
  qr_gen_part(20*h,11*h,9,h)
  qr_gen_part(20*h,19*h,9,h)
  qr_gen_part(12*h,3*h,9,h)
  qr_gen_part(12*h,11*h,9,h)
  qr_gen_part(12*h,19*h,9,h)
  angle(8*h,3*h,h)
  qr_gen_part(4*h,11*h,9,h)
  angle(8*h,21*h,h)
  carre(24*h,19*h,h)
  for i in range(5):
    fill_rect(14*h,(11+i*2)*h,h,h,color(0,0,0))
    fill_rect(14*h,(12+i*2)*h,h,h,color(255,255,255))
  for i in range(5):
    fill_rect((16+i*2)*h,9*h,h,h,color(0,0,0))
    fill_rect((17+i*2)*h,9*h,h,h,color(255,255,255))
  fill_rect(16*h,20*h,h,h,color(0,0,0))

p=[127,65,93,93,93,65,127]
q = [31,17,21,17,31]

def angle(x_,y_,h=5):
  x,y=x_,y_
  for i in range(0,7):
    bina=bin(p[i])
    for j in range(2,9):
      if bina[j] == "0":
        r,g,b=255,255,255
      elif bina[j] == "1":
        r,g,b=0,0,0
      else:
        r,g,b=255,255,255
      fill_rect(x,y,h,h,color(r,g,b))
      x+=h
    y+=h
    x=x_

def carre(x_,y_,h=5):
  x,y=x_,y_
  for i in range(0,5):
    bina=bin(q[i])
    for j in range(2,7):
      if bina[j] == "0":
        r,g,b=255,255,255
      elif bina[j] == "1":
        r,g,b=0,0,0
      else:
        r,g,b=255,255,255
      fill_rect(x,y,h,h,color(r,g,b))
      x+=h
    y+=h
    x=x_

def qr_gen_part(x_,y_,w=8,h=5):
  #w,h=7,5 x,y=0,0
  x,y=x_,y_
  for i in range(w):
    bina=bin(randrange(2**(w+3),2**(w+4)))
    for j in range(4+w):
      if bina[j] == "0" and j >= 3:
        r,g,b=255,255,255
      elif bina[j] == "1" and j >= 4:
        r,g,b=0,0,0
      else:
        r,g,b=255,255,255
      fill_rect(x,y,h,h,color(r,g,b))
      x+=h
    y+=h;x=x_