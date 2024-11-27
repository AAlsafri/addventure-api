"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RegisterUser,
    LoginUser,
    DestinationList,
    DestinationDetail,
    ContinentViewSet,
)

router = DefaultRouter()
router.register(r'continents', ContinentViewSet, basename='continent')

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('destinations/', DestinationList.as_view(), name='destination-list'),
    path('destinations/<int:pk>/', DestinationDetail.as_view(), name='destination-detail'),
    path('', include(router.urls)),  
]