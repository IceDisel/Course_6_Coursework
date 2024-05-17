from django.urls import path
from django.views.decorators.cache import cache_page
from blog.apps import BlogConfig
from blog.views import BlogPostListView, BlogPostCreateView, BlogPostDetailView, BlogPostUpdateView, BlogPostDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('blogpost_list/', cache_page(60)(BlogPostListView.as_view()), name='blogpost_list'),
    path('blogpost_detail/<int:pk>', BlogPostDetailView.as_view(), name='blogpost_detail'),
    path('blogpost_edit/<int:pk>', BlogPostUpdateView.as_view(), name='blogpost_edit'),
    path('blogpost_delete/<int:pk>', BlogPostDeleteView.as_view(), name='blogpost_delete'),
    path('blogpost_form/', BlogPostCreateView.as_view(), name='blogpost_form'),

]
