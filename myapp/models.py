from django.db import models

# Create your models here.


class Topic(models.Model):
    topic_name = models.CharField(max_length=30, unique=True, blank=False)

    def __str__(self):
        return self.topic_name


class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True, blank=False)
    url = models.URLField(max_length=100, unique=True, blank=False)

    def __str__(self):
        return self.name


class AccessDetails(models.Model):
    webpage = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    def __str__(self):
        print(self.datetime)
        return str(self.datetime).split(" ")[0]
