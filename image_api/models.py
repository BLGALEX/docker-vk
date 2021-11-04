from django.db import models


class Image(models.Model):

    image = models.ImageField(upload_to='images/', default='Images/None/No-img.jpg')

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image)
        super().delete()