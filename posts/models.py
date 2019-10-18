from django.db import models

from django.utils import timezone


class Post(models.Model):
    """
    A single blog post
    """
    # Title of blog
    title = models.CharField(max_length=200)
    
    #Content of blog
    content = models.TextField()
    
    # Add date and time as soon as blog is created
    created_date = models.DateTimeField(auto_now_add=True)
    
    # Published date not necessarily same as created date so, allow blank, null,
    # and default to the time now
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    
    # Keep count of views - default to 0, as no views yet
    views = models.IntegerField(default=0)
    
    # Allow user to add tags so that we can group blog posts together
    tag = models.CharField(max_length=30)
    
    # Allow user to upload an image to the img folder under 'media'
    image = models.ImageField(upload_to='img', blank=True, null=True)
    
    
    def __unicode__(self):
        return self.title