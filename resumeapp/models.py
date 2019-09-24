from django.db import models


class Resumelist(models.Model):

    company = models.CharField(max_length=100)  
    position = models.CharField(max_length=100) 
    position2 = models.CharField(max_length=100)
    position_detail = models.CharField(max_length=100, null=True) 
    resume_name = models.CharField(max_length=100) 
    sex = models.CharField(max_length=100)
    born_year = models.CharField(max_length=100) 
    final_edu = models.CharField(max_length=100) 
    work_year = models.CharField(max_length=100)
    work_year_avg = models.CharField(max_length=100, null=True) 
    phone_number = models.CharField(max_length=100, null=True) 
    email_address = models.CharField(max_length=100, null=True) 
    resume_detail = models.TextField()
    salary = models.CharField(max_length=100, null=True)
    salary_fit = models.CharField(max_length=100, null=True) 
    job_fit = models.CharField(max_length=100, null=True) 
    outcome = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.resume_name

    def summary(self):
        return self.resume_detail[:100]
