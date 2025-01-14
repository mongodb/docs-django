# start-models
from django.db import models
from django_mongodb_backend.fields import EmbeddedModelField, ArrayField

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
    
class Award(models.Model):
    wins = models.IntegerField(default=0)
    nominations = models.IntegerField(default=0)
    text = models.CharField(max_length=100)

    class Meta:
        managed = False
# end-models

# start-all
# end-all