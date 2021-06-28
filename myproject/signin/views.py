from django.shortcuts import render

# Create your views here.
def index(request):
    #print("abcd....index...")
    return render(request, 'signin.html')