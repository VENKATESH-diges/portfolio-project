from django.urls import path
from . import views
urlpatterns = [
    path('siging_Portfolio/', views.signup, name='sign_in')
    
]
