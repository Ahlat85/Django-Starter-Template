from django.shortcuts import render

def index(request):
  context = {
    'title_page': 'Index'
  }
  return render(request, 'home/index.html', context)