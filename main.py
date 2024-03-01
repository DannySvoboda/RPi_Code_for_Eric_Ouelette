#import modules
import aiy.voicehat
import aiy.audio

def main():
#establish button
  button = aiy.voicehat.get_button()

#wait for button press
  while True:
    print("Press the button for music!")
    button.wait_for_press()
    print("Button pressed, playing music!")
    aiy.audio.play_wave("music_files/Cyborg Ninja.wav")
    print("You played music!")

if __name__ == "__main__":
  main()