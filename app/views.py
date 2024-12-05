from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from app.forms import AnketaForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.db import models
from .models import Blog

from .models import Comment 
from .forms import CommentForm
from .forms import BlogForm


 

def home(request): 
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'О-Псков',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Страеница с нашими контактами.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest) 
    return render(
        request,
        'app/about.html',
        {
            'title':'О нас',
            'message':'Сведения о нас',
            'year':datetime.now().year,
        }
    )

def links(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/links.html',
        {
            'title':'',
            'message':' Дополнительные ссылки:',
            'year':datetime.now().year,
        }
    )

def anketa(request):
    assert isinstance(request, HttpRequest)
    data = None
    gender={'1':'Женщина','2':'Мужчина'}
    internet={'1':'Каждый день','2':' Через день ',
              '3':' Один раз в неделю','4':' Один раз в месяц',
              '5':' Не бегаю'}
    if request.method =='POST':
        form = AnketaForm(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['city'] = form.cleaned_data['city']
            data['job'] = form.cleaned_data['job']
            data['gender'] =gender[form.cleaned_data['gender']]
            data['internet'] = internet[form.cleaned_data['internet']]
            if(form.cleaned_data['notice'] == True):
                data['notice']='Да'
            else:
                data['notice']='Нет' 
            data['email'] = form.cleaned_data['email']
            data['message'] = form.cleaned_data['message']
            form = None
    else:
         form = AnketaForm()
    return render(
         request,
          'app/anketa.html',
          {
              'form':form,
              'data':data,
          }
    
    )  

def registration(request):

    assert isinstance(request, HttpRequest)

    if request.method == "POST": # после отправки формы

      regform = UserCreationForm (request.POST)

      if regform.is_valid(): #валидация полей формы

       reg_f = regform.save(commit=False) # не сохраняем автоматически данные формы

       reg_f.is_staff = False # запрещен вход в административный раздел

       reg_f.is_active = True # активный пользователь

       reg_f.is_superuser = False # не является суперпользователем

       reg_f.date_joined = datetime.now() # дата регистрации

       reg_f.last_login = datetime.now() # дата последней авторизации

       reg_f.save() # сохраняем изменения после добавления данных

       return redirect('home') # переадресация на главную страницу после регистрации

    else:

       regform = UserCreationForm() # создание объекта формы для ввода данных нового пользователя

    return render(
         request,
          'app/registration.html',
          {
             'regform': regform, # передача формы в шаблон веб-страницы
             'year':datetime.now().year,
          }
    
    )  
def blog(request):
   posts = Blog.objects.all() 
   assert isinstance(request, HttpRequest)
   return render(
         request,
          'app/blog.html',
          {
            'title':'Блог',

            'posts': posts, # передача списка статей в шаблон веб-страницы

            'year':datetime.now().year,
          }
    
    )  
def blogpost(request, parametr):

    assert isinstance(request, HttpRequest)

    post_1 = Blog.objects.get(id=parametr) # запрос на выбор конкретной статьи по параметру
    
    comments = Comment.objects.filter(post=parametr)
    
    if request.method == "POST":

      form = CommentForm(request.POST)

      if form.is_valid():

        comment_f = form.save(commit=False)

        comment_f.author = request.user # добавляем (так как этого поля нет в форме) в модель Комментария (Comment) в поле автор авторизованного пользователя

        comment_f.date = datetime.now() # добавляем в модель Комментария (Comment) текущую дату

        comment_f.post = Blog.objects.get(id=parametr) # добавляем в модель Комментария (Comment) статью, для которой данный комментарий

        comment_f.save() # сохраняем изменения после добавления полей
        
        return redirect('blogpost', parametr=post_1.id) # переадресация на ту же страницу статьи после отправки комментария

    else:

      form = CommentForm() # создание формы для ввода комментария 
    
    return render(

            request,

              'app/blogpost.html',

               {

                'post_1': post_1, # передача конкретной статьи в шаблон веб-страницы

                'comments': comments, # передача всех комментариев к данной статье в шаблон веб-страницы

                'form': form, # передача формы добавления комментария в шаблон веб-страницы
                
                'year':datetime.now().year,
                
                

               }

    )

def newpost(request):

    assert isinstance(request, HttpRequest)

    if request.method == "POST":
       
       blogform = BlogForm(request.POST, request.FILES)
        
       if blogform.is_valid():
          blog_f=blogform.save( commit=False)
          blog_f.posted=datetime.now()
          blog_f.author=request.user
          blog_f.save()
          return redirect('blog')
    else:
      
      blogform = BlogForm()
      
      return render(

            request,

              'app/newpost.html',

               {
                'blogform':blogform,
                
                'title':'Добавить статью блога',
                
                'year':datetime.now().year,           
               }

      )
    
def vidiopost(request): 
    assert isinstance(request, HttpRequest) 
    return render(
        request,
        'app/vidiopost.html',
        {
            'title':'Наши видео',
            'message':'Сведения о наших видео',
            'year':datetime.now().year,
        }
    )

def calendar(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest) 
    return render(
        request,
        'app/calendar.html',
        {
            'title':'Календарь',
            
        }
    )







   
    
  
                             
                          
