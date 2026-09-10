from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('browse/', views.browse_view, name='browse'),
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),
    path('stories/create/', views.create_story_view, name='create_story'),
    path('stories/mine/', views.my_stories_view, name='my_stories'),
    path('stories/dashboard/', views.dashboard_view, name='dashboard'),
    path('stories/<str:story_id>/', views.story_detail_view, name='story_detail'),
    path('stories/<str:story_id>/edit/', views.edit_story_view, name='edit_story'),
    path('stories/<str:story_id>/delete/', views.delete_story_view, name='delete_story'),
    path('stories/<str:story_id>/add-chapter/', views.add_chapter_view, name='add_chapter'),
    path('stories/<str:story_id>/read/<int:chapter_number>/', views.reader_view, name='reader'),
]
