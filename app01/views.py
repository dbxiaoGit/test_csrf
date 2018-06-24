from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the app01 index.")

def transfer(request):
    if request.method == 'POST':
        from_ = request.POST.get('from_')
        to_ = request.POST.get('to_')
        money = request.POST.get('money')
        print('{}转给{}了{}元钱'.format(from_, to_, money))
        return HttpResponse('转账成功')
    return render(request,'zhuanzhang.html')