from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('add', views.AddNewRecruiteAPIView.as_view()),
    path('accepted-recruits', views.AcceptedRecruitsAPIView.as_view()),
    path('rejected-recruits', views.RejectedRecruitsAPIView.as_view()),
    path('potential-airforce-recruits', views.PotentialAirforceRecruitsAPIView.as_view()),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
