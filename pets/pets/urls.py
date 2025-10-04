"""
URL configuration for pets project.

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
from pets_app.views import PetView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pets/', PetView.as_view()),  # POST
    path('pets/<str:pet_id>/', PetView.as_view()),  # GET por id, PUT
    path('pets/document/<str:documento>/', PetView.as_view()),  # GET por documento (path param)
]
