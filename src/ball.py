from sys import exit

from constants import *
from functions import *

class Ball:
  def __init__(self,coord, paddles):
    self.x = coord[0]
    self.y = coord[1]
    self.w = 10
    self.h = 10
    self.vx = 5 
    self.vy = 5.0
    if rand(2):
      self.vx *= -1
    if rand(2):
      self.vy *= -1
    self.paddles = paddles

  def render(self):
    pygame.draw.rect(WINDOW, (255,255,255), (self.x,self.y,self.w,self.h))

  def run(self):
    for i in range(len(self.paddles)):
      if self.paddles[i].score >= 15:
        print("Player %i Wins" % int(i+1))
        pygame.quit()
        exit()
    self.x += self.vx
    self.y += self.vy
    if self.y < 0 or self.y+self.h > WIN_SIZE[1]:
      self.vy *= -1.01

    if self.x+self.w < 0 or self.x > WIN_SIZE[0]:
      if self.x+self.w < 0:
        self.paddles[1].score += 1
      elif self.x > WIN_SIZE[0]:
        self.paddles[0].score += 1
      self.x = WIN_SIZE[0] / 2
      self.y = WIN_SIZE[1] / 2

    for p in self.paddles:
      if collision(self, p):
        self.vx *= -1.05
    self.render()
