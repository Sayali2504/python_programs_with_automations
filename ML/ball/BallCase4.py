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
def BallPredictor(weight,surface):
    Features = [[35,1],[47,1],[90,0],[48,1],[90,1],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]] 
    Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    # Decide the machine learning algorithm
    obj = tree.DecisionTreeClassifier()

    # Perform the traning of model
    obj = obj.fit(Features,Labels) #traning - fit method 

    # Perform the testing 
   # print(obj.predict([[97,0]]))

    ret = obj.predict([[weight,surface]])
    if ret == 1:
        print("Your object looks like a Tennis ball")
    else:
        print("Your object lokks like Cricket ball")    


def main():
    print("----------------------Ball predictor case study----------------")
   
    print("Please enter the weight of your object in grams")
    weight = int(input())

    print("Please enter the type of surface of your object(Rought/ Smooth)")
    surface= input()

    if surface.lower() == "rough":
        surface  = 1
    elif surface.lower == 'smooth':
        surface = 0    
    else: 
        print("Invalid type of surface")    
        exit()

    BallPredictor(weight,surface)

if __name__ == "__main__":
    main()
       