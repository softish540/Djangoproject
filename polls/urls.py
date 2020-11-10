from django.urls import path
#no admin path needed in poll app
from . import views #from polls dir import view

#mapping a url to a template
app_name = 'polls' #creating a name space for polls app
urlpatterns = [
    path('',views.index, name='index'),
]