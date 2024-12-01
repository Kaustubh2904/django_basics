"""
URL configuration for chaiaurDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings #this is for the images to be shown on the page
from django.conf.urls.static import static #this is for the images to be shown on the page
from .  import views

urlpatterns = [
    path('admin/', admin.site.urls), #yha sae admin khul raha hai bhaisaab 
    path('', views.home, name="home"), # This is the default page called home but if i have a diff landong page i can change it to that and a diff home page then i would add a new path where ther would be 'home/' and the view would be 'home/
    path('superman/', views.superman, name="superman"),
    path('ganja/', views.ganja, name="ganja"),
    path('chai/', include('chai.urls')),

    path("__reload__/", include("django_browser_reload.urls")), #this is a heavy path like it takes time so keep it always at the last and its for pre prod not for prod 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #this is for the images to be shown on the page
