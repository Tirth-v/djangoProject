from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# We can create two types of views first is function based view and second is class based view.
# Let's look at function based views firstly.
""" 
 - A function based view, is a python function that takes a web request and returns a web response.
 - This response can be the HTML contents of a web page, or a redirect, or a 404 error, or an XML
   document, or an image or anything.
 - Each view function takes an HttpRequest object as its first parameter.
   The view returns an HttpResponse objectt that contains the generated response. Each view function is
   responsible for returning an HttpResponse object.
 - We will call these functions as view function or view function of application or view. 
"""
#HttpResponse
def func(request):
   return HttpResponse(request,"<h1>Hello this is response</h1>")
#render
"""
In Django, render is a function provided by django.shortcuts that simplifies the process of rendering 
an HTML template with context data. It takes the request object, template name, and a dictionary 
of context data as parameters, and returns an HttpResponse object with the rendered content.
"""
def func1(request):
   return render(request,"index.html")

def function(request):
   for i in range(0,11):
      if i/2 == 0:
         print(i)
      else:
         print("odd number")