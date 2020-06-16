from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import AuthToken
from . import predict_model
# ['BVP_mean', 'BVP_std', 'EDA_phasic_mean', 'EDA_phasic_min',
#        'EDA_smna_min', 'EDA_tonic_mean', 'Resp_mean', 'Resp_std', 'TEMP_mean',
#        'TEMP_std', 'TEMP_slope', 'BVP_peak_freq', 'age', 'height', 'weight']





@api_view(['POST'])
def apiModel(request,token):
    try:
        user = AuthToken.objects.get(token=token)
    except:
        return Response('You are not Authorized, Authentication Error!!')


    data = request.data
    arr = []
    try:
        arr.append(data['BVP_mean'])
        arr.append(data['BVP_std'])
        arr.append(data['EDA_phasic_mean'])
        arr.append(data['EDA_phasic_min'])
        arr.append(data['EDA_smna_min'])
        arr.append(data['EDA_tonic_mean'])
        arr.append(data['Resp_mean'])
        arr.append(data['Resp_std'])
        arr.append(data['TEMP_mean'])
        arr.append(data['TEMP_std'])
        arr.append(data['TEMP_slope'])
        arr.append(data['BVP_peak_freq'])
        arr.append(data['age'])
        arr.append(data['height'])
        arr.append(data['weight'])

    except:
        return Response("Invalid Data!!")


    # try:
    all_result1 = predict_model.decisionTree(arr)
    all_result2 = predict_model.randomForest(arr)
    all_result3 = predict_model.gradBoost(arr)
    
    for i in range(3):
        all_result1[1][i] = round(all_result1[1][i],4)
        all_result2[1][i] = round(all_result2[1][i],4)
        all_result3[1][i] = round(all_result3[1][i],4)
    # except:
    #     return Response("something went wrong!!")

    re = {0 : 'amusement', 1: 'baseline', 2: 'stress'}
    re = re[all_result2[0][0]]

    d = {
        "decisionTree" : {"result" : {re : all_result1[0]}, "probability" :{"amusement" : all_result1[1][0], "baseline" : all_result1[1][1], "stress" : all_result1[1][2]}},
        "gradBoost" : {"result" : {re : all_result2[0]}, "probability" :{"amusement" : all_result2[1][0], "baseline" : all_result2[1][1], "stress" : all_result2[1][2]} },
        "randomForest" : {"result" : {re : all_result3[0]}, "probability" :{"amusement" : all_result3[1][0], "baseline" : all_result3[1][1], "stress" : all_result3[1][2]} }
    }

    return Response(d)




@api_view(['GET'])
def graphModel(request,id,token):
    try:
        user = AuthToken.objects.get(token=token)
    except:
        return Response('You are not Authorized, Authentication Error!!')
    try:
        all_result = predict_model.get_one_predict(id) 
    except:
        return Response('something went wrong!!') 

    d = {
        "decisionTree" : { "result" : all_result[0][0], "probability" : all_result[0][1] },
        "gradBoost" : { "result" : all_result[1][0], "probability" : all_result[1][1] },
        "randomForest" : { "result" : all_result[2][0], "probability" : all_result[2][1] }
    }
    return Response(d)