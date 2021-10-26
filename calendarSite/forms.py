'''
    form.py
'''
from django.core.files.storage import default_storage
from django import forms

from calendarSite.models import Friend

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



class searchForm(forms.Form):
    subject = forms.ChoiceField()
    user=forms.CharField(
        max_length=200,
        required=True
    )

    

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

class testForm(forms.Form):
    name = forms.CharField(label='Name')
    mail = forms.EmailField(label='Email')
    gender = forms.BooleanField(label = 'Gender',required=False)
    age = forms.IntegerField(label='Age')
    birthday = forms.DateField(label='Birth')

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name','mail','gender','age','birthday']