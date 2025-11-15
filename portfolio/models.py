from django.db import models

from django.urls import reverse

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio:project_detail', args=[self.slug])

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField(help_text='Percent 0-100')

    def __str__(self):
        return f"{self.name} ({self.level}%)"

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.title} @ {self.company}"

class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    excerpt = models.TextField(blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio:blog_detail', args=[self.slug])

class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name} <{self.email}>"
