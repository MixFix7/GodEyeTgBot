from . import views
from django.urls import path


urlpatterns = [
    path('add-presons-data/', views.AddPersonsData.as_view()),
    path('find-person/', views.FindPerson.as_view()),
]