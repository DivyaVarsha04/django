"""
URL configuration for demo4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('signup/',views.signup),
    path('login/',views.login, name='login'),
    # path('days/',views.days),
    # path('days/monday',views.monday),
    # path('days/tuesday',views.tuesday),
    # path('days/wednesday',views.wednesday),
    # path('days/thursday',views.thursday),
    # path('days/friday',views.friday),
    # path('days/saturday',views.saturday),
    # path('days/sunday',views.sunday),
    path('days/<day>/',views.days),
    path('months/<month>/',views.months),
    path('day/<wee>/',views.weeks),
    path('',views.mainpg),
    path('sinfo/<name>/',views.sinfo,name='sinfo'),
    path('i_s/<rollno>',views.i_s,name='i_s'),
    path('home/',views.home),
    path('student/',views.student),
    path('main/',views.main),
    path('main/<days>/',views.days),
    path('main_mon/',views.main_month),
    path('main_mon/<month>/',views.months),
    path('stu/',views.stu), 
    
    
   
]