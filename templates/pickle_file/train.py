import pandas as pd
import numpy as np
import joblib

df = pd.read_csv('https://raw.githubusercontent.com/siddharthzs/stress_management/master/m14_merged.csv', index_col=0)
# df = pd.read_csv('data/m14_merged.csv')

feats =   ['BVP_mean', 'BVP_std', 'EDA_phasic_mean', 'EDA_phasic_min', 'EDA_smna_min', 
           'EDA_tonic_mean', 'Resp_mean', 'Resp_std', 'TEMP_mean', 'TEMP_std', 'TEMP_slope', 'BVP_peak_freq', 'age', 'height', 'weight', 'label']  

df2 = df[feats]
X = df2.drop('label', axis=1).values
y = df2['label'].values
df2.label.value_counts()


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)  




#DECISION TREE
from sklearn import tree
model = tree.DecisionTreeClassifier()
model.fit(X_train,y_train)
model.score(X_test,y_test)
filename = 'decisionTree_model.sav'
# pickle.dump(model, open(filename, 'wb'))
joblib.dump(model, 'decisionTree_model.pkl')








#BAGGING MODEL -  RANDOM FOREST ALGORITHM 
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=40)#doubt 
model.fit(X_train,y_train)
model.score(X_test,y_test)
# filename = 'gradBoost_model.sav'
# pickle.dump(model, open(filename, 'wb'))
joblib.dump(model, 'gradBoost_model.pkl')



#GRADBOOST ALGORITHM 
from sklearn.ensemble import GradientBoostingClassifier
model = GradientBoostingClassifier(random_state=0) 
model.fit(X_train,y_train)
# model.score(X_test,y_test)
# filename = 'randomForest_model.sav'
# pickle.dump(model, open(filename, 'wb'))
joblib.dump(model, 'randomForest_model.pkl')

