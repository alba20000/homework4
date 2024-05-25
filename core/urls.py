from django.urls import path
from core import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('staff_model', views.StaffModel, basename='staff_model')

urlpatterns = [
    path('staff/', views.Staff.as_view(), name='staff'),
    path('staff_api/', views.StaffAPI.as_view(), name='staff_api')
]

urlpatterns += router.urls
