# it3038c-scripts

Lab 7

I downloaded the pygame plugin, which allows you to make games from python.

Create a vitual environment:

  virtualenv c:\it3038c-scripts\venv\pygame
  source c:\it3038c-scripts\venv\Webscraping\activate.ps1
  
Then install pygame:
  
  pip install pygame
    
First we need to make a game window:

  import pygame
  pygame.init()
  window = pygame.display.set_mode((800,600)
  
Then title the pop-up window:

  pygame.display.set_caption("Lab 7")
  
And last, to make sure it doesn't disappear as soon as its created, a wait command.

  pygame.time.wait(3600)
  pygame.quit()
  
That was the game window you created! Remember to deactivate.

  deactivate
