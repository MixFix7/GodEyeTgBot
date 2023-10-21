from . import views
from django.urls import path


urlpatterns = [
    path('add-person-data/', views.AddPersonsData.as_view()),
    path('find-person/', views.FindPerson.as_view()),
]