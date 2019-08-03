import pytest
from unittest import TestCase
from sergen import gen

coord_list = []
index = 0
start = 0
end = 0

class TestGen(TestCase):
    # Globals.
    global coord_list
    global index
    global start
    global end

    def test_on_move(self):
        global coord_list
        global index
        global start
        global end
        coord_list = []
        index = 0
        start = 0
        end = 0

        gen.on_move(0,0)
        assert coord_list == [[0,0]] 
        
    
