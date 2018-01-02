# R4dat
# 2018-01-02

from datetime import date
from collections import namedtuple

Date_Range = namedtuple('begin','end')

a = Date_Range(begin = date(2017,1,1),end = date(2017,2,1))
b = Date_Range(begin = date(2017,1,15),end = date(2017,5,1))

def overlap_test(a,b):
    print('stub')
    raise NotImplementedError
    return False
