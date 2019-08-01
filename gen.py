from pynput.mouse import Listener

def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0}'.format(
        (x, y)))

def _sergen_logger(cls, log_path):
    """Creates a logger with a name suitable for a specific class.
    This function takes into account that implementations for classes reside in
    platform dependent modules, and thus removes the final part of the module
    name.
    :param type cls: The class for which to create a logger.
    :param type log_path: The path of the log file to which we write. 
    :return: a logger
    """
    import logging
    logging.basicConfig(filename=log_path,level=logging.DEBUG)
    return logging.getLogger('{}.{}'.format(
        '.'.join(cls.__module__.split('.', 2)[:2]),
        cls.__name__))

# Collect events until released
with Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()
