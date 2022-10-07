from django.db import models
from mainuser.models import NewUser, Userprofile


class Category(models.Model):

    category_name = models.CharField(max_length=225)
    slug = models.SlugField(max_length=100,unique=True,null=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):

        return self.category_name    


class JobsPosting(models.Model):

    user = models.ForeignKey(NewUser,on_delete=models.CASCADE,related_name='jobs_user')
    profile = models.ForeignKey(Userprofile,on_delete=models.CASCADE,related_name='jobs_profile') 
    category = models.ManyToManyField(Category,related_name='jobs_category')
    job_title = models.CharField(max_length=225)
    job_description = models.TextField()

    def __str__(self):

        return self.job_title       
