from django.shortcuts import render

from django.views import View
from django.shortcuts import get_object_or_404
from document.models import Article, ArticleImage, ArticleCategory

# Create your views here.
def index(request):
    return render(request, 'index.html')


class CategoryView(View):
    def get(self, request, id):
        print("=============================================", id)
        # articles = get_object_or_404(Article, category = id)
        articles = Article.objects.filter(category=id)
        print("=============================================", articles)
        
        return render(request, 'article_list.html', {'articles':articles})
    
    
    

def article(request, name):
    print("=============================================", name)
    news = Article.objects.all()
    
    context = {
        'article' : news,
    }
    
    return render(request, 'article_list.html', context)
