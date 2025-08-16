from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Posts(models.Model) :
    title = models.CharField(max_length=100) 
    content = models.TextField()
    data_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="liked_posts", blank=True)
    
    def __str__(self) :
        return self.title 
    