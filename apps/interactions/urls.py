from django.urls import path
from . import views

urlpatterns = [
    path('like/<str:story_id>/', views.toggle_like, name='toggle_like'),
    path('comment/<str:story_id>/add/', views.add_comment, name='add_comment'),
    path('comment/<str:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('reading-list/', views.reading_list_view, name='reading_list'),
    path('reading-list/<str:story_id>/toggle/', views.toggle_reading_list, name='toggle_reading_list'),
]
