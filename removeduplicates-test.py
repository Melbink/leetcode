# test_removeDuplicates.py
#import pytest

class solution:
    @staticmethod
    def removeDuplicates(arr):
        hasharr={}
        for number in arr:
            hasharr[number]=hasharr.get(number,0)+1 
        return list(hasharr.keys())
sol = solution()
removeDuplicates = sol.removeDuplicates

def test_unique_values():
    # Test when the array contains unique values only.
    arr = [1, 2, 3, 4, 5]
    # Since the input is already unique, the output should be the same.
    assert removeDuplicates(arr) == [1, 2, 3, 4, 5]

def test_with_duplicates():
    # Test when the array contains duplicates.
    arr = [1, 2, 2, 3, 3, 3, 4]
    expected = [1, 2, 3, 5,4]
    result = removeDuplicates(arr)
    # As dictionary keys preserve insertion order, we expect the result in order of first appearance.
    assert result == expected

def test_empty_array():
    # Test an empty input array.
    arr = []
    assert removeDuplicates(arr) == []

def test_unsorted_input():
    # Test when the array is unsorted.
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = []
    # The order of unique values is defined by the order in which they first appear.
    for num in arr:
        if num not in expected:
            expected.append(num)
    result = removeDuplicates(arr)
    assert result == expected

def test_given_example():
    # Test with the given example input of unique values.
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert removeDuplicates(arr) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]