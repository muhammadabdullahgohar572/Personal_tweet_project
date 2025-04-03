
from django.urls import path
from . import views


urlpatterns = [
  
    path('',views.HomePage,name="Home_Page"),
    path('Tweet_Create',views.Tweet_Create,name="Tweet_Create"),
    
    
]
