import pytest
from series.series import sum_series
from series.series import fibonacci
from series.series import lucas

def test_fab_function ():
     actual=fibonacci(0)
     expected=0
     assert actual == expected

def test_lucas_function ():
     actual=lucas(0)
     expected=2
     assert actual == expected


def test_fab_with_index_0():
    actual=sum_series(0)
    expected=0
    assert actual == expected

def test_fab_with_index_1():
    actual=sum_series(1)
    expected=1
    assert actual == expected

def test_fab_with_index_4():
    actual=sum_series(4)
    expected=3
    assert actual == expected

def test_lucas_with_index_0_and_right_parameters():
    actual=sum_series(0,2,1)
    expected=2
    assert actual == expected

def test_lucas_with_index_1_and_right_parameters():
    actual=sum_series(1,2,1)
    expected=1
    assert actual == expected

def test_lucas_with_index_4_and_right_parameters():
    actual=sum_series(4,2,1)
    expected=7
    assert actual == expected

def test_lucas_with_index_5_and_wrong_parameters():
    actual=sum_series(5,1,1)
    expected=16
    assert actual == expected


