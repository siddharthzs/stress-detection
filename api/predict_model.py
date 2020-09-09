import numpy as np
import pandas as pd
import multiprocessing 
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier


df = pd.read_csv('https://raw.githubusercontent.com/siddharthzs/stress_management/master/m14_merged.csv', index_col=0)
# df = pd.read_csv('data/m14_merged.csv')

feats =   ['BVP_mean', 'BVP_std', 'EDA_phasic_mean', 'EDA_phasic_min', 'EDA_smna_min', 
           'EDA_tonic_mean', 'Resp_mean', 'Resp_std', 'TEMP_mean', 'TEMP_std', 'TEMP_slope', 'BVP_peak_freq', 'age', 'height', 'weight', 'label']  

df2 = df[feats]
X = df2.drop('label', axis=1).values
y = df2['label'].values



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)  



decisionTree_model = tree.DecisionTreeClassifier()
decisionTree_model.fit(X_train,y_train)


randomForest_model = RandomForestClassifier(n_estimators=40)
randomForest_model.fit(X_train,y_train)


gradBoost_model = GradientBoostingClassifier(random_state=0) 
gradBoost_model.fit(X_train,y_train)


def decisionTree(arr):
    global decisionTree_model

    arr = np.array(arr)
    # file = open('templates/pickle_file/decisionTree_model.sav','rb')
    # model = pickle.load(file)
    # model = load('templates/pickle_file/decisionTree_model.pkl')
    result = decisionTree_model.predict(arr.reshape(1,-1)).flatten()
    prob = decisionTree_model.predict_proba(arr.reshape(1,-1)).flatten()
    return result, prob


def gradBoost(arr):
    global gradBoost_model
    arr = np.array(arr)
    # model = pickle.load(open('templates/pickle_file/gradBoost_model.sav','rb'))
    # model = load('templates/pickle_file/gradBoost_model.pkl')

    result = gradBoost_model.predict(arr.reshape(1,-1)).flatten()
    prob = gradBoost_model.predict_proba(arr.reshape(1,-1)).flatten()
    return result, prob



def randomForest(arr):
    global randomForest_model

    arr = np.array(arr)
    # model = pickle.load(open('templates/pickle_file/randomForest_model.sav','rb'))
    # model = load('templates/pickle_file/randomForest_model.pkl')

    result = randomForest_model.predict(arr.reshape(1,-1)).flatten()
    prob = randomForest_model.predict_proba(arr.reshape(1,-1)).flatten()
    return result, prob


def get_one_predict(id):

    data = np.genfromtxt('templates/pickle_file/testcase20.csv',delimiter=',')
    re1, prob1 = decisionTree(data[id])
    re2, prob2 = gradBoost(data[id])
    re3, prob3 = randomForest(data[id])

    return [[re1,prob1],[re2,prob2],[re3,prob3]]










# arr = [-0.1816732617297902, 107.648359232624, 1.8242890005698504, 0.3679770831591029, 5.229658028414467e-08, 1.2321641222809565, 
#     0.1481839773616847, 2.9356168122316832, 35.817090909090865, 0.012673914122067007, -0.00016905980208731805, 0.13566986998304126, 27.0,
#     175.0, 80.0]
# # arr = [54.55 for i in range(15)]
# print(decisionTree(arr))
# print(randomForest(arr))
# print(gradBoost(arr))
