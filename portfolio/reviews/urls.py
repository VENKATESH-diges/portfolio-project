from django.urls import path
from . import views
urlpatterns = [
    path('reviews/', views.Reviews_page ,  name="reviewspage"),
    path('ReviewsPage/',views.review_submit ),
    path ("Reviewsall/",views.reviews_all , name="reviews_all")

]

