from django.db import models

class Product(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICE = ((LIVE, 'Live'), (DELETE, 'Delete'))
    title = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='media/')
    description = models.TextField()
    delete_status = models.IntegerField(choices=DELETE_CHOICE, default=LIVE)
    priority = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
