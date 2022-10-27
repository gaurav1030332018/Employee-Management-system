from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    print("Home function")
    isActive=True
    name="Gaurav"
    list_of_program=[
        'WAP to check even or odd',
        'WAP to check prime number',
        'wap to print all prime numbers from 1 to 100',
        'WAP to print pascals triangle'
    ]

    student={
        'student_name':"Rahul",
        'student_collage':"ZYZ",
        'student_city':"lucknow"
    }

    data={
        'isActive':isActive,
        'name':name,
        'list_of_program':list_of_program,
        'student':student

    }
    #return HttpResponse("<h1>Hello this is index page</h1>")
    return render(request,"home.html",data)
def about(request):
    return render(request,"about.html",{})

def services(request):
    return render(request,"services.html",{})
