from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Job
from django.core.paginator import Paginator
from .forms import ApplyForm, JobForm
from django.urls import reverse


# class JobListView(ListView):
#     model = Job
#     template_name = 'job/job_list.html'


# class JobDetailView(DetailView):
#     model = Job
#     template_name = 'job/job_details.html'



def job_list(request):
    job_list = Job.objects.all()
    paginator = Paginator(job_list,3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    jobs = {'jobs' : page_obj}
    return render(request, 'job/job_list.html', jobs)



def job_deatils(request, slug):
    job_deatils = Job.objects.get(slug=slug)

    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_deatils
            myform.save()

    else:

        form = ApplyForm()

    job = {'job' : job_deatils, 'form': form}


    return render(request, 'job/job_details.html', job)



def add_job(request):

    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:joblist'))
    
    else:
        form = JobForm()

    return render(request,'job/add_job.html',{'form':form})