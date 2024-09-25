from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):       # models.Model it means the post is django model then  saves it in the database

    # define each filed and determine the type of every one
    title = models.CharField(max_length=200)            # models.CharField define text with limited number of chars
    text = models.TextField()                           # models.TextField long text without limit
    created_date = models.DateTimeField(default=timezone.now)           # models.DateTimeField this is a date time 
    published_date = models.DateTimeField(blank=True, null=True)
    
    # models.ForeignKey this is a link to another model      
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)     


    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title