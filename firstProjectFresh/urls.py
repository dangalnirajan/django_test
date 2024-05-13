"""
URL configuration for firstProjectFresh project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import logout
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path


from home.views import *
from vege.views import *

urlpatterns = [

    path('',details, name='details'),
    path('contact/',contact, name='contact'),
    path('recipes/',recipes, name='recipes'),
    path('about/',about, name='about'),
    path('admin/', admin.site.urls),
    path('details/',details, name='details'),
    path('delete-recipe/<id>/',delete_recipe, name='delete-recipe'),
    path('update-recipe/<id>/',update_recipe, name='update-recipe'),
    # path('register/', register, name='register'),
    # path('login/', login , name='login'),
    # path('logout/', logout, name='logout'),
    #

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()