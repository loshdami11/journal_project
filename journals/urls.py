from django.urls import path
from .views import (
    JournalListView,
    JournalDetailView,
    JournalCreateView,
    JournalUpdateView,
    JournalDeleteView,
)   
    

urlpatterns = [
    path('', JournalListView.as_view(), name='home'),
    path('<int:pk>/', JournalDetailView.as_view(), name='journal-detail'),
    path('create/', JournalCreateView.as_view(), name='journal-create'),
     path('update/<int:pk>/', JournalUpdateView.as_view(), name='journal-update'),
    path('delete/<int:pk>/', JournalDeleteView.as_view(), name='journal-delete'),


]