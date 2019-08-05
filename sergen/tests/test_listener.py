import pytest
import numpy as np
from unittest import TestCase

from sergen import gen, listener

class TestListener(TestCase):
    def test_listen(self):
        error_text = "Found no compatible display."
        try:
            listener.listen(gen.on_move, gen.on_click)
        except OSError as e:
            assert str(e) == error_text
