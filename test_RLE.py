from unittest import TestCase
import pytest
import RLE

def test_RLE_1():
    assert RLE.RLE('AAARRRRGGGGGHH', True) == 'A3R4G5H2'

def test_RLE_2():
    assert RLE.RLE('CUTLASSES', compress_ones = True) == 'CUTLAS2ES'

def test_RLE_3():
    assert RLE.RLE('A') == 'A1'