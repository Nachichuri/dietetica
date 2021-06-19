from django.urls import path
from .views import CategoriesListView, ProductsListView, ProductDetail
from . import views

urlpatterns = [
    path('', views.home, name='main-home'),
    path('despensa/', CategoriesListView.as_view(), name='main-categories'),
    path('despensa/<pk>/', ProductsListView.as_view(), name='main-products'),
    path('despensa/<category>/<pk>/', ProductDetail.as_view(), name='main-product-detail')
]