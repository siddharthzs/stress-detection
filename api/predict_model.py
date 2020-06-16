import numpy as np
from joblib import load


def decisionTree(arr):

    arr = np.array(arr)
    # file = open('templates/pickle_file/decisionTree_model.sav','rb')
    # model = pickle.load(file)
    model = load('templates/pickle_file/decisionTree_model.pkl')
    result = model.predict(arr.reshape(1,-1)).flatten()
    prob = model.predict_proba(arr.reshape(1,-1)).flatten()
    return result, prob


def gradBoost(arr):

    arr = np.array(arr)
    # model = pickle.load(open('templates/pickle_file/gradBoost_model.sav','rb'))
    model = load('templates/pickle_file/gradBoost_model.pkl')

    result = model.predict(arr.reshape(1,-1)).flatten()
    prob = model.predict_proba(arr.reshape(1,-1)).flatten()
    return result, prob



def randomForest(arr):

    arr = np.array(arr)
    # model = pickle.load(open('templates/pickle_file/randomForest_model.sav','rb'))
    model = load('templates/pickle_file/randomForest_model.pkl')

    result = model.predict(arr.reshape(1,-1)).flatten()
    prob = model.predict_proba(arr.reshape(1,-1)).flatten()
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
