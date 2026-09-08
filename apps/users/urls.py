from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('profile/<str:username>/edit/', views.edit_profile_view, name='edit_profile'),
    path('profile/<str:username>/follow/', views.follow_view, name='follow'),
    # Admin
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/users/', views.admin_users, name='admin_users'),
    path('admin/users/<str:user_id>/toggle/', views.admin_toggle_user, name='admin_toggle_user'),
    path('admin/stories/', views.admin_stories, name='admin_stories'),
    path('admin/stories/<str:story_id>/toggle/', views.admin_toggle_story, name='admin_toggle_story'),
    path('admin/stories/<str:story_id>/delete/', views.admin_delete_story, name='admin_delete_story'),
    path('admin/comments/', views.admin_comments, name='admin_comments'),
    path('admin/comments/<str:comment_id>/delete/', views.admin_delete_comment, name='admin_delete_comment'),
    path('admin/purchases/', views.admin_purchases, name='admin_purchases'),
]
