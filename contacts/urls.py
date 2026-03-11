from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('list/', views.contact_list, name='contact_list'),
    path('add/', views.contact_add, name='contact_add'),
    path('export/', views.export_csv, name='export_csv'),
    path('signup/', views.signup, name='signup'),
    path('contact/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('contact/<int:pk>/edit/', views.contact_edit, name='contact_edit'),
    path('contact/<int:pk>/delete/', views.contact_delete, name='contact_delete'),
]