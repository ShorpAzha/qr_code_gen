from kandinsky import *
from time import *
from qr_code_sh_rnd import qr_gen_part, carre, angle
from copyl import copy_qr, qr_code_read

'''
Make by Shorp
Dev en cours
'''

def qr_code(cc=9,h=5):
  angle(h*(10+cc),h,h)
  qr_gen_part(13*h,9*h,cc,h)
  qr_gen_part(13*h,17*h,cc,h)
  qr_gen_part(5*h,17*h,cc,h)
  qr_gen_part(5*h,9*h,cc,h)
  qr_gen_part(5*h,h,cc,h)
  angle(h,(cc+10)*h,h)
  qr_gen_part(-3*h,9*h,cc,h)
  angle(h,h,h)
  carre(h*(9+cc),h*(9+cc),h)
  for i in range(0,cc,2):
    fill_rect(7*h,h*(8+i),h,h,color(255,255,255))
    fill_rect(7*h,h*(9+i),h,h,color(0,0,0))
  for i in range(0,cc,2):
    fill_rect(h*(8+i),h*7,h,h,color(255,255,255))
    fill_rect(h*(9+i),h*7,h,h,color(0,0,0))
  fill_rect(h*9,h*(cc+9),h,h,color(0,0,0))
  copy_qr(1,1,cc+16,cc+16,h)
  sleep(2)
  qr_code_read(cc+16)