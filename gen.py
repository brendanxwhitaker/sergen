from pynput.mouse import Listener
import numpy as np
import random

# Expand mode and Repeat mode.
REPEAT = True
TIME_STEPS = 1000
coord_list = []
index = 0
start = 0
end = 0

"""
We use global variables to avoid having
to peer into ``pynput`` and mess with their
``on_<event>`` functions. 
"""
def on_move(x, y):
    global coord_list
    global index
    coord_list.append((x, y))
    index += 1

def on_click(x, y, button, pressed):
    global coord_list
    global index
    global start
    global end
    if pressed:
        coord_list.append((x, y))
        index += 1
        start = index
    else:
        coord_list.append((x, y))
        index += 1
        end = index
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=None,
        suppress=False) as listener:
    listener.join()

coords = np.array(coord_list)
raw_steps = coords.shape[0]
coords = coords.astype(float)

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

print("coords shape:", coords.shape)
print(coords)
np.savetxt("coords.csv", coords, delimiter=",")
