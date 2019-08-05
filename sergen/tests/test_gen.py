import pytest
import numpy as np
from sergen import gen
from unittest import TestCase

coord_list = []
index = 0
start = 0
end = 0

class TestGen(TestCase):

    def test_resize_repeat(self):
        coords = np.random.rand(143, 2)
        raw_steps = 143
        REPEAT = True
        TIME_STEPS = 1000
        res = gen.resize(coords, raw_steps, REPEAT, TIME_STEPS) 
        assert tuple(res.shape) == (1000, 2)
        np.testing.assert_array_almost_equal(res[142], res[857])
    
    def test_resize_no_repeat(self):
        coords = np.random.rand(143, 2)
        raw_steps = 143
        REPEAT = False
        TIME_STEPS = 1000
        res = gen.resize(coords, raw_steps, REPEAT, TIME_STEPS) 
        assert tuple(res.shape) == (1000, 2)
    
    def test_resize_truncate_repeat(self):
        coords = np.random.rand(1430, 2)
        raw_steps = 1430
        REPEAT = True
        TIME_STEPS = 1000
        res = gen.resize(coords, raw_steps, REPEAT, TIME_STEPS) 
        assert tuple(res.shape) == (1000, 2)
    
    def test_resize_truncate_no_repeat(self):
        coords = np.random.rand(1430, 2)
        raw_steps = 1430
        REPEAT = False
        TIME_STEPS = 1000
        res = gen.resize(coords, raw_steps, REPEAT, TIME_STEPS) 
        assert tuple(res.shape) == (1000, 2)
    
    def test_main(self):
        coord_list = []
        for i in range(259):
            coord_list.append(tuple([i, i*i]))
        index = 259
        start = 205
        end = 253
        RESHAPE = True
        REPEAT = True
        TIME_STEPS = 998
        SAVE_CSV = False
        df = gen.main(coord_list, start, end, RESHAPE, REPEAT, TIME_STEPS, SAVE_CSV)
        assert df.shape == (998, 1)
        coords = np.array(coord_list[start:end])
        height = max(coords[:, 1])
        assert df['y'][767] == height - coords[47, 1]

    def test_on_move(self):
        error_text = "name 'coord_list' is not defined"
        try:
            gen.on_move(0, 0)
        except NameError as e:
            assert str(e) == error_text
    
    def test_on_click(self):
        error_text = "name 'coord_list' is not defined"
        try:
            gen.on_click(0, 0, None, True)
        except NameError as e:
            assert str(e) == error_text
