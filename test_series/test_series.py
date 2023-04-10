import pytest
from series.series import sum_series
from series.series import fibonacci
from series.series import lucas

def test_fab_function_index0 ():
     actual=fibonacci(0)
     expected=0
     assert actual == expected

def test_fab_function_index1 ():
     actual=fibonacci(1)
     expected=1
     assert actual == expected

def test_fab_function_index2 ():
     actual=fibonacci(2)
     expected=1
     assert actual == expected

def test_fab_function_index3 ():
     actual=fibonacci(3)
     expected=2
     assert actual == expected

def test_fab_function_index4 ():
     actual=fibonacci(4)
     expected=3
     assert actual == expected
#########################################

def test_lucas_function_index0 ():
     actual=lucas(0)
     expected=2
     assert actual == expected

def test_lucas_function_index1 ():
     actual=lucas(1)
     expected=1
     assert actual == expected

def test_lucas_function_index2 ():
     actual=lucas(2)
     expected=3
     assert actual == expected

def test_lucas_function_index3 ():
     actual=lucas(3)
     expected=4
     assert actual == expected

def test_lucas_function_index4 ():
     actual=lucas(4)
     expected=7
     assert actual == expected

#############################################


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

################################################

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

#####################################################

def test_sum_with_index_0_and_wrong_parameters():
    actual=sum_series(0,3,4)
    expected=0
    assert actual == expected

def test_sum_with_index_1_and_wrong_parameters():
    actual=sum_series(1,4,5)
    expected=1
    assert actual == expected

def test_sum_with_index_2_and_wrong_parameters():
    actual=sum_series(2,5,9)
    expected=1
    assert actual == expected

def test_sum_with_index_3_and_wrong_parameters():
    actual=sum_series(3,7,6)
    expected=2
    assert actual == expected

def test_sum_with_index_4_and_wrong_parameters():
    actual=sum_series(4,7,6)
    expected=3
    assert actual == expected


