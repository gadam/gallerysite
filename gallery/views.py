from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from gallery.forms import PostForm
from gallery.models import Post


def index(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.clean()
            Post(
                image=form.cleaned_data["image"],
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                pub_date=timezone.now()
            ).save()
            return redirect("/")
    else:
        form = PostForm()

    context = {
        "posts": Post.objects.all().order_by("pub_date").reverse(),
        "form": form
    }
    return render(request, "index.html", context)


def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.image.delete()
        post.delete()
    return redirect("/")
