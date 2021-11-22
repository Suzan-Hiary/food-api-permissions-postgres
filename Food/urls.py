from django.urls import path 

from .views import Foodviewset , FoodDetails



urlpatterns =[
    
    path('' , Foodviewset.as_view() , name='food'),
    path('<int:pk>',  FoodDetails.as_view(), name='food_details')
]