import pandas as pd
from sklearn.preprocessing import StandardScaler  
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score , classification_report
import pickle

def createModel(data):
   X = data.drop('diagnosis',axis=1)
   y = data['diagnosis']

   scaler = StandardScaler()

   X = scaler.fit_transform(X)
   
   # data split
   Xtrain , Xtest , ytrain , ytest = train_test_split(X,y , test_size=0.2 , random_state=42)

   # train data    
   model =  LogisticRegression()

   model.fit(Xtrain,ytrain)

   #test model  
   ypred = model.predict(Xtest)

   print(f'Accuracy score is {accuracy_score(ytest,ypred)}')
   print(f'Classification report : {classification_report(ytest,ypred)}') 
   return model , scaler

 

def getCleanData():

    data= pd.read_csv(".\data\data.csv")
    data = data.drop(["Unnamed: 32","id"],axis=1)
    data['diagnosis'] = data['diagnosis'].map({"M" : 1 , "B":0}) 
    

    return data

def main():
    data = getCleanData()
    model , scaler = createModel(data)

    #testModel(model) 
     
    with open('model.pkl',"wb")  as f:
        pickle.dump(model , f)

    with open("scaler.pkl","wb")  as f:
        pickle.dump(scaler,f)   


if __name__ == "__main__":
    main()
 
    



