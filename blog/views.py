from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    return render(request,'blog/post_list.html')  
 
def tab(request):
        num1 = dict()
        number =int (request.GET.get('num'))
        for i in range(1,13):
            num1[i] = number*i

        return render(request,'blog/tab.html',{"result" : num1})