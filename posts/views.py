from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm


#Create first view - get a list of all the posts

def get_posts(request):
    
    """
    Create a list of all the Posts that were published prior to 'now' and
    render them to the 'blogposts.html' template
    """
    
    # Create posts object, all posts created up to 'now', sorted by
    # published_date in descending order (notice the '-' before 
    # 'published_date')
    # (if you a red x telling you that there's no object for Post, ignore it,
    # Django will create it when needed.)
    
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return  render(request, 'blogposts.html', {'posts': posts})


def post_detail(request, pk):
    
    """
    Create a view that returns a single Post object based on the Post ID(pk)
    and render it to the 'postdetail.html' template or return a 404 error if
    the Post is not found.
    """
    
    post = get_object_or_404(Post, pk=pk)
    
    # Increment number of views this post has received
    
    post.views +=1
    post.save()
    return  render(request, 'postdetail.html', {'post': post})

def create_or_edit_post(request, pk=None):
    """
    Create a view that allows us to create or edit a view depending on 
    whether the pk is null or not. 
    """
    
    post = get_object_or_404(Post, pk=pk) if pk else None
    
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post_detail, post.pk)
            
    else:
        form = BlogPostForm(instance=post)
    
    return  render(request, 'blogpostform.html', {'form': form})