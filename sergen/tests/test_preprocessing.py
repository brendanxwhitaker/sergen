import os
import pytest
import numpy as np
from unittest import TestCase

from sergen import preprocessing

class TestPreprocessing(TestCase):

    def test_read_csv(self):
        csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test.csv")
        dfs, ylabels, column_counts = preprocessing.read_csv(csv_path)
        assert dfs[0].shape == (500, 1)
        assert len(dfs) == 1
        assert len(ylabels) == 1
        assert len(column_counts) == 1
        assert ylabels[0] == "y"
        assert column_counts[0] == 1
    def test_read_json(self):
        json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test.log")
        dfs, ylabels, column_counts = preprocessing.read_json(json_path, "train")
        assert len(dfs) == 6
        assert len(ylabels) == 6
        assert len(column_counts) == 6
        print(column_counts)
        for index in [0, 1, 2, 3, 4]:
            assert dfs[index].shape == (960, 2)
            assert column_counts[index] == 1
        assert dfs[5].shape == (960, 3)
        assert column_counts[5] == 2 
