from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
import uuid
import os




class Category(models.Model):
  title = models.CharField(max_length=50)

  def __str__(self):
   return self.title

class Post(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='post')
  title = models.CharField(max_lengt=200)
  slug = models.SlugField(unique=True, maxx_length=200, blank=True)
  content = models.TextField(max_length=10000)
  created_at = models.DateTimeField(deafult=timezone.now)
  update_at = models.DateTimeField(auto_now=True)
  allow_comments = models.BooleanField(default=True)

  def __str__(self):
   return self.title
  
  @property
  def amount_comments(self):
    return self.comments.count()
  
  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = self.generate_unique_slug()

      super().save(*args, **kwargs)

  def generate_unique_slug(self):
    slug = slugify(self.title)
    unique_slug = slug
    num = 1

    while Post.objects.filter(slug=unique_slug).exist():
      unique_slug = f'{slug}-{num}'
      num += 1

    return unique_slug

  
class Comment(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE, relate_name='comments')
  content = models.TextField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)

  def __str__(self):
   return self.id
