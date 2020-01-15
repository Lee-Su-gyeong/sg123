"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
#blog.urls를 가져오려면, include 함수가 필요

urlpatterns = [
    path('admin/', admin.site.urls), #admin/로 시작하는 모든 URL을 view와 대조해 찾아냄.python3 -m venv myvenv
    path('', include('blog.urls')),
    #mysite/urls.py파일로 url들을 가져올 거에요.
]
