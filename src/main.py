from time import sleep

from constants import *
from paddle import *
from ball import *

def main():
  p1 = Paddle((0,WIN_SIZE[1] / 2 - 50),0)
  p2 = Paddle((WIN_SIZE[0]-20, WIN_SIZE[1] / 2 - 50),1)
  ball = Ball((WIN_SIZE[0]/2, WIN_SIZE[1]/2), [p1,p2])
  font = pygame.font.Font(None, 100)
  while 1:
    WINDOW.fill((0,0,0))
    p1.run(ball)
    p2.run(ball)
    ball.run()
    pygame.draw.rect(WINDOW,(255,255,255),(WIN_SIZE[0]/2-10,0,20,WIN_SIZE[1]))
    
    label = font.render("%i" % p1.score, 1, (255,255,255))
    WINDOW.blit(label, (WIN_SIZE[0]/4,20))

    label = font.render("%i" % p2.score, 1, (255,255,255))
    WINDOW.blit(label, ((WIN_SIZE[0]/4) * 3,20))
    for i in range(WIN_SIZE[1]):
      if i % 2:
        pygame.draw.line(WINDOW,SCANLINE_COLOR,(0,i),(WIN_SIZE[0],i))
    pygame.display.update()
    sleep(DELAY)

main()
