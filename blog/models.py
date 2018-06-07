from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone

# command
# python manage.py runserver
# python manage.py makemigrations blog
# python manage.py sqlmigrate blog 0001
# python manage.py migrate


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    # other model field type
    # https://docs.djangoproject.com/en/1.8/ref/models/fields/
    title = models.CharField(max_length=250)                # CharField in SQL db to VARCHAR
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=django.utils.timezone.now)
    created = models.DateTimeField(auto_now_add=True)       # use auto_now_add auto save when addd
    updated = models.DateTimeField(auto_now=True)           # auto update time
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
