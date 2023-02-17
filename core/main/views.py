from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')


def res(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    char =request.POST['char']
    if char == '+':
        res = num1 + num2
    elif char == '-':
        res = num1 - num2
    elif char == '*':
        res = num1 * num2
    elif char == '/':
        res = num1 / num2
    return render(request, 'res.html', {'res':res})
