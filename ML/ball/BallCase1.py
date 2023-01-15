#pip install scikit-learn
#import required library
from sklearn import tree

# Load the data 
Features = [[35,"Rough"],[47,"Rough"],[90,"Smooth"],[48,"Rough"],[90,"Smooth"],[35,"Rough"],[92,"Smooth"],[35,"Rough"],[35,"Rough"],[35,"Rough"],[96,"Smooth"],[43,"Rough"],[110,"Smooth"],[35,"Rough"],[95,"Smooth"]] 
Labels = ["Tennis","Tennis","Cricket","Tennis","Cricket","Tennis","Cricket","Tennis","Tennis","Tennis","Cricket","Tennis","Cricket","Tennis","Cricket"]

# Decide the machine learning algorithm
obj = tree.DecisionTreeClassifier()

# Perform the traning of model
obj = obj.fit(Features,Labels) #traning - fit method 

# Perform the testing 
print(obj.predict([[97,"Smooth"]]))