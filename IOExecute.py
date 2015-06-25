__author__ = 'dimage01'


fo = open("commit2.txt","w+")
print "name:",fo.name
print "closed or not",fo.closed
fo.write("hey hey Python! Im here with you!")

# print "opening mode",fo.mode
fo.close()

fo = open("commit2.txt","r")
str = fo.read()
print str



