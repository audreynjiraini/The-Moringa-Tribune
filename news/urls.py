from django.conf.urls import url
from . import views


# list of url instances for our app. create url instances by calling the url function and pass in the URL regular expression, the view and a name keyword argument.
urlpatterns=[
    url('^$', views.welcome, name= 'welcome'),
    url('^today/$', views.news_of_day, name= 'newsToday')
]