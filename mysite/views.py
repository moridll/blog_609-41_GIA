from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('<h1>Home</h1>')
    return render(request, 'homepage.html')

def about(request, company_name, company_phone):
    # return HttpResponse(f"""<h1>About</h1>
    # <div> Company Name: {company_name} </div>
    # <div> Company Phone: {company_phone} </div>
    # """)
    return render(request, 'about.html')