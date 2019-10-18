from django import forms

# Import the class we created in models.py

from .models import Post

# Create a blog form based on the Post class we created in models.py

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        
        # Include on the form only those fields the user can edit (dont include
        # 'views' or 'created_date')
        
        fields = ('title', 'content', 'image', 'tag', 'published_date')
        
    
