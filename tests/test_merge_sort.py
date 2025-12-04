import pytest

from src.merge_sort import merge_sort

def test_merge_sort_empty_arr():
    arr = []
    assert merge_sort(arr) == arr

def test_merge_sort_single_arr():
    arr = [5]
    assert merge_sort(arr) == arr

def test_merge_sort_sorted_arr():
    arr = [1, 2, 3, 4, 5]
    assert merge_sort(arr) == arr

def test_merge_sort_reverse_sorted():
    arr = [5, 4, 3, 2, 1]
    assert merge_sort(arr) == [1, 2, 3, 4, 5]

def test_merge_sort_duplicates():
    arr = [3, 1, 2, 3, 1, 2]
    assert merge_sort(arr) == [1, 1, 2, 2, 3, 3]

def test_merge_sort_negative():
    arr = [-5, -1, -3, -2, -4]
    assert merge_sort(arr) == [-5, -4, -3, -2, -1]

def test_merge_sort_mixed():
    arr = [3, -2, 0, -1, 5]
    assert merge_sort(arr) == [-2, -1, 0, 3, 5]
