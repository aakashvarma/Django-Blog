from django.http import HttpResponse
from django.shortcuts import render ,get_object_or_404
from .models import Post

# Create your views here.


def posts_home(request):


	queryset = Post.objects.all().order_by('-timestamp')
	context = {
		"object_list": queryset,
		"title": "List"
	}
	return render(request, "index.html", context)

def posts_detail(request, id):

	instance = get_object_or_404(Post, id=id)
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "posts_details.html", context)
