"""Code Written by Danny Svoboda on March 1st 2021. 
Intended to be used in a Google AIY Voice Kit Raspberry Pi,
for Eric Ouelette in a robotics project. 
Code is intended to wait for button press, then play audio file."""

#import modules
from aiy.board import Board,Led
import aiy.voice.audio

def main():
#wait for button press
  while True:
    with Board() as board:
      print("Press the button for music!")
      board.button.wait_for_press()
      board.led.state = Led.ON
      print("Button pressed, playing music!")
      aiy.audio.play_wav("music_files/Cyborg Ninja.wav")
      print("You played music!")
  
if __name__ == "__main__":
  main()