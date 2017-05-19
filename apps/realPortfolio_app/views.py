from django.shortcuts import render, redirect

def index(request):
    return render(request, 'realPortfolio_app/index.html')
def about(request):
    return render(request, 'realPortfolio_app/about.html')
def projects(request):
    return render(request, 'realPortfolio_app/projects.html')
def testimonials(request):
    return render(request, 'realPortfolio_app/testimonials.html')
