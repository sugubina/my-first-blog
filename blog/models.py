from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage

# fs = FileSystemStorage(location='/media/photos')

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    photo = models.ImageField(upload_to='documents/', null=True, blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title