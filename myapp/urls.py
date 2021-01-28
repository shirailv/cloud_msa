from django.urls import path
from . import views
from myapp.views import post_detail, post_add, post_delete

urlpatterns = [
    path('',views.index, name='index'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/add/', post_add, name='post_add'),
    path('post/<int:pk>/delete/', post_delete, name='post_delete')
]