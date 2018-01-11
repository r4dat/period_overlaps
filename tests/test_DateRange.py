import pytest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from period_overlap import DateRange
from datetime import date

a_date_str = '2018-01-15'
b_date_obj = date(2018, 2, 1)
c_date_obj = date(2017, 1, 1)

types_variation_data = [(a_date_str, b_date_obj),
                        (a_date_str, a_date_str),
                        (b_date_obj, a_date_str)]


@pytest.mark.parametrize("a,b", types_variation_data)
def test_date_range_types(a, b):
    with pytest.raises(TypeError):
        DateRange(a, b)


def test_date_range_order():
    e_date_obj = date(2018, 2, 1)
    f_date_obj = date(2017, 1, 1)
    with pytest.raises(AttributeError):
        DateRange(e_date_obj, f_date_obj)
