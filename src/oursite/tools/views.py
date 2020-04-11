from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Tool, Blog, Comment
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse


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


def postblog(request, **kwargs):
    contents = request.POST.get("content")
    nameGiven = request.POST.get("name")
    titleGiven = request.POST.get("title")

    if nameGiven == "":
        nameGiven = "Anonymous"

    if titleGiven == "":
        titleGiven = "Untitled Post"

    if contents == "":
        contents = "No content."

    blognew = Blog.objects.create(title = titleGiven, author = nameGiven, content = contents) 

    return redirect('blog')


def reserve(request):
    if request.method == 'POST':
        tool = get_object_or_404(Tool, pk=tool)
        tool.borrower = User.objects.get(pk=user)
        return HttpResponseRedirect(reverse('tools'))
    return render(request, 'tools/toolview.html', context)


def tools(request):
    tools_list = Tool.objects.order_by('name')
    context = {'tools_list': tools_list}
    if request.method == 'POST':
        tool = request.POST['tool']
        user = None
        if request.user.is_authenticated:
            user = request.user.username
        results = Tool.objects.filter(name=tool).count()
        if results <= 0:
            pass # do nothing
        else:
            tool_mod = Tool.objects.get(name=tool)
            if tool_mod.borrower is None:
                name = ""
            else:
                name = tool_mod.borrower.username
            if name == user:
                tool_mod.borrower = None
                tool_mod.status = 'a'
                tool_mod.save()
            else:
                tool_mod.borrower = User.objects.get(username=user)
                tool_mod.status = 'r'
                tool_mod.save()
        return HttpResponseRedirect(reverse('tools'))
    return render(request, 'tools/toolview.html', context)


def contact(request):
    return render(request, 'tools/contact.html')


def about(request):
    return render(request, 'tools/about.html')
# Create your views here.
