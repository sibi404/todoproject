from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.accountLogin,name = 'login'),
    path('register/',views.registration,name = 'registration'),
    path('logout',views.logout,name='logout')
]