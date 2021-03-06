from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('articles/<int:a_id>', views.view_article, name="articles"),
    path('author', views.author, name="author"),
    path('signin', views.login, name="login"),
    path('articles/edit/<int:id>', views.edit_article, name="edit_article"),
    path('articles/delete/<int:id>', views.delete_article, name="delete_article"),
    path('articles/create', views.create_article, name="create_article"),
    path('cookies', views.cookies, name="cookies"),
    path('get_cookies', views.get_cookies, name="get_cookies"),
    path('set_session', views.set_session, name="set_session"),
    path('get_session', views.get_session, name="get_session"),
    path('login', views.usr_login, name="usr_login"),  # backends function
    path('logout', views.usr_logout, name="usr_logout"),  # backends function
    path('chat', views.course_chat_room, name="chat"),
]
