import sys
import random

import numpy as np
import pandas as pd

from typing import List
from screeninfo import get_monitors

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

def on_move(x: int, y: int) -> None:
    global coord_list
    global index
    coord_list.append((x, y))
    print('Pointer moved to {0}'.format((x, y)))
    sys.stdout.flush()
    index += 1

def on_click(x: int, y: int, button, pressed: bool) -> bool:
    global coord_list
    global index
    global start
    global end
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',(x, y)))
    sys.stdout.flush()
    if pressed:
        coord_list.append((x, y))
        index += 1
        start = index
        print("Click down.")
    else:
        coord_list.append((x, y))
        index += 1
        end = index
        print("Click up.")
        # Stop listener
        return False

def resize(coords: np.ndarray, 
           raw_steps: int, 
           REPEAT: bool, 
           TIME_STEPS: int) -> np.ndarray:
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

    return coords

print("Note: this script requires mouse input.")
sys.stdout.flush()

def main(RESHAPE: bool, REPEAT: bool, TIME_STEPS: int) -> None:
    global coord_list
    global index
    global start
    global end
    coord_list = coord_list[start:end]
    coords = np.array(coord_list)
    raw_steps = coords.shape[0]
    coords = coords.astype(float)

    if RESHAPE:
        coords = resize(coords, raw_steps, REPEAT, TIME_STEPS)

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

if __name__ == "__main__":
    # Constants.
    RESHAPE = True
    REPEAT = True
    TIME_STEPS = 500

    """
    We use global variables to avoid having
    to peer into ``pynput`` and mess with their
    ``on_<event>`` functions. 
    """
    # Globals.
    global coord_list
    global index
    global start
    global end
    coord_list = []
    index = 0
    start = 0
    end = 0

    import listener
    listener.listen(on_move, on_click)
    print(coord_list)
    main(RESHAPE, REPEAT, TIME_STEPS)
