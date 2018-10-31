from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class ListForm(forms.Form):
    your_name = forms.CharField(label='Insert gene name', max_length=100)#widget=forms.Textarea)
