from random import random

def rand(n):
  return int(random() * n) % n

def collision(r1, r2):
  _1r2 = r1.x > r2.x+r2.w
  _2r1 = r2.x > r1.x+r1.w
  _1b2 = r1.y > r2.y+r2.h
  _2b1 = r2.y > r1.y+r1.h
  return not (_1r2 or _2r1 or _1b2 or _2b1)
