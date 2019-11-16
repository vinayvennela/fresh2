from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class UserFeatures(models.Model):
    penname = models.CharField(max_length=100, unique = True)
    profileimage = models.ImageField(upload_to='profilepics',blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    #Indicates where to look after an instance is created
    def get_absolute_url(self):
        return reverse("blog:post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comments(models.Model):
    #See the representation how a model is called - Post model in blog app
    post = models.ForeignKey('blog.Post',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    create_date= models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
