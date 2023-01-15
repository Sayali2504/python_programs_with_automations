#pip install scikit-learn
#import required library
from sklearn import tree

# Load the data 

'''
1.Rough =1
2.Smooth = 0
3.Tennis = 1
4.Cricket = 2
'''
Features = [[35,1],[47,1],[90,0],[48,1],[90,1],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]] 
Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

# Decide the machine learning algorithm
obj = tree.DecisionTreeClassifier()

# Perform the traning of model
obj = obj.fit(Features,Labels) #traning - fit method 

# Perform the testing 
print(obj.predict([[97,0],[35,1]]))