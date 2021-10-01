from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from blog.models import Blog, Contact
import math


# Create your views here.
def home(request):
    return render(request, 'index.html')

def bloghome(request):
    no_of_posts = 4
    #if request.GET['pageno']
    page = request.GET.get('page')
    if page is None:
        page=1
    else:
        page = int(page)
    #print(page)
    '''''
    1  : 0  - 3
    2  : 3  - 6
    3  : 6  - 9

    1 :0 - 0+ no_of_posts
    2 :no_of_posts to no_of_posts + no_of_posts
    3 :no_of_posts + no_of_posts to no_of_posts + no_of_posts + no_of_posts

    (page-no-1) to page-no* no-of-posts
    '''
    #print(request.GET.get('pageno'))
    blogs = Blog.objects.all()
    length =len(blogs) 
    print(length)
    blogs=blogs[(page-1)*no_of_posts: page*no_of_posts]
    if page >1:
        prev = page -1 
    else:
        prev = None

        '''ceil used to show num of pages ex: math.ceil(4.5)=5,
        math.ceil(5.56)=6'''

    if page <math.ceil(length/no_of_posts):
        nxt=page + 1
    else:
        nxt = None
    print(prev,nxt)

   # prev = page - 1
   # nxt= page + 1
    context ={'blogs':blogs, 'prev':prev, 'nxt':nxt}
    return render(request, 'bloghome.html' ,context)

def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first()
    context ={'blog':blog}

    return render(request, 'blogpost.html',context)

def contact(request):
    if request.method =='POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        instance = Contact(name=name, email=email, phone=phone, desc=desc)
        instance.save()

    return render(request, 'contact.html')

def search(request):
    return render(request, 'search.html')