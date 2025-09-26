from django.db import models
from storages.backends.azure_storage import AzureStorage


class Post(models.Model):
    image = models.ImageField(storage=AzureStorage())
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField()
