"""messageClone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from messageApp import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Index.as_view(),name='index'),
    path('register/',views.register,name='register'),
    path('login/',LoginView.as_view(template_name='messageApp/login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('listUser/',views.UserList.as_view(),name='list_user'),
    path('user/inbox/<int:pk>/',views.listMessages,name='list_message'),  ##Filter user by username
    path('user/create_message/',views.CreateMessage.as_view(),name='create_message'), ##Creating message
    path('user/sent_items/',views.SentItems.as_view(),name='sent_items'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
