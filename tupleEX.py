#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jd0919889
#
# Created:     31/10/2019
# Copyright:   (c) jd0919889 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
tuplel = ("John", "Doe", 45, "Dog", True)
x = list(tuplel)
x[0] = "Joe"

print(tuplel)
print(tuplel[2])
print(tuplel[-1])
print(tuplel[1:3])
print(tuplel[0:4])
