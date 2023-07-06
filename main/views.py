from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.contrib import messages
from django.shortcuts import redirect

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

from .form import AnalysisForm
from .models import tweets, twitterUser
from .serializers import tweetsSerializers
import pickle
import json
import pandas as pd
import numpy as np
import joblib

# Create your views here.

class analysisView(viewsets.ModelViewSet):
    queryset = tweets.objects.all()
    serializer_class = tweetsSerializers

def tweetsAnalysis(data):
    try:
        mdl = joblib.load("D:/School/FYP/Website/fypTest/main/SVMClassifier.pkl")
        y_pred = mdl.predict(data)
        result = pd.DataFrame(y_pred, columns = ['Category'])
        result = result.replace({0:'Hateful Message', 1:'Offensive Language', 2:'Neutral'})
        print(result)
        return (result.iloc[0]['Category'])
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    
def postRequest(request):
    if request.method == 'POST':
        form = AnalysisForm(request.POST)
        if form.is_valid():
            userName = form.cleaned_data['userName']
            tweet = form.cleaned_data['tweets']
            tf_idf_fit_only = pickle.load( open("D:/School/FYP/Website/fypTest/main/tfidf_pickle_fit", "rb"))
            #unit should be the tweet data
            matrix =tf_idf_fit_only.transform([tweet])
            # vectorising the new tweets
            df_vector = pd.DataFrame(matrix.todense(),columns = tf_idf_fit_only.get_feature_names_out() )
            result = tweetsAnalysis(df_vector)
            messages.success(request,'Application Status: {}'.format(result))

    form = AnalysisForm()
    return render(request, 'myform/form.html', {'form':form})

def table(response):
    t = tweets.objects.all()
    tu = twitterUser.objects.all()
    return render(response, "myform/tweetTable.html", {"t":t, "tu":tu})

def tweetRetrieval(response):
    t = tweets.objects.all()
    return render(response, "myform/tweetRetrieval.html", {"t":t})

def twitterUserRetrieval(response):
    t = twitterUser.objects.all()
    return render(response, "myform/twitterUserRetrieval.html", {"t":t})

def home(response):
    return render(response,"myform/home.html")
        