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

disjoint_data = [( DateRange(date(2017,1,1),date(2017,2,1)), DateRange(date(2017,2,5),date(2017,3,7)) ),
                 ( DateRange(date(2017,2,5),date(2017,3,7)), DateRange(date(2017,1,1),date(2017,2,1)) )]

@pytest.mark.parametrize("a,b",disjoint_data)
def test_disjoint(a,b):
    ## A < B
    ## B < A
    assert overlap_test(a,b)==False
    assert overlap_test(b,a)==False

partial_data = [( DateRange(date(2017,1,1),date(2017,3,1)), DateRange(date(2017,2,5),date(2017,9,7)) ),
                ( DateRange(date(2017,2,5),date(2017,9,7)), DateRange(date(2017,1,1),date(2017,3,1)) )]

@pytest.mark.parametrize("a,b",partial_data)
def test_partial(a,b):
    assert overlap_test(a,b) == True
    assert overlap_test(b,a) == True


subset_data = [( DateRange(date(2017,1,1),date(2017,12,1)), DateRange(date(2017,2,5),date(2017,3,7)) ),
               ( DateRange(date(2017,1,5),date(2017,3,7)), DateRange(date(2017,1,1),date(2017,12,1)) )]
@pytest.mark.parametrize("a,b",subset_data)
def test_subset(a,b):
    assert overlap_test(a,b) == True
    assert overlap_test(b,a) == True

def test_identical():
    a = DateRange(date(2017, 1, 1), date(2017, 2, 1))
    b = DateRange(date(2017, 1, 1), date(2017, 2, 1))
    assert overlap_test(a,b)==True
    assert overlap_test(b,a)==True
