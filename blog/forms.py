from django import forms
from blog.models import Post

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('music_url',)
        labels = {
        "music_url": "Spotify Music Link"
        }
