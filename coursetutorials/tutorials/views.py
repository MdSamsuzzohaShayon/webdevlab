from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, "tutorials/index.html")
    # return HttpResponse("Hello")


def about(request):
    return render(request, "tutorials/about.html")


def contact(request):
    return render(request, "tutorials/contact.html")


def tutorial_series(request):
    tutorials = ({
            "num": 1,
            "title": "Title one",
            "desc": "This is desc one [Text editor text]",
            "video_url": "https://www.youtube.com/watch?v=LzVzen_L2c8"
        },
        {
            "num": 3,
            "title": "Title three",
            "desc": "This is desc three [Text editor text]",
            "video_url": "https://www.youtube.com/watch?v=-6qNFvLUS9s"
        },
        {
            "num": 2,
            "title": "Title two",
            "desc": "This is desc two [Text editor text]",
            "video_url": "https://www.youtube.com/watch?v=QjoWsrzP-SI"
        },
    )

    serilize_tutorials = sorted(tutorials, key=lambda x: x['num'])

    context = {
        "tutorials": serilize_tutorials
    }
    return render(request, "tutorials/series-tutorials.html", context)


def individual_tutorial(request):
    return render(request, 'tutorials/individual-tutorial.html')
