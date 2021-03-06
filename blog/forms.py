from django import forms
from blog.models import Post

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('music_link',)
        labels = {
        "music_link": "Spotify Music Link"
        }
