from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Category
from comments.models import Comment
from comments.forms import CommentForm


def writings_list(request):
    posts = Post.objects.all()
    category = request.GET.get('category')
    search = request.GET.get('search')
    
    if category:
        posts = posts.filter(category__slug=category)
    
    if search:
        posts = posts.filter(title__icontains=search) | posts.filter(content__icontains=search)
    
    categories = Category.objects.all()
    
    context = {
        'posts': posts,
        'categories': categories,
        'selected_category': category,
        'search_query': search,
    }
    return render(request, 'writings/writings_list.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    
    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Your comment has been posted!')
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()
    
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'can_edit': request.user == post.author,
        'can_delete': request.user == post.author,
    }
    return render(request, 'writings/post_detail.html', context)


@login_required(login_url='login')
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category_id = request.POST.get('category')
        inspiration_note = request.POST.get('inspiration_note')
        
        category = get_object_or_404(Category, pk=category_id) if category_id else None
        
        post = Post.objects.create(
            title=title,
            content=content,
            author=request.user,
            category=category,
            inspiration_note=inspiration_note if inspiration_note else ''
        )
        
        messages.success(request, 'Your writing has been published!')
        return redirect('post_detail', pk=post.pk)
    
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'writings/create_post.html', context)


@login_required(login_url='login')
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.user != post.author:
        messages.error(request, 'You can only edit your own posts.')
        return redirect('post_detail', pk=post.pk)
    
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        category_id = request.POST.get('category')
        post.inspiration_note = request.POST.get('inspiration_note')
        
        if category_id:
            post.category = get_object_or_404(Category, pk=category_id)
        
        post.save()
        messages.success(request, 'Your writing has been updated!')
        return redirect('post_detail', pk=post.pk)
    
    categories = Category.objects.all()
    context = {
        'post': post,
        'categories': categories,
    }
    return render(request, 'writings/edit_post.html', context)


@login_required(login_url='login')
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.user != post.author:
        messages.error(request, 'You can only delete your own posts.')
        return redirect('post_detail', pk=post.pk)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Your writing has been deleted.')
        return redirect('writings_list')
    
    context = {'post': post}
    return render(request, 'writings/confirm_delete.html', context)
