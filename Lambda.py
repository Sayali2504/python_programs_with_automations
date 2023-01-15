
#NOrmal functions
#def Function_name(Function_parameters)
#  Function body

def Add(No1,No2):
    return No1+No2

#Lambda functionas
#lamba parameters : body
'''if you define a function it have name and we call it using that name
but wihtout name we can use lambda function. Can be for short time purpose '''
AddFunction = lambda A,B : A+B

ans = Add(10,11)
ans1 = AddFunction(10,11)

print("Using normal",ans)
print("Using lambda function",ans1)


print("Type of lamba function is",type(AddFunction))