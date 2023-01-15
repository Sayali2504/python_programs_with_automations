print("Demonstration of list")

# Data : Heterogeneous
# Ordered : Yes
# Mutable : Yes
# Indexed : Yes
# Duplicates : Yes

data = [11,21,51,101,21] #Duplicate 
data1 = [11,90.80,True,"Hello"] #Heterogeneous

print("Data is Heterogenous:",data1)
print("Data is ordered:",data1)
print("Data is index 2:",data1[2]) # Subscript operator -> []
print("Data is duplicate:",data)


print("List is mutable")
data.append(201)
print("Data after append:",data)
data.pop()
print("Data after pop:",data)