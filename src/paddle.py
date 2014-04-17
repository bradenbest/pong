from constants import *
from controls import *

class Paddle:
  def __init__(self, coord, AI):
    self.x = coord[0]
    self.y = coord[1]
    self.w = 20
    self.h = 100
    self.AI = AI
    self.score = 0
  def render(self):
    pygame.draw.rect(WINDOW,(255,255,255),(self.x,self.y,self.w,self.h))
  def run(self, ball):
    if self.AI:
      if self.y+(self.h/2) < ball.y and self.y+(self.h) <= WIN_SIZE[1]:
        self.y += 5
      elif self.y+(self.h/2) > ball.y and self.y >= 0:
        self.y -= 5
    else:
      controls_run()
      if keys[pygame.K_UP] and self.y >= 0:
        self.y -= 10
      elif keys[pygame.K_DOWN] and self.y+(self.h) <= WIN_SIZE[1]:
        self.y += 10
    self.render()
