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
    return render(request, 'index.html')


class CategoryView(View):
    def get(self, request, id):
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
        
        
    def post(self, request, id):
        article = ArticleCategory.objects.get(id=id)
        if str(article) == "Bog'lanish":
            form = ContactForm(data=request.POST)
            if form.is_valid():
                data1 = form.save(request)
                
                messages.success(request,"Xabaringiz adminga yuborildi. XAbaringiz uchun rahmat.")
                print("==========================================", request)
                
                # # data = request.data
                print("==========================================", data1.name)
                data = Contact.objects.get(name=data1.name)
               
              
                today = datetime.date.today()
                formatted_date = today.strftime("%Y-%m-%d")
     
                text = f"""
        📝 Yangi xabar:\n
        🙍🏻‍♂️ Foydalanuvchi: {data.name}
        📲 Telefon: {data.phone}
        🧑🏻‍💻 Xabar: {data.body}
        📅 Sana: {formatted_date}
        """
                with open('api/data.txt', 'w') as file:
                    file.write(str(text))

                    
                try:
                    # tg_bot.run_bot()
                    subprocess.run(['python', 'app/bot.py'])
                except Exception as e:
                    print(f"============================ Error executing the script: {e}")

                print(" ========================== contact create view  another_function ================================")
        
                return redirect("app:index")
            return render(request, "article_list.html", {"form":form})
        
        
    
    
    
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
