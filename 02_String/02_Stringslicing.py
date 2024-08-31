'''
Topic - String Slicing.
'''
s = "pwskills"

# Indexing - Two types 1. Positive 2. Negative
# Positive indexing
print(s[0]) # p
print(s[1]) # w
print(s[2]) # s
print(s[3]) # k
print(s[4]) # i
print(s[5]) # l
print(s[6]) # l
print(s[7]) # s

# Negative indexing
print("--------Negative indexing-----------")
print(s[-1]) 
print(s[-2]) 
print(s[-3]) 
print(s[-4]) 
print(s[-5]) 
print(s[-6])
print(s[-7])
print(s[-8])

# Slicing[m : (n-1)]

print("--------slicing-----")
p = "Harry"
print(p[0:5])
print(p[3:5])
print(p[:]) #prints full
print(p[:5]) #prints full - it automatically take starting point as 0 index

# Negative slicing
print(p[-5:-1])
print(p[-3:-5]) #output - blank
print(p[-4:-1]) #output - blank

# Jump slicing
s = "pwskills"
# [start:stop:step]
print(s[0:7:2])
print(s[1:7:]) #if we not given step size it automaticaly take step size as 1

# it will not show error if it is out of range at stoping point it will print it comes inside
print(s[0:100:2])

# it prints blank
print(s[0:7:-1])

# upperbound minus one 6 to 1 (-1)
print(s[6:1:-1])

# Reverse
print(s[7:0:-1])
print(s[7::-1])
# prints reverse order
print(s[::-1])

a = "Dhanush"
b = "@"
c = 2006

print(a,b,c, end="-", sep="~")