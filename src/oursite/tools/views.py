from django.shortcuts import render, get_object_or_404
from .models import Tool


def homepage(request):
    return render(request, 'tools/homepage.html')

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
