__author__ = 'dimage01'

import copy


"Cong hoa xa hoi chu nghia Viet Nam"
"This file for testing function"


def sortList(list):
    "this function will sort my list "
         # aList = list[:]
    aList = copy.copy(list)
    aList.sort()

    return aList


aList = [1,6,3,5,4,9,0]

print sortList(aList)
print(aList)
