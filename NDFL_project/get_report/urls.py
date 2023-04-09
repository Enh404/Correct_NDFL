from django.urls import path

from . import views

app_name = 'get_report'

urlpatterns = [
    path('', views.ExcelReportView.as_view(), name='report'),
]