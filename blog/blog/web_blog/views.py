from django.shortcuts import render

posts = [
    {
        'author': 'Antonio',
        'title': "Antonio's blog",
        'content': 'First content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Ivan',
        'title': "Ivan's blog",
        'content': 'Second content',
        'date_posted': 'September 27, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'web_blog/home.html', context)


def about(request):
    return render(request, 'web_blog/about.html', {'title': 'About'})
