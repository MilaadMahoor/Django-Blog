from django.shortcuts import render,redirect
from . import models,forms
from django.contrib.auth.decorators import login_required

# Create your views here.
def article_list(request):
    articles = models.Article.objects.all()
    args = {'articles': articles}
    return render(request,'articlelist.html',args)

def article_detail(request, title):
    article = models.Article.objects.get(title=title)
    args = {'article': article}
    return render(request,'single-page.html' , args)

@login_required(login_url = "/accounts/login")
def create_Article(request):
    if request.method =='POST':
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid:
            #save
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    args = {'form':form}
    return render(request,'create_Article.html',args)
