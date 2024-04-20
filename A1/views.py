from django.http import HttpResponse
from django.shortcuts import render
def defaultPage(request):
    data ={
        'title':'Home Page',
        'description': 'welcome to home page'
    }
    try:
        '''
        firstName = request.POST['fname']
        lastName = request.POST['lname']
        city = request.POST['city']
        '''
        firstName = request.POST['fname']
        lastName = request.POST['lname']
        city = request.POST['city']
        
        print(firstName,lastName,city)
        data = {
            'firstName':firstName,
            'lastName':lastName,
            'city':city
        }
        
    except:
        print("error")
    return render(request, "default.html",data)
def mainPage(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def serviceDetail(request,serviceid):
    return HttpResponse(serviceid)

def homePage(request):
    data = {
        'title': 'WElcome to hom epage',
        'description':'This is a home page description',
        'fetchData': ['php','python','java'],
        'details':[
                    {'id':1000,
                    'name':'chandan kumar',
                    'age':20,
                    'city':'indore'
                    },
                     {'id':1001,
                    'name':'mohan kumar',
                    'age':23,
                    'city':'dehi'
                    },
                     {'id':1002,
                    'name':'sohan',
                    'age':26,
                    'city':'dehi'
                    }
                    ]
    }
    return render(request, 'index.html',data)