from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home),
    path('delete/<int:task_id>',views.taskDelete,name = 'delete'),
    path('add_task/',views.add_task,name = 'add_task'),
    path('cbvtask/',views.TaskListView.as_view(),name = 'classBasedView'),
    path('taskComplete/<int:task_id>',views.taskComplete,name = 'complete')
]