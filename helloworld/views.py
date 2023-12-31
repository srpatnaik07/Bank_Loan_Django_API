from django.shortcuts import render
# from .forms import MyForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Approvals
from .serializers import approvalsSerializers
import joblib
import json
import numpy as np
import pandas as pd
import pickle

class ApprovalsView(viewsets.ModelViewSet):
    queryset = Approvals.objects.all()
    serializer_class = approvalsSerializers

@api_view(["POST"])
def approvereject(request):
    try:
        mdl = pickle.load(open("C:/Users/sohan/Desktop/new-django/hello/helloworld/loan_model.pkl", "rb"))
        print(mdl)
        mydata = request.data
        unit = np.array(list(mydata.values()))
        unit = unit.reshape(1, -1)
        scalers = joblib.load("C:/Users/sohan/Desktop/new-django/hello/helloworld/scalers.pkl")
        X = scalers.transform(unit)
        y_pred = mdl.predict(X)
        y_pred = (y_pred > 0.58)
        newdf = pd.DataFrame(y_pred, columns=['Status'])
        print(newdf)
        newdf = newdf.replace({True: 'Approved', False: 'Rejected'})
        return JsonResponse('Your Status is {}'.format(newdf), safe=False)
    except ValueError as e:
        return Response(e.args[0], status=status.HTTP_400_BAD_REQUEST)
