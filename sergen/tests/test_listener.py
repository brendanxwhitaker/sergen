import pytest
import numpy as np
from unittest import TestCase

from sergen import gen, listener

coord_list = []
index = 0
start = 0
end = 0

class TestListener(TestCase):
    error_text = "Found no compatible display."
    try:
        listener.listen(gen.on_move, gen.on_click)
    except OSError as e:
        assert str(e) == error_text
