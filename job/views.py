from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Job
# Create your views here.



class JobListView(ListView):
    model = Job
    template_name = 'job/job_list.html'


class JobDetailView(DetailView):
    model = Job
    template_name = 'job/job_details.html'



# def job_list(request):
#     job_list = Job.objects.all()
#     jobs = {'jobs' : job_list}
#     return render(request, 'job/job_list.html', jobs)

# def job_deatils(request, id):
#     job_deatils = Job.objects.get(id=id)
#     job = {'job' : job_deatils}
#     return render(request, 'job/job_details.html', job)