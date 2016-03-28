from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Subject, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Page(models.Model):
    Subject = models.ForeignKey(Subject)
    title = models.CharField(max_length=128)
    url = models.URLField()
    view = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title
