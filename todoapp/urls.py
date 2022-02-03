from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home),
    path('delete/<int:task_id>',views.taskDone,name = 'delete'),
    path('cbvtask/',views.TaskListView.as_view(),name = 'classBasedView')
]