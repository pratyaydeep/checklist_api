from django.urls import path
from core.views import TestAPIView, CheckListAPIView

urlpatterns = [
    path('', TestAPIView.as_view()),
    path('api/checklists/', CheckListAPIView.as_view()),
]
