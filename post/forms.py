from pyexpat import model
from post.models import Comment, Contact
from django import forms


#Есть 2 вида формы 
#1) ModelForm - Форма основанные на полях модели
#1) Form - Обычная форма


class CommentForm(forms.Form):
    class Meta:
        model = Comment
        fields = ['comment']

        widgets = {
            'comment':forms.TextInput(attrs ={
                'class':"form-control"
            })
        }



class ContactForm(forms.Form):
    class Meta:
        model = Contact
        fields = ['nomer']
