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

def resize(coords: np.ndarray:, raw_steps: int) -> np.ndarray:
    """Resizes first dim of coordinate array. """
    # Interpolate time series. 
    if REPEAT:
        full_reps = TIME_STEPS // raw_steps
        reps = [coords] * full_reps
        coords = np.concatenate(reps)
        raw_steps = coords.shape[0]

    while REPEAT and raw_steps < TIME_STEPS:
        diff = TIME_STEPS - raw_steps
        coords = np.concatenate([coords, coords[:diff]])
        raw_steps = coords.shape[0]

    while not REPEAT and raw_steps < TIME_STEPS:
        add_loc = random.randint(0,raw_steps - 2) # Inclusive right index. 
        p1 = coords[add_loc]
        p2 = coords[add_loc + 1]
        mean = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
        coords = np.insert(coords, add_loc + 1, mean, 0)
        raw_steps = coords.shape[0]

    # Filter time series. 
    while raw_steps > TIME_STEPS:
        del_loc = random.randint(0,raw_steps - 1)
        coords = np.delete(coords, del_loc, 0)
        raw_steps = coords.shape[0]

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
