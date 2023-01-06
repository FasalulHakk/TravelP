from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from .models import travel

# Create your views here.

# def main(request):
#     return render(request, 'home.html')
# def about(request):
#     return render(request, 'aboutus.html')
# def contact(request):
#     return HttpResponse('(+91)8156-859-334')
# def details(request):
#     return HttpResponse('You are welcome')
# def end(request):
#     return HttpResponse('Thanks')

# def main1(request):
#     return render(request, 'operators.html')
#
#
# def addition(request):
#     n1 = int(request.GET['num1'])
#     n2 = int(request.GET['num2'])
#     res1 = n1 + n2
#
#     n1 = int(request.GET['num1'])
#     n2 = int(request.GET['num2'])
#     res2 = n1 - n2
#
#     n1 = int(request.GET['num1'])
#     n2 = int(request.GET['num2'])
#     res3 = n1 * n2
#
#     n1 = int(request.GET['num1'])
#     n2 = int(request.GET['num2'])
#     res4 = n1 / n2
#
#     return render(request,'basic_calc.html', {'add_1': res1,'sub_tn': res2, 'mul_3': res3, 'div_4': res4})
from .models import team


def main2(request):
    obj = travel.objects.all()
    obj2 = team.objects.all()
    return render(request, 'index.html', {'photos': obj, 'players': obj2})




