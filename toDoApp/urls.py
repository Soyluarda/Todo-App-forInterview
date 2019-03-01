from django.conf.urls import url,include
from toDoApp import views
from django.contrib.auth.views import login,logout
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todos',views.TodoView)

urlpatterns = [
    url(r'^api/',include(router.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^login/$',login,{'template_name':'todo/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'todo/logout.html'}),
    url(r'^registered/$',views.register,name="register"),
    url(r'^add/$', views.addToDo, name='add'),
    url(r'complete/(?P<todo_id>\d+)$', views.completeToDo, name='complete'),
    url(r'uncomplete/(?P<todo_id>\d+)$', views.NotToDo, name='uncomple'),
    url(r'^deletecomplete/$', views.deleteCompleted, name='delcomplete'),
    url(r'^deleteall/$', views.deleteAll, name='delall')

]