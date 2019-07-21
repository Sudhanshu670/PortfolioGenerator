from django.urls import path
from main import views
urlpatterns=[
    
    path('project/',views.project,name= "project"),
    path('languages/',views.languages,name="languages"),
    path('education/',views.education,name="education"),
    path('achievements/',views.achievements,name="achievements"),
    path('',views.index,name="index")
]
