from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=150, blank=False)
    surname = models.CharField(max_length=150, blank=True)
    job_description = models.CharField(max_length=445, blank=True)
    def __str__(self):
        return self.name

class Articles(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=True)
    summary = models.CharField(max_length=255, blank=True)
    content = models.CharField(max_length=255, blank=True)
    published = models.BooleanField(default=False)
    published_date = models.DateField(blank=True)
    
    def __str__(self):
        return self.title