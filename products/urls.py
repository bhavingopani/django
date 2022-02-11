from django.urls import path    #to reference url - importing path function
from . import views  #here period means the current folder




urlpatterns = [
    path ('', views.index), #empty string represents root of this app #here we are not calling index function like views.index() -- we are just passing a reference to it views.index Django will take care of calling this function at run time - We dont call it as Django will call when user sends a http request to the sesrver
    path ('new', views.newproducts)
]
