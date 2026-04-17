from django.http import HttpResponse

def home_view(request):
    print(request)
    return HttpResponse('<h1> Olá Mundo! </h1>')