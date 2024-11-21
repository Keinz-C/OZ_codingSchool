from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def create(request):
    if request.method == 'POST':
        article = Article()
        article.title = request.POST['title']
        article.content = request.POST['content']
        article.save()

    else:
        return render(request, 'articles/create.html')