from django.shortcuts import render

from django.http import HttpResponse

def home(request):

    peoples = [
            { 'name' : 'Chirayu', 'age': 19} ,
            { 'name' : 'hiten', 'age': 13} ,
            { 'name' : 'meet', 'age': 16} ,
            { 'name' : 'akshat', 'age': 17} ,
            { 'name' : 'raj', 'age': 18} ,
            { 'name' : 'Yash', 'age': 20} ,
]
    return render(request, "home/index.html" , context={'peoples' : peoples} ,)



def about(request):
    return render(request , "home/about.html")

def contact(request):
    return render(request , "home/contact.html")




def success_page(request):
    return HttpResponse("<h1> This Is The Success Page</h1>")