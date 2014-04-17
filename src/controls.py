from constants import *

keys = []
for i in range(0xFFFF):
  keys.append(0)

def controls_run():
  global keys
  for e in pygame.event.get():
    if e.type == pygame.KEYDOWN:
      keys[e.key] = 1
    elif e.type == pygame.KEYUP:
      keys[e.key] = 0

      #if e.key == pygame.K_UP:
        #self.y -= 5
      #elif e.key == pygame.K_DOWN:
        #self.y += 5
