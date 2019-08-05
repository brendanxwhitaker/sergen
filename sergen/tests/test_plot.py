import os
import pytest
import shutil
import tempfile
import argparse
import numpy as np
from unittest import TestCase

from sergen import plot

class TestPlot(TestCase):

    def test_main(self):

        tmp_dir = tempfile.mkdtemp()
        # ... do stuff with dirpath

        parser = argparse.ArgumentParser(description='Matplotlib 538-style plot generator.')
        parser.add_argument('--filepath', type=str, help='File to parse and graph.', required=True)
        parser.add_argument('--format', type=str, default='csv', help='`csv` or `json`.')
        parser.add_argument('--phase',
                            type=str,
                            default='',
                            help='The section to graph. One of \'train\', \'validate\', \'test\'.')
        parser.add_argument('--graphs_path',
                            type=str,
                            default='graphs/',
                            help='Where to save graphs.')
        testfile_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),("test.csv"))
        args = parser.parse_args(["--filepath", testfile_path, "--graphs_path", tmp_dir])
        plot.main(args)
        shutil.rmtree(tmp_dir)
