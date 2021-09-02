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
    title=()
    data=()
    user=()


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
    subject=()
    title=()
    data=()
    user=()

