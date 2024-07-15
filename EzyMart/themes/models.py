from django.db import models

# Create model from themes
class SiteSetting(models.Model):
  banner=models.ImageField(upload_to="media/site/")
  caption=models.TextField()

