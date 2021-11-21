from django.db import models
import uuid

# class BaseModel(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
         return self.title

         
