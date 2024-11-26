from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello world')

def Calculator(request):
    out=''
    if request.method == 'POST':
        n1=float(request.POST.get('num1'))
        n2=float(request.POST.get('num2'))
        operator=request.POST.get('oper')
        if operator=="+":
            out=n1+n2
        elif operator=="-":
            out=n1-n2
        elif operator=="*":
            out=n1*n2
        elif operator=="/":
            out=n1/n2

        else:
            print("invalid operation")
    print(out)

    return render(request,'calculator.html',{'out':out})