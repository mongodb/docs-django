# start-models
from django.db import models
from django_mongodb_backend.fields import EmbeddedModelField, ArrayField

class Award(models.Model):
    wins = models.IntegerField(default=0)
    nominations = models.IntegerField(default=0)
    text = models.CharField(max_length=100)

    class Meta:
        managed = False

class Movie(models.Model):
    title = models.CharField(max_length=200)
    plot = models.TextField(blank=True)
    runtime = models.IntegerField(default=0)
    released = models.DateTimeField("release date", null=True, blank=True)
    awards = EmbeddedModelField(Award)
    genres = ArrayField(models.CharField(max_length=100), null=True, blank=True)

    class Meta:
        db_table = "movies"
        managed = False
    
    def __str__(self):
        return self.title
# end-models

# start-all
Movie.objects.all()
# end-all

# start-filter
Movie.objects.filter(runtime=300)
# end-filter

# start-get
Movie.objects.get(title="Finding Nemo")
# end-get

# start-exclude
Movie.objects.exclude(released__lt=timezone.make_aware(datetime(1980, 1, 1)))
# end-exclude

# start-filter-contains
Movie.objects.filter(plot__contains="coming-of-age")
# end-filter-contains

# start-filter-lte
Movie.objects.filter(runtime__lte=50)
# end-filter-lte

# start-filter-relationships
Movie.objects.filter(awards__wins=93)
# end-filter-relationships

# start-filter-combine
Movie.objects.filter(awards__text__istartswith="nominated")
# end-filter-combine

# start-sort
Movie.objects.filter(title__startswith="Rocky").order_by("released")
# end-sort

# start-limit
Movie.objects.filter(released=timezone.make_aware(datetime(2010, 7, 1)))[3:6]
# end-limit

# start-first
Movie.objects.filter(genres=["Crime", "Comedy"]).first()
# end-first