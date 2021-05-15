from django.urls import path
from . import views
from .views import(
    BlogListView, 
    BlogDetailView, 
    BlogCreateView, 
    BlogUpdateView, 
    BlogDeleteView
)

    
urlpatterns = [
    path('', views.register_request, name='register'),
    path('register', views.register_request, name='register'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name= 'logout'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('home', BlogListView.as_view(), name='home'),
    path('post/home', BlogListView.as_view(), name='home'),
]






















