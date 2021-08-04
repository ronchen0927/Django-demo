from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from .models import _get_articles, _create_articles, _get_articles_by_id, _del_articles_by_id, _edit_articles_by_id
from .create_articles import create_articles_form, edit_articles_form
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


# chat
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required


# chat
@login_required
def course_chat_room(request):
    return render(request, 'chat/room.html')


def set_session(request):
    request.session['pref'] = "C++"
    response = HttpResponse("Session set!")
    return response


def get_session(request):
    response = HttpResponse("Session set!"+str(request.session['pref']))
    return response


def get_cookies(request):
    if "pref" in request.COOKIES:
        print("pref:", request.COOKIES['pref'])


def cookies(request):
    response = HttpResponse("Cookie set!")
    response.set_cookie("pref", "PYTHON")
    return response


def index(request):
    articles = _get_articles()
    content = {"articles": articles}
    return render(request, 'index.html', content)


def create_article(request):
    if request.method == 'POST':
        _create_articles(request)
        return redirect("index")
    else:
        form = create_articles_form()
        context = {"form": form, "user": ""}
        return render(request, "create_articles.html", context)


def edit_article(request, id):
    if request.method == 'POST':
        _edit_articles_by_id(request, id)
        return redirect("index")
    else:
        form = edit_articles_form(id)
        context = {"form": form, "id": id}
        return render(request, "edit_articles.html", context)


def delete_article(request, id):
    _del_articles_by_id(id)
    return redirect("index")


def author(request):
    context = {
        "name": "RonChen",
        "sidebar": ["Home", "Articles", "Authors"],
        "articles": articles
    }
    return render(request, "author.html", context)


def login(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    return redirect("index")


def usr_login(request):
    user = authenticate(
        request, username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        auth_login(request, user)
        return redirect('index')
    else:
        return redirect('usr_login')


def usr_logout(request):
    auth_logout(request)
    return redirect('index')


def view_article(request, a_id):
    context = {"article": _get_articles_by_id(a_id)}
    return render(request, "show_articles.html", context)
