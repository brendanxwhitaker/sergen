import sys
import random

import numpy as np
import pandas as pd

from typing import List
from screeninfo import get_monitors
try:
    from pynput.mouse import Listener
except:
    print("=================================================================")
    print("Is this machine connected to a display that supports mouse input?")
    print("=================================================================")
    raise OSError

"""
DOCSTRING
Constants:
    **REPEAT**: ``bool``:
        Whether to repeat/loop the sequence to extend the 
        number of time steps, or to expand it by interpolation. 
    **TIME_STEPS: ``int``:
        Desired number of time steps in the time series. 

Global variables:
    **coord_list**: ``List[List[int]]`` of shape ``(raw_steps, 2)``: 
        Planar coordinates of the captured mouse positions from the 
        ``on_move`` and ``on_click`` events. 
    **index**: ``int``:
        Number of (not necessarily unique) coordinate positions seen 
        so far. 
    **start**: ``int``: 
        Index of first click depress. 
    **end**: ``int``:
        Index of first click release.       
"""

# Constants.
RESHAPE = True
REPEAT = True
TIME_STEPS = 500

# Globals.
coord_list = []
index = 0
start = 0
end = 0

print("Note: this script requires mouse input.")
sys.stdout.flush()
"""
We use global variables to avoid having
to peer into ``pynput`` and mess with their
``on_<event>`` functions. 
"""

# Collect events until released
with Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=None,
        suppress=False) as listener:
    listener.join()

coord_list = coord_list[start:end]
coords = np.array(coord_list)
raw_steps = coords.shape[0]
coords = coords.astype(float)

if RESHAPE:
    coords = resize(coords, raw_steps, REPEAT)


name = input("Enter a path for the saved file (include `.csv`): ")
coords_df = pd.DataFrame(coords)
coords_df.columns = ['x', 'y']
coords_df = coords_df.drop(['x'], 1)
for m in get_monitors():
    height = m.height
    width = m.width

coords_df['y'] = height - coords_df['y']
coords_df.to_csv(name, index=False)
print(coords_df)
