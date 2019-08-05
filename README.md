# sergen

A library for rapid automatic generation of sample time series data via mouse input. 

Requires a machine with a display and support for mouse input. 

![alt text](https://raw.githubusercontent.com/brendanxwhitaker/sergen/master/sergen/graphs/sawtooth.PNG)

### Generating time series

To generate time series, run the command:
```
python3 gen.py
```
and follow the instructions. Click and drag anywhere to draw a figure (script tracks mouse movement). The portion on mouse movement between first depress and first release is used to create time series data. The x-position is not used, hence to make interpretable movements, only move the mouse rightward, up, and down. 

Saving to the `series/` directory is recommended. 

### Plotting in terminal with `terminalplot`

To plot in the terminal, run the command: 
```
python3 termplt.py
```
and follow the instructions.

### Plotting in svg files in `matplotlib`

Run the command:
```
python3 plot.py --filepath <path_to_file>
```
to generate a `.svg` graph. 

### TODO

- [x] Make `gen.py` script read filename input from bash. 
- [x] Make directory for saved `.csv` files. 
- [x] Build script for processing and graphing saved files.
- [x] Remove x-axis from numpy array. 
- [x] Print with `terminalplot`.  
- [x] Change saved `.csv` to a single column.
- [x] Print with `plotplotplot` library.
- [x] Verify that `.csv` files with less than 100,000 rows with fit in the github repo.
- [x] Add `argparse` support which reads filename from `stdin` if no argument is passed, and uses specified filename otherwise. (Veto)
- [x] Update README with usage information.
- [x] Make `tests` directory. 
- [x] Write tests.
- [x] Write note in README explaining why `gen.py` does not have proper module structure.
- [x] Lint. 
- [ ] Add codecov.

Lacks proper python3 module structure by heuristic and for simplicity. 

Note: the repo name "sergen" stands for series generation. 

