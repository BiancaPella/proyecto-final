from django import forms   
from .models import Comment, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'header_image', 'title_tag', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Titulo del post'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Tag del post'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Cuerpo del post'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Titulo del post'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Tag del post'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Cuerpo del post'}),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
