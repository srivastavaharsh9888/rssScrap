from django.conf.urls import url
from . import views

urlpatterns = [
    url('home/$',views.home,name='home'),
    url('showData/$',views.scrapeData,name='data'),
    url('$',views.showHome,name='re'),
]
