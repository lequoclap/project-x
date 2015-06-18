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
   mylist = [1,65,4,32,13]; # This would assig new reference in mylist
   print "Values inside the function: ", mylist
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist


def printme( str = "kule kelu" ):
   "This prints a passed string into this function"
   print str;
   return;

# Now you can call printme function
printme( str = "My string")
printme("My string")
printme()


# Function definition is here
def printinfo( arg1, *arg2):
   "This prints a variable passed arguments"
   print "Output is: "
   print arg1
   for var in arg2:
       print var, "arg2"
   return;

# Now you can call printinfo function
printinfo( 10 );
printinfo( "hello","ohayou","merci");









