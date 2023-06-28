from django.shortcuts import render


def main(request):
    return render(request, 'main.html')


def about_me(request):
    return render(request, 'about_me.html')

