from django.urls import path
from . import views
urlpatterns = [
    path('api/v1/recordslist/', views.CreateListRecordsAPIView.as_view()),
]
