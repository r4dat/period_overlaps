import pytest
from period_overlap import overlap_test, DateRange
from datetime import date

a_date_str = '2018-01-15'
b_date_obj = date(2018, 2, 1)
c_date_obj = date(2017,1,1)
a_DateRange = DateRange(date(2017,1,1),date(2017,2,1))
b_DateRange = DateRange(date(2017,1,15),date(2017,4,1))

types_variation_data = [(a_date_str,b_date_obj),
                        (a_date_str,a_date_str),
                        (b_date_obj,a_date_str),
                        ]

@pytest.mark.parametrize("a,b",types_variation_data)
def test_overlap_check_types(a,b):
    with pytest.raises(TypeError):
        overlap_test(a,b)

def test_disjoint():
    ## A < B
    ## B < A
    a = DateRange(date(2017,1,1),date(2017,2,1))
    b = DateRange(date(2017,2,5),date(2017,3,7))
    assert overlap_test(a,b)==False
    assert overlap_test(b,a)==False

def test_partial():
    assert True

def test_subset():
    assert True

def test_identical():
    assert True