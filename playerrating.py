import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import pickle

data=pd.read_csv("SoccerPlayersData.csv")

data

data.isna().sum()

data=data.fillna(0)

data

le=LabelEncoder()

le_name=le.fit_transform(data['name'])


le_role=le.fit_transform(data['role'])

data['name']=le_name
data['role']=le_role

data

data=data.drop(['player_id','name'],axis=1)

data

x=data.drop('rating',axis=1)
y=data['rating']

x

y

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=30)

lin_reg=LinearRegression()

lin_reg.fit(x_train,y_train)

lin_reg.score(x_test,y_test)

pr_model=RandomForestRegressor(random_state=10)
pr_model.fit(x_train,y_train)
pr_model.score(x_test,y_test)

pickle.dump(pr_model, open('pr_model.pkl','wb'))
            