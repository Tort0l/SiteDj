

from dataclasses import fields
from email import message
from random import choices
from django import forms
from django.db import models
from .models import Comment
from .models import Blog

from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _



class AnketaForm(forms.Form):
    name = forms.CharField(label = 'Ваше имя',min_length=2, max_length=100)
    city = forms.CharField(label = 'Ваш город',min_length=2, max_length=100)
    job = forms.CharField(label = 'Ваш род занятий',min_length=2, max_length=100)
    gender = forms.ChoiceField(label='Ваш пол',
                             choices=[('1','Женский'),('2','Мужской')],
                             widget=forms.RadioSelect, initial=1)
    internet = forms.ChoiceField(label='Как часто вы бегаете?',
                               choices= (('1',''),
                               ('2',' Через день '),
                               ('3',' Один раз в неделю'),
                               ('4',' Один раз в месяц'),
                               ('5',' Не бегаю')), initial=1)
    notice = forms.BooleanField(label='Получать новости с сайта на e-mail?',
                               required=False)
    email=forms.EmailField(label=' Ваш email',min_length=7)
    message=forms.CharField(label='Рсскажите о себе',
                            widget=forms.Textarea(attrs={'rows':12, 'cols':20}))
                                     

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
    
class CommentForm(forms.ModelForm):

  class Meta:

   model = Comment # используемая модель

   fields = ('text',) # требуется заполнить только поле text

   labels = {'text': "Комментарий"} # метка к полю формы text


class BlogForm(forms.ModelForm):
      class Meta:
         model = Blog
         fields = ( 'title', 'description', 'content', 'image',)
         labels = { 'title' : "Заголовок", 'description' : "Краткое содержание", 'content' : "Полное содержание ", 'image': " Картинка" }
         