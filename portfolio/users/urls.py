from django.urls import path
from . import views
urlpatterns = [
    path('wellcome/',views.Enter_page,name="login_enterpage"),
    path("forget/",views.forget_p,name="password_reset"),
    path('logout/',views.log_out,name='logout'),
    path("Home/",views.home , name="home")
    

]
