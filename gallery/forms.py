from django import forms

from gallery.models import Post


class PostForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))

    class Meta:
        model = Post
        fields = ["image", "title", "description"]
