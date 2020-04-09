from django.shortcuts import render, get_object_or_404, redirect
from .models import Tool, Blog, Comment
from django.template import loader
from django.views import generic
from django.urls import reverse
from django import forms
import datetime


def homepage(request):
    return render(request, 'tools/homepage.html')

class BlogView(generic.ListView):
    template_name = 'tools/blog.html'
    context_object_name = 'all_blog_list'

    def get_queryset(self):
        return Blog.objects.order_by('-date')

class EntryView(generic.DetailView):
    model = Blog
    template_name = 'tools/entry.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(blog = self.get_object())
        return context


def blogtest(request):
    blog1 = Blog.objects.create(title = "new post", author = 'NA', content = 'content of blog +')
    Blog.objects.all().delete()
    return redirect('blog')

def postcomment(request, **kwargs):
    contents = request.POST.get("content")
    nameGiven = request.POST.get("name")
    titleGiven = request.POST.get("title")

    blognew = Blog.objects.create(title = titleGiven, author = nameGiven, content = contents) 

    return redirect('blog')

def tools(request):
    tools_list = Tool.objects.order_by('name')
    context = {'tools_list': tools_list}
    return render(request, 'tools/toolview.html', context)


def tool_view(request, tool_id):
    tool = get_object_or_404(Tool, pk=tool_id)
    return render(request, 'tools/tool.html', {'tool': tool})

def contact(request):
    return render(request, 'tools/contact.html')

def about(request):
    return render(request, 'tools/about.html')
# Create your views here.
