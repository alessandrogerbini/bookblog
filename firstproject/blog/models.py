from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    
    class Meta:
        ordering = ['last_name']
    
class Blogpost(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publication_date = models.DateField()
    body = models.TextField()
    
    def __unicode__(self):
        return self.title