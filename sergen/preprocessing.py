""" Read data from a specified filepath and pass to ``plot.py``. """

import json

import pandas as pd
# pylint: disable=too-many-locals, too-many-statements

#DATA PREPROCESSING

def read_csv(file_path):
    """ Read data to be plotted from a ``.csv`` file. """

    print("Reading from file:", file_path)

    csv = pd.read_csv(file_path)
    keys = list(csv.columns)
    dfs = []

    column_counts = []
    i = 0
    for i, _ in enumerate(keys):
        column_counts.append(1)
        i += 1

    # Iterate over column split, and create a seperate DataFrame for
    # each subplot. Add the subplot names to `ylabels`.
    ylabels = []
    for i, count in enumerate(column_counts):
        key_list = []
        if count == 1:
            ylabels.append(keys[i])
            key_list.append(keys[i])
            dfs.append(csv[key_list])
        else:
            words = []
            for j in range(count):
                words.append(keys[i + j])
                words.append("/")
                key_list.append(keys[i + j])
            ylabels.append("".join(words[:-1]))
            dfs.append(csv[key_list])
    print("Generating", len(dfs), "subplots.")

    return dfs, ylabels, column_counts

def read_json(file_path, phase):
    """ Read data to be plotted from a ``.json`` file. """

    phases = ['train', 'validate', 'test']
    assert phase in phases

    print("Reading from file:", file_path)

    def isfloat(x):
        try:
            float(x)
        except ValueError:
            return False
        else:
            return True

    def isint(x):
        try:
            aval = float(x)
            bval = int(aval)
        except ValueError:
            return False
        else:
            return aval == bval

    with open(file_path, encoding='utf-8') as json_file:
        json_data = json.load(json_file)

        phase_key = phase + "Results"

        row_list = []
        log_list = json_data[phase_key]

        # Construct train array.
        for i, stepdict in enumerate(log_list):
            row = []
            for key, val in stepdict.items():
                if isint(val):
                    row.append(int(val))
                elif isfloat(val):
                    row.append(float(val))
                else:
                    row.append(val)
            row_list.append(row)

        log_df = pd.DataFrame(log_list)
        keys = list(log_df.columns)
        log_df['index'] = log_df.index
        log_df['index'] = log_df['index'].apply(lambda x: x * 10)

    dfs = []

    # This column_counts generation process assumes
    # `top5` always follows `top1` in keys.
    column_counts = []
    i = 0
    # pylint: disable=consider-using-enumerate
    for i in range(len(keys)):
        key = keys[i]
        if key == 'top1':
            column_counts.append(2)
        elif key != 'top5':
            column_counts.append(1)
        i += 1

    # Iterate over column split, and create a seperate DataFrame for
    # each subplot. Add the subplot names to `ylabels`.
    ylabels = []
    for i, count in enumerate(column_counts):
        key_list = ['index']
        if count == 1:
            ylabels.append(keys[i])
            key_list.append(keys[i])
            dfs.append(log_df[key_list])
        else:
            words = []
            for j in range(count):
                words.append(keys[i + j])
                words.append("/")
                key_list.append(keys[i + j])
            ylabels.append("".join(words[:-1]))
            dfs.append(log_df[key_list])
    print("Generating", len(dfs), "subplots.")

    return dfs, ylabels, column_counts
