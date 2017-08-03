from django.shortcuts import render
from .models import Post
from django.utils import timezone

'''
a nézetek összekötik a modelleket a sablonokkal
itt döntjük el h miket akarunk megjeleníteni
'''

def post_list(request):
    #azok a postok amik publikálva vannak és published_date szerint vannak sorba rendezve
    posts_queryset = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts_queryset': posts_queryset})

