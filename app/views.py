from django.shortcuts import render, redirect
from navbar.forms import ContactForm
from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib import messages
from document.models import Article, ArticleImage, ArticleCategory
from navbar.models import Contact

import datetime
import  subprocess
from app import bot

# Create your views here.
def index(request):
    objs = Article.objects.filter(category=1)
    return render(request, 'index.html', context={'articles' : objs})

class IndexView(View):
    def get(self, request):
        category_id = ArticleCategory.objects.get(name="Yangiliklar")
        articles = Article.objects.filter(category=category_id).order_by('-id')
        article = articles[0]

        articles = articles[0:4]

        context = {
                'articles':articles,
                'article':article,
                }
        return render(request, 'index.html', context)
        
        
class CategoryView(View):
    
    def get(self, request, id):
        # articles = get_object_or_404(Article, category = id)
        articles = Article.objects.filter(category = id).order_by('-id')
        article = ArticleCategory.objects.get(id=id)
        # print("=============================================", article)
        
        if str(article) == "Bog'lanish":
            form = ContactForm()
            return render(request, "contact.html", {'form':form})
        
        elif str(article) in ["Yangiliklar", "E'lonlar"]:
            # print("--------------------------------------", request)
            context = {
                '_id':id,
                'articles':articles,
                'article':article,
                }
            return render(request, 'article_list.html', context)
        
        
        elif str(article) in ["Qonunlar", "Qarorlar", "Farmonlar", "Standartlar", "Dasturlar", "Loyihalar"]:
            # print("--------------------------------------", request)
            context = {
                '_id':id,
                'articles':articles,
                'article':article,
                }
            return render(request, 'documents_list.html', context)
        

        else:
            if articles:
                context = {
                    '_id':id,
                    'article':articles[0],
                    }
                return render(request, 'one_page_detail.html', context)
            else:
                category_id = ArticleCategory.objects.get(name="Yangiliklar")
                articles = Article.objects.filter(category=category_id)
                article = Article.objects.filter(category=category_id)[len(articles)-1]

                articles = articles[0:4]

                context = {
                        'articles':articles,
                        'article':article,
                        }
                return render(request, 'index.html', context)
            
            
                
    def post(self, request, id):
        article = ArticleCategory.objects.get(id=id)
        if str(article) == "Bog'lanish":
            form = ContactForm(data=request.POST)
            if form.is_valid():
                data1 = form.save(request)
                # print("==========================================", request)
                
                messages.success(request,"Xabaringiz adminga yuborildi. Xabaringiz uchun rahmat.")
                # print("==========================================", request)
                
                # # data = request.data
                # print("==========================================", data1.id)
                data = Contact.objects.get(id=int(data1.id))
                print(data)
              
                today = datetime.date.today()
                formatted_date = today.strftime("%Y-%m-%d")
     
                text = f"""
        📝 Yangi xabar:\n
        🙍🏻‍♂️ Foydalanuvchi: {data.name}
        📲 Telefon: {data.phone}
        🧑🏻‍💻 Xabar: {data.body}
        📅 Sana: {formatted_date}
        """
                with open('app/data.txt', 'w') as file:
                    file.write(str(text))

                    
                try:
                    # tg_bot.run_bot()
                   
                    subprocess.run(['python', 'app/bot.py'])
                    
                except Exception as e:
                    print(f"============================ Error executing the script: {e}")

             
        
                return redirect("app:index")
            return render(request, "article_list.html", {"form":form})
        
        
    
    
    
class CategoryDetailView(View):
    def get(self, request,category_id, id):
        # articles = get_object_or_404(Article, category = id)
        article = Article.objects.get(id=id)
        articles = Article.objects.filter(category=category_id).order_by('-id')
        article.views += 1  # Ko'rishlar sonini 1 ga oshirish
        article.save()
      
        context = {
            'category_id':category_id,
            'article':article,
            'articles':articles[0:10],
            }
        # print("==========================++++++++==============",articles)
        # print("==========================++++++++==============",context)
        
        if str(article.category) in ["Qonunlar", "Qarorlar", "Farmonlar", "Standartlar", "Dasturlar", "Loyihalar"]:
            return render(request, 'one_page_detail.html', context)
        return render(request, 'article_detail.html', context)
    
    

# def article(request, name):
#     print("=============================================", name)
#     news = Article.objects.all()
    
#     context = {
#         'article' : news,
#     }
    
#     return render(request, 'article_list.html', context)
