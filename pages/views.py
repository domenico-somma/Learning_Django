from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm, ListForm
import seaborn as sns
import pandas as pd
from .models import lineplot

def homePageView(request):
#    return HttpResponse('Hello, World!')
    return render(request, "home.html")

def aboutPageView(request):
    return render(request, "about.html")

def insert_name(request):
    form_in_view = NameForm()
    return render(request, 'insert_name_hello.html', {'form_in_html': form_in_view})

def helloPageView(request):
    data = NameForm(request.POST)
    if data.is_valid():
        text = data.cleaned_data['your_name']
    args= {'data': data, 'text': text}
    return render(request, "hello.html", args)

def insert_name_plot(request):
    #To move in model?
    import os
    try:
        os.remove("pages/static/pages/plot.png")
    except FileNotFoundError:
        pass
    listform_in_view = ListForm()
    return render(request, 'insert_name_plot.html', {'form_in_html': listform_in_view})

def plotView(request):
    #To move in model?
    df=pd.read_csv("pages/static/pages/BMDM/BMDM.csv",sep=",",index_col=0)

    data = NameForm(request.POST)
    if data.is_valid():
        text = data.cleaned_data['your_name']

    g=lineplot(df,text)
    try:
        g.savefig("pages/static/pages/plot.png")
        return render(request, 'plot.html')
    except AttributeError:
        return render(request, 'plot.html', {"text":"Gene not found"})
    # try canvas?
