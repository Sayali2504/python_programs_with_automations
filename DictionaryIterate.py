print("Demonstration of Dictionary")

# Data : Heterogeneous
# Ordered : Yes
# Mutable : Yes
# Indexed : No
# Duplicates : Key -> No , Value -> Yes

programming = {"C":"Ritchie", "C++":"Stroustrup","Java":"Gosling","Python":"Rossum"}

Batches = {"PPA":18000,"LB":16700,"Python":16500,"Angular":15000}

print("Data of dictionary")

print("Data traversal using for loop get keys only ")

for x in Batches:
    print(x)


print("Data traversal using for loop  get key and value")

for x in Batches:
    print(x,Batches[x])


print("Data traversal using for loop  get key and value")

for x in Batches:
    print(x,Batches.get(x))

keys  = Batches.keys()

print(type(keys))
print(keys)

valuebatches = Batches.values()
print(type(valuebatches))
print(valuebatches)


#program for dictionary in dictionary
