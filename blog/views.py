from django.shortcuts import render
from django.utils import timezone
from .models import Post

i = 1

def post_list(request):
    return render(request,'blog/post_list.html')  
 
def tab(request):
        num1 = dict()
        number =int (request.GET.get('num'))
        for i in range(1,11):
            num1[i] = number*i

        return render(request,'blog/tab.html',{"result" : num1})
        return render(request,'blog/tab.html',{"number" : number})