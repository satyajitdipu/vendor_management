"""
URL configuration for vendor_management_system project.

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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.http import HttpResponse
from vendor_app.views import VendorViewSet, PurchaseOrderViewSet,VendorPerformanceViewSet
def home(request):
    return HttpResponse("Welcome to the Vendor Management System!")

router = DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r'purchase_orders', PurchaseOrderViewSet)
router.register(r'vendor_performance', VendorPerformanceViewSet, basename='vendor-performance')
urlpatterns = [
    path('api/', include(router.urls)),
    path('', home),
    path('api/vendors/<int:pk>/performance/', VendorPerformanceViewSet.as_view({'get': 'retrieve'}))
]
