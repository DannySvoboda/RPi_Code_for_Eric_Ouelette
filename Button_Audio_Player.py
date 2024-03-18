"""Code Written by Danny Svoboda on March 1st 2021. 
Intended to be used in a Google AIY Voice Kit Raspberry Pi,
for Eric Ouelette in a robotics project. 
Code is intended to wait for button press, then play audio file."""

#import modules
from aiy.board import Board,Led
import pygame

def main():
#wait for button press
  pygame.mixer.init()
  pygame.mixer.music.load("music_files/MP3s(For_Storage)/Cyborg Ninja.mp3")
  while True:
    with Board() as board:
      print("Press the button for music!")
      board.button.wait_for_press()
      board.led.state = Led.ON
      print("Button pressed, playing music!")
      pygame.mixer.music.play()       
      print("You played music!")
  
if __name__ == "__main__":
  main()