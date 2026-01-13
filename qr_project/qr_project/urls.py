"""
URL configuration for qr_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from qr_app.views import home, view_card
from django.shortcuts import render


urlpatterns = [
    path('admin/', admin.site.urls),
    path('card/<str:uid>/', view_card),
    path('', home, name='home'),
    path('scan-image/', lambda request: render(request, 'qr_app/image_scanner.html'), name='scan_image'),

]

