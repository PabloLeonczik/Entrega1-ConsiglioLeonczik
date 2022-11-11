from django.urls import path
from account import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.mi_login, name = 'login'),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name = 'logout'),

]