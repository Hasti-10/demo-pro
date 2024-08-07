"""
URL configuration for djpro project.

The `urlpatterns` list routes URLs to vews. For more information please see:
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
from django.urls import path,include
from djapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product',views.pro.as_view()),
    path('prodetail/<int:pk>', views.pro_d.as_view()),
    path('cust',views.cust.as_view()),
    path('review', views.review.as_view()),
    path('rev/<int:pk>', views.rev.as_view()),
    path('revlist', views.revlist.as_view()),
    #path('rev',views.Reviewgeneric.as_view()),
   # path('mixin/<int:pk>', views.mixin.as_view()),

]
