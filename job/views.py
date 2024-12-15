from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Job
from django.core.paginator import Paginator
from .forms import ApplyForm 


# class JobListView(ListView):
#     model = Job
#     template_name = 'job/job_list.html'


# class JobDetailView(DetailView):
#     model = Job
#     template_name = 'job/job_details.html'



def job_list(request):
    job_list = Job.objects.all()
    paginator = Paginator(job_list,1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    jobs = {'jobs' : page_obj}
    return render(request, 'job/job_list.html', jobs)



def job_deatils(request, slug):
    job_deatils = Job.objects.get(slug=slug)

    if request.method == 'POST':
        pass
    else:

        form = ApplyForm()

    job = {'job' : job_deatils, 'form': form}


    return render(request, 'job/job_details.html', job)