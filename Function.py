__author__ = 'dimage01'

import copy


"Cong hoa xa hoi chu nghia Viet Nam"
"This file for testing function"


def sortList(list):
    "this function will sort my list "
         # aList = list[:]
    #aList = copy.copy(list)
    aList = list
    aList.sort()

    return aList


aList = [1,6,3,5,4,9,0]

print sortList(aList)
print(aList)


#!/usr/bin/python

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [3,2,4,32,13]; # This would assig new reference in mylist
   print "Values inside the function: ", mylist
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist