from django.urls import include, path
from authapp import views

#new --------


urlpatterns = [
     path('signup/', views.signup, name='signup'),
     path('login/',views.handleLogin, name ='handleLogin'),
     path('logout/',views.handleLogout, name ='handelLogout'),  
]