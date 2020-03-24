from django.shortcuts import render, get_object_or_404, redirect
from .models import Tool, Blog, Comment
from django.template import loader
from django.views import generic
from django.urls import reverse
import datetime


def homepage(request):
    return render(request, 'tools/homepage.html')

class BlogView(generic.ListView):
    template_name = 'tools/blog.html'
    context_object_name = 'blog_list'

    def get_queryset(self):
        return Blog.objects.order_by('-date')

class EntryView(generic.DetailView):
    model = Blog
    template_name = 'tools/blog/entry.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(blog = self.get_object())
        return context

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
