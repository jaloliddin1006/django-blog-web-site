from django.shortcuts import render, redirect
from .models import Article
from .myforms import *
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')


def home(request):
    articles = Article.objects.filter(is_active = True)
    return render(request, 'home.html', {'articles': articles})

def article_detail(request, id):
    article = Article.objects.get(id=id)
    articles = Article.objects.filter(is_active = True)
    return render(request, 'detail.html', {'article':article, 'articles':articles})
    
    
def article_create(request):
    user = request.user
    if user.is_authenticated:
        form = ArticleForm()
        if request.method == "POST":
            form = ArticleForm(data = request.POST)
            if form.is_valid():
                articles = form.save(commit=False)
                articles.author = user
                articles = form.save(commit=True)
                return redirect('index')
            
            else:return render(request, 'create.html', {'form':form})    
        else:return render(request, 'create.html', {'form':form})    
    else:return HttpResponse("Not allowed")
    