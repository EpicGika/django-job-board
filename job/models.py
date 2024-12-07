from django.db import models

# Create your models here.

JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
)

class Job(models.Model):
    # - title
    # - location 
    # - job type 
    # - job description 
    # - job summry (publishd_at - vacancy - salary - job 

    title = models.CharField(max_length=100)
    # location = models
    job_type = models.CharField(max_length=50, choices=JOB_TYPE)
    description = models.TextField(max_length=1000,blank=True, null=True)
    published_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experince = models.IntegerField(default=1)




    def __str__(self):
        return self.title