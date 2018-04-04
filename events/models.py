from django.db import models
from django.utils.text import slugify
from datetime import datetime
from django.db.models.signals import pre_save
from django.utils.timezone import now as timezone
from django.urls import reverse
import random, string
from .utils import unique_slug_generator, random_string_generator

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length = 32)
    tag = models.SlugField()
    description = models.TextField(default = '')
    date = models.DateTimeField(default=datetime.now())
    organiser = models.CharField(max_length = 32)
    contact = models.EmailField(default="abc@gmail.com")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.tag = unique_slug_generator(self)
        super(Event, self).save()

    def get_absolute_url(self):
        return reverse("events:detail", kwargs={"slug": self.tag})
