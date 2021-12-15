'''
    form.py
'''
from django.core.files.storage import default_storage
from django import forms

from calendarSite.models import Task
from calendarSite.models import Subject

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

class subject_manageForm(forms.Form):
    subject=()
    title=()
    data=()
    user=()
    chk=forms.CharField(
        widget=forms.CheckboxInput
    )

class taskForm(forms.Form):
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


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name','week','period']

class TaskForm(forms.ModelForm):
    subject_id = ()
    name = forms.CharField(
        max_length=200,
        required=True
    )
    author = ()
    contents = forms.CharField(
        max_length=200,
        required=True
    )
    end = forms.DateField(
        widget=forms.DateInput(attrs={"type":"date"}),
        input_formats=['%Y-%m-%d']
    )

