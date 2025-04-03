
from django.urls import path
from . import views


urlpatterns = [
  
    path('',views.HomePage,name="Home_Page"),
    path('Tweet_Create',views.Tweet_Create,name="Tweet_Create"),
    path('Deleted_Tweet/<int:emp_id>/',views.DeleteTweet,name="deletetweet"),
    path('updated_Tweet/<int:emp_id>/',views.Tweet_Update,name="updatedtweet"),
    path('Tweet_Updated/<int:emp_id>/',views.Updated_Tweet,name="Tweet_Updated"),
    
    
]
