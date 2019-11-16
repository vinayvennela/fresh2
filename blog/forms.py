from django import forms
from django.contrib.auth.models import User
from blog.models import UserFeatures,Post,Comments

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class SignUpFormPart(forms.ModelForm):

    class Meta():
        model = UserFeatures
        fields = ('penname','profileimage')

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields=('author','title','text')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comments
        fields = ('author','text')

        widgets ={
        'author':forms.TextInput(attrs={'class':'textinputclass'}),
        'text': forms.Textarea(attrs={'class':'ediatble medium-editor-textarea  '})
        }
