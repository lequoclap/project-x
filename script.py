# var = 2 ** 3
# print var ** 2



# testing while
#
#
# count = 10
# while (count > 5):
#     print "number :", count
#     count = count - 1
#
# testing else in while
#
# count = 10
# while(count > 7):
#     print "So chan ", count
#     count = count -1
# else:
#     print "So le:",count
#     count = count -1
# print "good bye!"
#
# # testing else in for loop
#
# array = ["a","b","c"]
# for i in range(len(array)):
#     print array[i]
# else:
#     print i;
#
# for i in array:
#     print i
#
#     for c in "frenzy":
#         print c



for num in range(10,20):  #to iterate between 10 to 20
   for i in range(2,num): #to iterate on the factors of the number
      if num%i == 0:      #to determine the first factor
         j=num/i          #to calculate the second factor
         print '%d equals %d * %d' % (num,i,j)
         break #to move to the next number, the #first FOR
   else:                  # else part of the loop
        print num, 'is a prime number'

else:
    print "Goodbye!"