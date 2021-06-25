from django.urls import path
from .views import CategoriesListView, ProductsListView, ProductDetail
from . import views

urlpatterns = [
    path('', views.home, name='main-home'),
    path('despensa/', CategoriesListView.as_view(), name='main-categories'),
    path('despensa/<slug:pk>/', ProductsListView.as_view(), name='main-products'),
    path('despensa/<slug:category>/<slug:pk>/', ProductDetail.as_view(), name='main-product-detail')
]