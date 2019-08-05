""" Pynput listener to grab screen coordinates. """

def listen(on_move, on_click):
    """ Listen with ``on_move`` and ``on_click`` functions. """
    try:
        from pynput.mouse import Listener
    except:
        print("=================================================================")
        print("Is this machine connected to a display that supports mouse input?")
        print("=================================================================")
        raise OSError("Found no compatible display.")
    # Collect events until released
    with Listener(on_move=on_move, on_click=on_click, on_scroll=None, suppress=False) as listener:
        listener.join()
