from django.db import models

# Create your models here.

class ProductionCompany(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    def total_content_duration(self):
        get_producers = ProductionCompany.objects.get(pk=self.id).producer_set.all()
        shows = [e.program_set.all() for e in get_producers]
        unique_shows = list(set([j for i in shows for j in i]))
        duration = [int(x.dur) for x in unique_shows]
        return sum(duration) 
    
class Producer(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    company = models.ForeignKey(ProductionCompany, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    dur = models.IntegerField()
    producers = models.ManyToManyField(Producer)
    
    def __str__(self):
        return self.name
