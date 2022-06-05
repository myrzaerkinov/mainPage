from django.urls import path
from . import views
urlpatterns = [
    path('api/v1/recordslist/', views.CreateListRecordsAPIView.as_view()),
    path('api/v1/<int:id>/', views.ListTimeRecordsAPIView.as_view()),
    path('api/v1/m/<int:id>/', views.ListFreeDayAPIView.as_view()),
    path('api/v1/user/records/<int:id>/', views.ListUserRecordsAPIView.as_view()),
    path('api/v1/popular/salon/', views.SalonListAPIView.as_view()),
    path('api/v1/category/salon/', views.CategoryListAPIView.as_view()),
    path('api/v1/category/salon/<int:id>/', views.ListCategoryAPIView.as_view()),

]
