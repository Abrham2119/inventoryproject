from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'dashboard/index.html')
def staff(request):
    return render(request,'dashboard/staff.html')
def products(request):
    
    return render(request,'dashboard/products.html')
def orders(request):
    return render(request,'dashboard/orders.html')