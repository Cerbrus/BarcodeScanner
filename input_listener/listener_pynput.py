import re

import requests
from pynput import keyboard

apiEndpoint = 'http://localhost:5000/barcode/{}'
input = ''

def on_press(key):
    global input
    if isinstance(key, keyboard.KeyCode) and re.match(r'[0-9]', key.char):
        input += key.char
    elif key == keyboard.Key.enter:
        try:
            print('Scanned barcode:', input)
            requests.get(apiEndpoint.format(input))
        except Exception as e:
            print('Error sending request:', e)
        input = ''

# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()