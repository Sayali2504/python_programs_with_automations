print("Demonstration of SET")

# Data : Heterogeneous
# Ordered : NO
# Mutable : Yes
# Indexed : NO
# Duplicates : No

data = {11,21,51,101,21} 
data1 = {11,90.80,True,"Hello"} #Heterogeneous

print(data)
print(data1)

print("Length of data:",len(data))
print("Data is Heterogenous:",data1)
# print("Data is ordered:",data1)
# print("Data is index 2:",data1[2])
# print("Data is duplicate:",data)


print("Set is mutable")
#insert element

data.add(211)
print("Data after insertion: ",data)

#remove element 
data.remove(211) #if value does not exist it return exception , we can use to show validation that value does not exist
print("Data after removal: ",data)

#remove element
data.discard(201)
print("Data after discard: ",data)