import sys
sys.path.append("../")

from mygeopy.mygeopy.triangle import *

def test_hypot():
    assert hypot(3, 4) == 5
