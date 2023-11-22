from django.urls import path
from . import views


urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('comments/<int:article_pk>/list', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('comment_create/<int:article_pk>/', views.comment_create),
]
