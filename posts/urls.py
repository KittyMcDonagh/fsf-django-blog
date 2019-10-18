from django.conf.urls import url
from.views import get_posts, post_detail, create_or_edit_post

urlpatterns = [
    
    # Root dir, if we've gone to posts, we want to get the view with that name
    
    url(r'^$', get_posts, name='get_posts'),
    
    # If its passed in with an ID ('d+' indicates a decimal number) we want to 
    # open the post detail view
    
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    
    # If we want to create a new post - Note the name is not the same as the
    # view in this instance
    
    url(r'^new/$', create_or_edit_post, name="new_post"),
    
    # If we want to create a new post - Note the name is not the same as the
    # view in this instance
    
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_post, name='edit_post'),
    
]