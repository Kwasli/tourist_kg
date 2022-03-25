from turtle import width
from django import forms


#Есть 2 вида формы 
#1) ModelForm - Форма основанные на полях модели
#1) Form - Обычная форма


class LoginForm(forms.Form):
    username = forms.CharField()
    login = forms.CarField(widget = forms.PasswordInput)
