from django.urls import path
from . import views

app_name = 'job'

urlpatterns = [
    # path('', views.JobListView.as_view(), name='joblist'),
    path('', views.job_list, name='joblist'),
    path('add', views.add_job, name='add_job'),
    path('<str:slug>', views.job_deatils, name='job_deatils'),
    # path('<int:pk>', views.JobDetailView.as_view(), name='jobdeatil'),
]