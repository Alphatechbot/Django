from django.urls import path
from . import views

urlpatterns = [
    path('',views.webpage_one,name='webpage_one'),
    path('page1/', views.webpage_one),
    path('page2', views.webpage_two, name='webpage_two'),
    path('page3', views.webpage_three, name='webpage_three')
]