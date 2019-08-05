""" Plots a ``.csv`` file to terminal. """
import os
import platform
import numpy as np
import pandas as pd
from terminalplot import plot

assert platform.system() == 'Linux'
assert os.path.isdir("series/")
print("The following files are available to print (by entering `series/<name>.csv`):")
os.system("ls series/")
PATH = input("Enter the path to a saved curve as a csv: ")
RAW_SERIES = pd.read_csv(PATH)
SERIES = np.array(RAW_SERIES)
y = list(SERIES[:, 0])     # Assumes 2-dimensional data.
x = [i for i in range(SERIES.shape[0])]
plot(x, y)
print("Series shape:", SERIES.shape)
