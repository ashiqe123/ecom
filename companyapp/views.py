from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def electronics(request):
    return render(request,'electronics.html')

def fashion(request):
    return render(request,'fashion.html')

def watche_ornaments(request):
    return render(request,'jewels.html')

def mens_fashion(request):
    return render(request,'gents.html')

def womens_fashion(request):
    return render(request,'women.html')