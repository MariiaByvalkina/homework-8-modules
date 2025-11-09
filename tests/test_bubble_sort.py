from src.bubble_sort import bubble_sort

import pytest

def test_bubble_empty():
    arr = []
    assert bubble_sort(arr) == arr

def test_bubble_single():
    arr = [10]
    assert bubble_sort(arr) == arr

def test_bubble_single_element():
    arr = [1, 1, 1, 1]
    assert bubble_sort(arr) == arr

def test_bubble_negative():
    arr = [-1, -3, -7, -5]
    result = [-7, -5, -3, -1]
    assert bubble_sort(arr) == result
