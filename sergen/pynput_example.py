""" Example of pynput listener usage. """
import sys
from pynput.mouse import Listener

def on_move(x, y):
    """ Function to call on mouse movement. """
    print('Pointer moved to {0}'.format((x, y)))
    sys.stdout.flush()

def on_click(x, y, _, pressed):
    """ Function to call on mouse click. """
    print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
    sys.stdout.flush()
    ret = True
    if not pressed:
        # Stop listener
        ret = False
    return ret

def on_scroll(x, y, _, __):
    """ Function to call on mouse scroll. """
    print('Scrolled {0}'.format((x, y)))

# Collect events until released
with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
