# R4dat
# 2018-01-02

from datetime import date
from collections import namedtuple

class DateRange():
    def __init__(self,begin,end):
        _begin_type_check = isinstance(begin,date)
        _end_type_check = isinstance(end,date)
        if not (_begin_type_check or _end_type_check):
            raise TypeError("begin or end is not a datetime.date")
        if not (begin<=end):
            raise AttributeError("Start date must be <= end date")

        self.begin = begin
        self.end = end

a = Date_Range(begin = date(2017,1,1),end = date(2017,2,1))
b = Date_Range(begin = date(2017,1,15),end = date(2017,5,1))

def overlap_test(a,b):
    print('stub')
    raise NotImplementedError
    return False
