from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from blog.forms import SignUpForm,SignUpFormPart,PostForm,CommentForm
from blog.models import Post,Comments
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils import timezone

# Create your views here.
def createUser(request):
    # template_name='blog/signup.html'
    if request.method=='POST':
        userform = SignUpForm(request)

    userform = SignUpForm()
    userformPart = SignUpFormPart()
    return render(request,'blog/signup.html',{'userform':userform,'userformPart':userformPart})


class HomePageView(TemplateView):
    template_name = 'blog/home.html'

class About_View(TemplateView):
    template_name = 'blog/about.html'

class PostListView(ListView):
    model = Post

    #Custom query
    def get_queryset(self):
        #ORM of Django __ lte - lessthan or equal to ,
        # - indicates descending order
        # with below line we are mentioning that grab all objects of Post Model and then filter based on published less than or equal to
        # current datetime and order then in descending order
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

# @login_requried  - works only for functions based views
#Need to use mixins for class based views

class CreatePostView(LoginRequiredMixin,CreateView):
    # When using the LoginRequiredMixin, we need to setup few details like below
    # login_url is needed to say if user is not logged in , then where to redirect
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    #Maps a form class
    form_class = PostForm
    model = Post

class UpdatePostView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    #Maps a form class
    form_class = PostForm
    model = Post

class DeletePostView(LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    model = Post
    success_url = reverse_lazy('blog:post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url='login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')

########################################################
# Adding comment
#################################################
@login_required
def add_comment_to_post(request,pk):
    # Get the post object or 404 page
    post = get_object_or_404(Post,pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment= form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail',pk=post.pk)
    else :
        form = CommentForm()

    return render(request,'blog/comment_form.html',{'form':form})

#######################################################
# Comment Approval
###############################
@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comments,pk=pk)
    comment.approve()
    return redirect('blog:post_detail',pk=comment.post.pk)

##################################
# Delete Post
######################

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comments,pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('blog:post_detail',pk=post_pk)

########################################
# Publish Post
###################################
@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)

    post.publish()
    return redirect('blog:post_detail',pk=post.pk)
