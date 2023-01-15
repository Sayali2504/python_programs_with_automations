print("Tuple Iteration")

# Data : Heterogeneous
# Ordered : Yes
# Mutable : NO
# Indexed : Yes
# Duplicates : Yes

Data = (11,21,51,101)

print("Output using for loop")

for no in Data:    #like foreach loop
    print(no , end=" ")
print("\n________________________________________")

print("Output using for loop with index")

for i in range(0,len(Data)): #normal for
    print(Data[i] , end=" ")
print("\n________________________________________")

print("Output using for while with index")
i = 0
while(i < len(Data)):
    print(Data[i] , end=" ")
    i+=1
print("\n________________________________________")