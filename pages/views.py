from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm

def homePageView(request):
#    return HttpResponse('Hello, World!')
    return render(request, "home.html")

def aboutPageView(request):
    return render(request, "about.html")

def helloPageView(request):
#    if request.method == 'POST':
    data = NameForm(request.POST)
    if data.is_valid():
        text = data.cleaned_data['your_name']
    args= {'data': data, 'text': text}
    return render(request, "hello.html", args)

def get_name(request):
    form_in_view = NameForm()
    return render(request, 'insert_name.html', {'form_in_html': form_in_view})

#def get_name(request):
#    form_in_view = NameForm()
#    if request.method == 'POST':
#        form_in_view = NameForm(request.POST)
#        if form_in_view.is_valid():
#    return render(request, 'insert_name.html', {'form_in_html': form_in_view})

