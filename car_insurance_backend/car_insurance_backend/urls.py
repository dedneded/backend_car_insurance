"""
URL configuration for car_insurance_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path

from car_insurance.views import *

urlpatterns = [

    path('clients/create_client/', create_client, name='create_client'),
    path('clients/update_client/<int:pk>/', update_client, name='update_client'),
    path('clients/get_client/<int:pk>/', get_client, name='get_client'),
    path('employees/create_employee/', create_employee, name='create_employee'),
    path('employees/update_employee/<int:pk>/', update_employee, name='update_employee'),
    path('employees/get_employee/<int:pk>/', get_employee, name='get_employee'),
    path('employees/delete_employee/<int:pk>/', delete_employee, name='delete_employee'),
    #path('clients/', create_client, name='create_client'),
    path('clients/<int:pk>/', update_client),
    path('clients/<int:pk>/delete/', delete_client)
]
