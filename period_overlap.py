# R4dat
# 2018-01-02

from datetime import date

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


def overlap_test(a,b):
    # Instance using DateRange object
    _a_check = isinstance(a, DateRange)
    _b_check = isinstance(b, DateRange)
    if not (_a_check or _b_check):
        raise TypeError("a or b not a DateRange object")

    if (a.end < b.begin) or (b.end<a.begin):
        return False

    print('stub')
    raise NotImplementedError
    return False