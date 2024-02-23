from kandinsky import *
l=[]
def see_and_copy(x_,y_,h):
  for x in range(x_):
    for y in range(y_):
      l.append(get_pixel(x*h,y*h))
lne=[]
def copy_qr(decx,decy,x_,y_,h):
  for y in range(decy,y_+decy):
    lnd="0b1"
    for x in range(decx,x_+decx):
      if get_pixel(x*h,y*h) == (0,0,0):
        if (x == 1 or x == 4) and 9 < y < 14: lnd+="0"
        elif (x == 10 or x == 13) and y != 7: lnd+="0"
        elif (x == 16 or x == 19) and 9 < y: lnd+="0"
        else: lnd+="1"
      elif get_pixel(x*h,y*h) == (255,255,255):
        if (x == 1 or x == 4) and 9 < y < 14: lnd+="1"
        elif (x == 10 or x == 13) and y != 7: lnd+="1"
        elif (x == 16 or x == 19) and 9 < y: lnd+="1"
        else: lnd+="0"
    lne.append(int(lnd,2))

def qr_code_read(ld,p=lne,h=5):
  if p == []: pass
  else:
    x,y=h,h
    for i in range(len(p)):
      bina=bin(p[i])
      for j in range(3,3+ld):
        if bina[j] == '1':
          r,g,b=0,0,0
        elif bina[j] == '0':
          r,g,b=255,255,255
        fill_rect(x,y,h,h,color(r,g,b))
        x+=h
      y+=h;x=h

# =============== En Dev ===============
def qr_code_informat(data=bin(0b101),h=5):
  lzb='0x'
  for i in range(3,18):
    if data[i] == '1':
      lzb+='00'
    elif data[i] == '0':
      lzb+='ff'
  fill_rect(9*h,h,h,h,color(int(lzb[2:5],16)))
  fill_rect(9*h,2*h,h,h,color(int(lzb[4:7],16)))
# ======================================
    

p="00ff00ff00000000ff"
def locate(i):
  s=str("0x"+p[i:i+2])
  return int(s)
def draw(h=5):
  x,y=0,0
  for i in range(3):
     r,g,b=locate(i*6),locate(2+i*6),locate(4+i*6)
     fill_rect(x,y,h,h,color(r,g,b))
     x+=h
  see_and_copy(3,1,h)