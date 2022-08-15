from django.contrib import admin

from jobs.models import Category, JobsPosting

admin.site.register(Category)
admin.site.register(JobsPosting)
