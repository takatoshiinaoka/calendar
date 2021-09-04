'''
    form.py
'''
from django.core.files.storage import default_storage
from django import forms

class addDataForm(forms.Form):
    subject= forms.CharField(
        max_length=200,
        required=True
    )
    title=forms.CharField(
        max_length=200,
        required=True
    )
    date= forms.DateField(
        widget=forms.DateInput(attrs={"type":"date"}),
        input_formats=['%Y-%m-%d']
    )
    user=forms.CharField(
        max_length=200,
        required=True
    )


class indexForm(forms.Form):
    subject=()
    title=()
    data=()
    user=()



#class searchForm(forms.Form):
#    subject = forms.ChoiceField()

    

class subjectForm(forms.Form):
    subject=()
    title=()
    data=()
    user=()



class userForm(forms.Form):
    subject= forms.CharField(
        max_length=200,
        required=True
    )
    user=forms.CharField(
        max_length=200,
        required=True
    )

