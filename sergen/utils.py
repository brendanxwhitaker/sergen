import numpy as np

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

def resize(coords: np.ndarray:, raw_steps: int, REPEAT: bool) -> np.ndarray:
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
