from django.shortcuts import render
from navbar.forms import ContactForm
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
        article = ArticleCategory.objects.get(id=id)
        print("=============================================", article)
        
        if str(article) == "Bog'lanish":
            form = ContactForm()
            return render(request, "contact.html", {'form':form})
          
        else:
            print("--------------------------------------", request)
            context = {
                '_id':id,
                'articles':articles,
                }
            return render(request, 'article_list.html', context)
    
    
    
class CategoryDetailView(View):
    def get(self, request,category_id, id):
        # articles = get_object_or_404(Article, category = id)
        article = Article.objects.get(id=id)
        articles = Article.objects.filter(category=category_id)
      
        context = {
            '_id':category_id,
            'article':article,
            'articles':articles,
            }
        
        return render(request, 'article_detail.html', context)
    
    

# def article(request, name):
#     print("=============================================", name)
#     news = Article.objects.all()
    
#     context = {
#         'article' : news,
#     }
    
#     return render(request, 'article_list.html', context)
