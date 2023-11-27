from django.shortcuts import render

def main(request):
    return render(request,'index.html',{})

def pd(request):
    return render(request,'property-details.html',{})

def contact(request):
    return render(request,'contact.html',{})

def properties(request):
    return render(request,'properties.html',{})