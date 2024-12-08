from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobListView.as_view(), name='joblist'),
    # path('', views.job_list, name='joblist'),
    # path('<int:id>', views.job_deatils, name='jobdeatil'),
    path('<int:pk>', views.JobDetailView.as_view(), name='jobdeatil'),
]