from . import views
from django.urls import path

# Urls
urlpatterns = [
    path('get/<str:type>/', views.getEntries, name='journal' ),
    
    path('new/<str:type>/', views.addEntry, name='newentry'),
    path('edit/<str:type>/<str:id>/', views.editEntry, name='editentry'),
    path('delete/<str:type>/<str:id>/', views.delEntry, name='delentry'),
    path('urgents/all/', views.getUrgent, name='urgent'),
];
