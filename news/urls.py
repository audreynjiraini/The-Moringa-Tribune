from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


# list of url instances for our app. create url instances by calling the url function and pass in the URL regular expression, the view and a name keyword argument.
urlpatterns=[
    url('^$', views.news_today, name= 'newsToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    url(r'^search/$', views.search_results, name = 'search_results'),
    url(r'^article/(\d+)', views.article, name = 'article'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)