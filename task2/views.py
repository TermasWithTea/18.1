from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
def func(request):
    return render(request,'second_task/func_template.htmll')

class Class(TemplateView):
    template_name = 'second_task/class_template.html'