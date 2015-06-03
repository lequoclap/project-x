__author__ = 'dimage01'




list1 = [5]

print list1

list2 = [2,90,"v"]

list2.sort()
print(list2)
print cmp(list1,list2)

# Phep so sanh cmp se so sanh tung element giua cac list, doi chieu tung phan tu. Bat dau tu phan tu dau tien

tup1 = (1,2,3,4,5)

print tup1


dict = {
    'name':'LAPLQ',
    'age':'23'
}

print "I know who I am, and I am %s and %s year old " % (dict['name'],dict['age'])

print type(dict), type(list1), type(tup1)

seq = ('name', 'age', 'sex')

# dict = dict.fromkeys(seq)
# print "New Dictionary : %s" %  str(dict)

dict = dict.fromkeys(seq,2)
print "New Dictionary : %s" %  str(dict)



dict = {'Name': 'Zara', 'Age': 7}
dict2 = {'Age': 'female' }

dict.update(dict2)
print "Value : %s" %  dict