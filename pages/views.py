from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    print(*args, **kwargs)
    print(request)
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        'title': 'this is my text',
        'this_is_true': True,
        'my_number': '2288',
        'my_list': [123, 454, 4564, "batu"],
        'my_html': "<h1>Html Safe Komutu</h1>"
    }
    """for item in [12, 34, 56, 78, 90]:
        my_context['item1'] = item"""
    return render(request, "about.html", my_context)


def social_view(request, *args, **kwargs):
    return render(request, "social.html", {})
    # return HttpResponse("<h1>Social Page</>")
