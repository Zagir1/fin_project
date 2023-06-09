from django.urls import path
from members import views
from django.contrib.auth.views import LogoutView


app_name = 'members'

urlpatterns = [
                path('login/', views.LoginUser.as_view(), name='login'),
                path('logout/', LogoutView.as_view(next_page='core:home_page'), name='logout'),
                path('register/', views.RegisterView.as_view(), name='register'),
              ]
