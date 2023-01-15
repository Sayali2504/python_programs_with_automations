import sys

print(sys.getrecursionlimit()) #default recursion limit is 1000

sys.setrecursionlimit(3001)        

print(sys.getrecursionlimit()) #we can increase the recursion limit
