from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=250)
    video = models.FileField(upload_to='videos/%Y/%m/%d/')
    created_date = models.DateField(auto_now_add=True)

    @property
    def size(self):
        return self.video.size/(1024**2)