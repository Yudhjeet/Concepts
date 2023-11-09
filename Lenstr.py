#Backslash are not counted in the size of the strings, e.g

str= '1\
2\
3'

print("Size of String I:", len(str))

#However, EOL (End Of Line) are counted, this includes enter key spaces, e.g

str2= '''A
B
C'''

print("Size of String II:", len( str2))