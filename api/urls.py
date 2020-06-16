from django.urls import path
from .views import apiModel, graphModel


urlpatterns = [

    path('model/<str:token>/', apiModel, name='web-model-api'),
    path('model/<int:id>/predict/<str:token>/',graphModel, name='web-model-predict'),
    
]