from django.shortcuts import render, redirect

def home(requests):
    return render(requests, 'home.html')