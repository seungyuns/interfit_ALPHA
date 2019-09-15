from django.db import models

class Recruitlist(models.Model):

    recruit_company_name = models.CharField(max_length=100)
    recruit_summary = models.CharField(max_length=100) 
    recruit_company = models.CharField(max_length=100)  
    recruit_position = models.CharField(max_length=100)
    recruit_position2 = models.CharField(max_length=100)
    recruit_position_detail = models.CharField(max_length=100)
    recruit_salary = models.CharField(max_length=100)
    recruit_position_detail2 = models.TextField()
    recruit_company_detail = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.recruit_company_name

    def summary(self):
        return self.recruit_position_detail2[:100]