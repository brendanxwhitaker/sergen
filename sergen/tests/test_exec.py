import os
import pytest
import numpy as np
from unittest import TestCase

from sergen import gen, listener

class TestExec(TestCase):

    def test_exec(self):
        os.system("coverage run ../gen.py")
        os.system("coverage run ../termplt.py")
