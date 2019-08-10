import time
import RPi.GPIO as GPIO
import pygame
import os
 
#initialise a previous input variable to 0 (assume button not pressed last)
prev_input1 = 0
prev_input2 = 0
prev_input3 = 0  
boton1=17
boton2=27
boton3=22
boton4=23
boton5=24
GPIO.setmode(GPIO.BCM)
GPIO.setup(boton1,GPIO.IN)
GPIO.setup(boton2,GPIO.IN)
GPIO.setup(boton3,GPIO.IN)
GPIO.setup(boton4,GPIO.IN)
GPIO.setup(boton5,GPIO.IN)
 
try:
  pygame.init() 
  infoObject = pygame.display.Info()
  screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h), pygame.FULLSCREEN)
  main_dir = os.path.split(os.path.abspath(__file__))[0]
  file = os.path.join(main_dir, 'img1.jpg')
  surface1 = pygame.image.load(file).convert()
  file = os.path.join(main_dir, 'img2.jpg')
  surface2 = pygame.image.load(file).convert()
  file = os.path.join(main_dir, 'img3.jpg')
  surface3 = pygame.image.load(file).convert()
  file = os.path.join(main_dir, 'img4.jpg')
  surface4 = pygame.image.load(file).convert()
  file = os.path.join(main_dir, 'img5.jpg')
  surface5 = pygame.image.load(file).convert()
  while True:
      #take a reading
      input1 = GPIO.input(boton1)
      input2 = GPIO.input(boton2)
      input3 = GPIO.input(boton3)
      input4= GPIO.input(boton4)
      input5= GPIO.input(boton5)
      #if the last reading was low and this one high, print
      if (input1 && input1 does not equal prev_input):
        screen.fill((0,0,0))
        screen.blit(surface1, (0,0))
        pygame.display.flip() 
        prev_input = input1
        input1=0
      if (input2 && input2 does not equal prev_input):
         screen.fill((0,0,0))
         screen.blit(surface2, (0,0))
         pygame.display.flip()
         prev_input = input2
         input2=0
      if (input3 && input3 does not equal prev_input):
        screen.fill((0,0,0))
         screen.blit(surface3, (0,0))
         pygame.display.flip()
         prev_input = input3
         input3=0
      if (input4 && input4 does not equal prev_input):
         screen.fill((0,0,0))
         screen.blit(surface4, (0,0))
         pygame.display.flip()
         prev_input = input4
         input4=0
       if (input5 && input5 does not equal prev_input):
        screen.fill((0,0,0))
         screen.blit(surface5, (0,0))
         pygame.display.flip()
         prev_input = input5
         input5=0
      #slight pause to debounce
      time.sleep(0.05)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
    pygame.quit()
