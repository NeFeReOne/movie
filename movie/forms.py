from sqlite3 import Time
from tabnanny import check
from time import time
from django import forms
from.models import Check, Data, History
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# 時間について（５問）
class TimeForm(forms.ModelForm):
    class Meta:
        model = Check
        fields = ['ch1', 'ch2', 'ch3', 'ch4', 'ch5']

# 気分について（９問）
class FeelForm(forms.ModelForm):
    class Meta:
        model = Check
        fields = ['ch6','ch7','ch8','ch9','ch10','ch11','ch12','ch13','ch14',  ]

# 趣味について（１６問）
class HobbyForm(forms.ModelForm):
    class Meta:
        model = Check
        fields = ['ch15','ch16','ch17','ch18','ch19','ch20',
        'ch21','ch22','ch23','ch24','ch25','ch26','ch27','ch28','ch29','ch30']

# 興味について（１７問）
class InterestForm(forms.ModelForm):
    class Meta:
        model = Check
        fields = ['ch31','ch32','ch33','ch34','ch35','ch36','ch37','ch38','ch39','ch40',
        'ch41','ch42','ch43','ch44','ch45','ch46','ch47']







# class GroupCheckForm(forms.Form):
#     def __init__(self, user, *args, **kwargs):
#         super(GroupCheckForm, self).__init__(*args, **kwargs)
#         time = Check.objects.filter(username='time').first()
#         self.fields['check'] = forms.MultipleChoiceField()
#             choices=[(item.title, item.title) for item in \
#                 Time.objects.filter(owner__in=[user,time])],
#             widget=forms.CheckboxSelectMultiple(),


    # graduation = forms.MultipleChoiceField(
    #     widget=CustomCheckboxSelectMultiple, required=False,
    #     choices=GRADUATION_CHOICES,



