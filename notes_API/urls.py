
from django.urls import path
from .import views

urlpatterns = [
    path('notes/', views.note_view, name="note_view"), 
    path('notes/<slug:slug>', views.note_detail_view, name="note_detail_view"),
    path("notes-search/", views.search_notes, name='notes-search')
]



