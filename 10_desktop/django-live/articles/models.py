from django.db import models

# Create your models here.
class Article(models.Model):
    # title
    title = models.CharField(max_length=50)
    # content
    content = models.TextField()
    # created_at / create 했을 때
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at
    # update 할 때 마다
    updated_at = models.DateTimeField(auto_now=True)