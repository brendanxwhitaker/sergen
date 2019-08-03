def on_move(x, y):
    global coord_list
    global index
    coord_list.append((x, y))
    print('Pointer moved to {0}'.format((x, y)))
    sys.stdout.flush()
    index += 1

def on_click(x, y, button, pressed):
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
